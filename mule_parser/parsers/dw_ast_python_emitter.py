"""
AST → Python emitter for DataWeave scripts.

Generates Python from the parsed AST structure — no regex shape matching,
no embedded script literals, no connector-specific assumptions.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from mule_parser.parsers.dw_ast.nodes import (
    ArrayLiteral,
    BinaryOp,
    DefaultExpr,
    Expr,
    FunDirective,
    FunctionCall,
    Identifier,
    IfElse,
    ImportDirective,
    IndexSelector,
    Lambda,
    Literal,
    ObjectLiteral,
    OutputDirective,
    Program,
    Selector,
    UnaryOp,
    VarDirective,
)


@dataclass
class EmitScope:
    """Lexical scope for lambda parameters and bound names."""

    params: dict[str, str] = field(default_factory=dict)
    parent: EmitScope | None = None

    def resolve(self, name: str) -> str | None:
        if name in self.params:
            return self.params[name]
        if self.parent:
            return self.parent.resolve(name)
        return None

    def child(self, bindings: dict[str, str]) -> EmitScope:
        merged = dict(self.params)
        merged.update(bindings)
        return EmitScope(params=merged, parent=self)


class PythonEmitter:
    """Emit Python source from a DataWeave ``Program`` AST."""

    def emit_program(self, prog: Program) -> tuple[list[str], str, str]:
        """Return ``(preamble_lines, result_expr, output_format)``."""
        output_format = ""
        for directive in prog.directives:
            if isinstance(directive, OutputDirective):
                output_format = directive.mime_type.strip()

        preamble: list[str] = ["    _ctx = dw.DWContext(payload)"]
        var_exprs: dict[str, str] = {}
        fun_names = {d.name for d in prog.directives if isinstance(d, FunDirective)}
        builtins = self._collect_builtins(prog)

        for directive in prog.directives:
            if isinstance(directive, VarDirective):
                expr = self.emit_expr(directive.expr, EmitScope(), var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
                var_exprs[directive.name] = expr
                preamble.append(f"    _ctx.vars[{directive.name!r}] = {expr}")
            elif isinstance(directive, FunDirective):
                preamble.append(self._emit_function(directive, var_exprs, fun_names, builtins))

        if not prog.body:
            return preamble, "None", output_format

        result = self.emit_expr(prog.body, EmitScope(), var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return preamble, result, output_format

    def _collect_builtins(self, prog: Program) -> set[str]:
        names: set[str] = set()
        for directive in prog.directives:
            if isinstance(directive, ImportDirective):
                if directive.mappings == ["*"]:
                    if "Strings" in (directive.module or ""):
                        names.update({"startsWith", "endsWith", "substringAfter", "substringBefore", "contains"})
                    if "Arrays" in (directive.module or ""):
                        names.update({"slice", "indexOf"})
                    if "Objects" in (directive.module or ""):
                        names.update({"mergeWith"})
                elif directive.mappings:
                    names.update(directive.mappings)
        return names

    def _emit_function(
        self,
        directive: FunDirective,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        param_list = ", ".join(self._param_py_name(p) for p in directive.params) or "_"
        scope = EmitScope(params={p: self._param_py_name(p) for p in directive.params})
        body = self.emit_expr(directive.expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"    def _dw_fun_{directive.name}({param_list}):\n        return {body}"

    def emit_expr(
        self,
        expr: Expr,
        scope: EmitScope,
        *,
        var_exprs: dict[str, str] | None = None,
        fun_names: set[str] | None = None,
        builtins: set[str] | None = None,
    ) -> str:
        var_exprs = var_exprs or {}
        fun_names = fun_names or set()
        builtins = builtins or set()

        if isinstance(expr, Literal):
            return repr(expr.value)

        if isinstance(expr, Identifier):
            return self._emit_identifier(expr.name, scope, var_exprs, fun_names)

        if isinstance(expr, Selector):
            base = self.emit_expr(expr.left, scope, var_exprs=var_exprs, fun_names=fun_names)
            if base == "_ctx.payload":
                return f"dw.nested_get(_ctx.payload, {expr.field!r})"
            if base == "_ctx.vars":
                return f"dw.nested_get(_ctx.vars, {expr.field!r})"
            if base == "_ctx.attributes":
                return f"dw.nested_get(_ctx.attributes, {expr.field!r})"
            return f"dw.nested_get({base}, {expr.field!r})"

        if isinstance(expr, IndexSelector):
            base = self.emit_expr(expr.left, scope, var_exprs=var_exprs, fun_names=fun_names)
            index = self.emit_expr(expr.index, scope, var_exprs=var_exprs, fun_names=fun_names)
            return f"dw.index_get({base}, {index})"

        if isinstance(expr, UnaryOp):
            operand = self.emit_expr(expr.operand, scope, var_exprs=var_exprs, fun_names=fun_names)
            if expr.operator == "?":
                return f"_ctx.is_present({operand})"
            if expr.operator == "not":
                return f"(not {operand})"
            if expr.operator == "-":
                return f"(-({operand}))"
            return operand

        if isinstance(expr, DefaultExpr):
            if isinstance(expr.left, IndexSelector) and isinstance(expr.left.index, Literal) and expr.left.index.value == 0:
                seq = self.emit_expr(expr.left.left, scope, var_exprs=var_exprs, fun_names=fun_names)
                default = self.emit_expr(expr.right, scope, var_exprs=var_exprs, fun_names=fun_names)
                return f"dw.first_or({seq}, {default})"
            left = self.emit_expr(expr.left, scope, var_exprs=var_exprs, fun_names=fun_names)
            right = self.emit_expr(expr.right, scope, var_exprs=var_exprs, fun_names=fun_names)
            return f"(({left}) if ({left}) not in (None, '') else ({right}))"

        if isinstance(expr, IfElse):
            cond = self.emit_expr(expr.condition, scope, var_exprs=var_exprs, fun_names=fun_names)
            then_e = self.emit_expr(expr.then_expr, scope, var_exprs=var_exprs, fun_names=fun_names)
            else_e = self.emit_expr(expr.else_expr, scope, var_exprs=var_exprs, fun_names=fun_names)
            return f"({then_e} if {cond} else {else_e})"

        if isinstance(expr, ArrayLiteral):
            items = [self.emit_expr(el, scope, var_exprs=var_exprs, fun_names=fun_names) for el in expr.elements]
            return f"[{', '.join(items)}]"

        if isinstance(expr, ObjectLiteral):
            return self._emit_object(expr, scope, var_exprs, fun_names, builtins)

        if isinstance(expr, Lambda):
            return self._emit_lambda(expr, scope, var_exprs, fun_names, builtins)

        if isinstance(expr, FunctionCall):
            return self._emit_call(expr, scope, var_exprs, fun_names, builtins)

        if isinstance(expr, BinaryOp):
            return self._emit_binary(expr, scope, var_exprs, fun_names, builtins)

        raise NotImplementedError(f"Unsupported AST node: {type(expr).__name__}")

    def _emit_object(
        self,
        expr: ObjectLiteral,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        pairs: list[str] = []
        merges: list[str] = []
        for key_expr, val_expr in expr.pairs:
            key = self._object_key(key_expr, scope, var_exprs, fun_names)
            if (
                isinstance(val_expr, IfElse)
                and isinstance(val_expr.else_expr, Literal)
                and val_expr.else_expr.value is None
            ):
                cond = self.emit_expr(val_expr.condition, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
                val = self.emit_expr(val_expr.then_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
                merges.append(f"({{{key}: {val}}} if {cond} else {{}})")
            else:
                val = self.emit_expr(val_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
                pairs.append(f"{key}: {val}")
        result = "{" + ", ".join(pairs) + "}" if pairs else "{}"
        for merge in merges:
            result = f"dw.merge_objects({result}, {merge})"
        return result

    _DW_BUILTINS = {
        "lower": "dw.dw_lower({})",
        "upper": "dw.dw_upper({})",
        "sizeOf": "dw.dw_size({})",
        "randomInt": "dw.dw_random_int({})",
        "slice": "dw.dw_slice({})",
        "indexOf": "dw.dw_index_of({})",
        "substringAfter": "dw.str_substring_after({})",
        "substringBefore": "dw.str_substring_before({})",
        "startsWith": "dw.str_starts_with({})",
        "endsWith": "dw.str_ends_with({})",
    }

    def _emit_builtin_call(self, name: str, args: list[str]) -> str | None:
        if name == "lower" and len(args) == 1:
            return f"dw.dw_lower({args[0]})"
        if name == "upper" and len(args) == 1:
            return f"dw.dw_upper({args[0]})"
        if name == "sizeOf" and len(args) == 1:
            return f"dw.dw_size({args[0]})"
        if name == "randomInt" and len(args) == 1:
            return f"dw.dw_random_int({args[0]})"
        if name == "slice":
            return f"dw.dw_slice({', '.join(args)})"
        if name == "indexOf" and len(args) == 2:
            return f"dw.dw_index_of({args[0]}, {args[1]})"
        if name == "substringAfter" and len(args) == 2:
            return f"dw.str_substring_after({args[0]}, {args[1]})"
        if name == "substringBefore" and len(args) == 2:
            return f"dw.str_substring_before({args[0]}, {args[1]})"
        if name == "startsWith" and len(args) == 2:
            return f"dw.str_starts_with({args[0]}, {args[1]})"
        if name == "endsWith" and len(args) == 2:
            return f"dw.str_ends_with({args[0]}, {args[1]})"
        if name in ("p", "Mule::p", "p_str") and args:
            return f"dw.dw_property({args[0]})"
        return None

    def _emit_identifier(
        self,
        name: str,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
    ) -> str:
        bound = scope.resolve(name)
        if bound:
            return bound
        if name in ("$", "item"):
            return scope.resolve("$") or scope.resolve("item") or "_item"
        if name == "payload":
            return "_ctx.payload"
        if name == "vars":
            return "_ctx.vars"
        if name == "attributes":
            return "_ctx.attributes"
        if name in var_exprs:
            return f"_ctx.vars[{name!r}]"
        if name in fun_names:
            return f"_dw_fun_{name}"
        if name == "now":
            return "dw.dw_now()"
        return f"_ctx.get_path({name!r})"

    def _object_key(
        self,
        key_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
    ) -> str:
        if isinstance(key_expr, Literal) and isinstance(key_expr.value, str):
            return repr(key_expr.value)
        if isinstance(key_expr, Identifier):
            return repr(key_expr.name)
        return self.emit_expr(key_expr, scope, var_exprs=var_exprs, fun_names=fun_names)

    def _emit_lambda(
        self,
        expr: Lambda,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        bindings: dict[str, str] = {}
        py_params: list[str] = []
        for i, param in enumerate(expr.params):
            py_name = self._param_py_name(param)
            bindings[param] = py_name
            if param == "$" or i == 0:
                bindings["$"] = py_name
                bindings["item"] = py_name
            if py_name not in py_params:
                py_params.append(py_name)
        if not py_params:
            py_params = ["_item"]
            bindings["$"] = "_item"
            bindings["item"] = "_item"
        child = scope.child(bindings)
        body = self.emit_expr(expr.body, child, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"(lambda {', '.join(py_params)}: {body})"

    def _emit_call(
        self,
        expr: FunctionCall,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        args = [self.emit_expr(a, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins) for a in expr.args]
        if isinstance(expr.func, Identifier):
            name = expr.func.name
            if name == "write" and args:
                return f"dw.dw_write({args[0]})"
            if name in fun_names:
                return f"_dw_fun_{name}({', '.join(args)})"
            builtin = self._emit_builtin_call(name, args)
            if builtin:
                return builtin
        func = self.emit_expr(expr.func, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"{func}({', '.join(args)})"

    def _emit_binary(
        self,
        expr: BinaryOp,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        op = expr.operator
        left = self.emit_expr(expr.left, scope, var_exprs=var_exprs, fun_names=fun_names)
        right_expr = expr.right

        if op == "map":
            return self._emit_map(left, right_expr, scope, var_exprs, fun_names, builtins)
        if op == "filter":
            return self._emit_filter(left, right_expr, scope, var_exprs, fun_names, builtins)
        if op == "flatMap":
            fn = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins) if isinstance(right_expr, Lambda) else None
            if fn:
                return f"[y for _item in dw.as_list({left}) for y in dw.as_list(({fn})(_item))]"
        if op == "distinctBy":
            return self._emit_distinct_by(left, right_expr, scope, var_exprs, fun_names, builtins)
        if op == "orderBy":
            return self._emit_order_by(left, right_expr, scope, var_exprs, fun_names, builtins)
        if op == "groupBy":
            return self._emit_group_by(left, right_expr, scope, var_exprs, fun_names, builtins)
        if op == "joinBy":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.join_values({left}, {right})"
        if op == "mergeWith":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.merge_objects({left}, {right})"
        if op == "++":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            dedup_key = self._shared_distinct_key(expr.left, right_expr)
            if dedup_key:
                return f"dw.distinct_by(dw.as_list({left}) + dw.as_list({right}), {dedup_key!r})"
            if isinstance(expr.left, Identifier) and expr.left.name == "$":
                item = scope.resolve("$") or scope.resolve("item") or "_item"
                return f"dw.dw_plus({item}, {right})"
            return f"dw.dw_concat({left}, {right})"
        if op == "~=":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.loose_eq({left}, {right})"
        if op == "to":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.dw_range({left}, {right})"
        if op == "contains":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.str_contains({left}, {right})"
        if op == "startsWith":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.str_starts_with({left}, {right})"
        if op == "endsWith":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.str_ends_with({left}, {right})"
        if op == "substringAfter":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.str_substring_after({left}, {right})"
        if op == "substringBefore":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.str_substring_before({left}, {right})"
        if op == "as":
            type_name = right_expr.name if isinstance(right_expr, Identifier) else str(right_expr)
            if type_name == "DateTime":
                return f"dw.as_datetime({left})"
            if type_name == "Number":
                return f"dw.as_number({left})"
            return left
        if op == "and":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"({left} and {right})"
        if op == "or":
            right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"({left} or {right})"

        if op == "-":
            if isinstance(expr.left, Identifier) and expr.left.name == "$":
                if isinstance(right_expr, Literal) and isinstance(right_expr.value, str):
                    item = scope.resolve("$") or scope.resolve("item") or "_item"
                    return f"dw.remove_field({item}, {right_expr.value!r})"

        right = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        py_op = {"==": "==", "!=": "!=", ">": ">", "<": "<", ">=": ">=", "<=": "<=", "+": "+", "-": "-", "*": "*", "/": "/"}.get(op, op)
        return f"({left} {py_op} {right})"

    def _shared_distinct_key(self, left_expr: Expr, right_expr: Expr) -> str | None:
        """When both sides are ``distinctBy $.field``, return ``field`` for post-concat dedup."""

        def _key(node: Expr) -> str | None:
            if isinstance(node, BinaryOp) and node.operator == "distinctBy":
                sel = node.right
                if isinstance(sel, Selector) and isinstance(sel.left, Identifier) and sel.left.name == "$":
                    return sel.field
            return None

        lk, rk = _key(left_expr), _key(right_expr)
        return lk if lk and lk == rk else None

    def _param_py_name(self, param: str) -> str:
        if param in ("$", "item", ""):
            return "_item"
        return f"_{param}"

    def _lambda_scope(self, expr: Lambda, scope: EmitScope) -> tuple[list[str], EmitScope]:
        bindings: dict[str, str] = {}
        py_params: list[str] = []
        for i, param in enumerate(expr.params):
            py_name = self._param_py_name(param)
            bindings[param] = py_name
            if param == "$" or i == 0:
                bindings["$"] = py_name
                bindings["item"] = py_name
            if py_name not in py_params:
                py_params.append(py_name)
        if not py_params:
            py_params = ["_item"]
            bindings["$"] = "_item"
            bindings["item"] = "_item"
        return py_params, scope.child(bindings)

    def _emit_map(
        self,
        left: str,
        right_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        if isinstance(right_expr, Lambda):
            py_params, child = self._lambda_scope(right_expr, scope)
            body = self.emit_expr(right_expr.body, child, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"[{body} for {py_params[0]} in dw.as_list({left})]"
        py_param = "_item"
        child = scope.child({"$": py_param, "item": py_param})
        body = self.emit_expr(right_expr, child, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"[{body} for {py_param} in dw.as_list({left})]"

    def _emit_filter(
        self,
        left: str,
        right_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        if isinstance(right_expr, Lambda):
            py_params, child = self._lambda_scope(right_expr, scope)
            pred = self.emit_expr(right_expr.body, child, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"[{py_params[0]} for {py_params[0]} in dw.as_list({left}) if ({pred})]"
        filter_scope = scope.child({"$": "_row"})
        pred = self.emit_expr(right_expr, filter_scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"[ _row for _row in dw.as_list({left}) if ({pred}) ]"

    def _emit_distinct_by(
        self,
        left: str,
        right_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        if isinstance(right_expr, Selector) and isinstance(right_expr.left, Identifier) and right_expr.left.name == "$":
            return f"dw.distinct_by([r for r in dw.as_list({left}) if isinstance(r, dict)], {right_expr.field!r})"
        if isinstance(right_expr, Lambda):
            fn = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.distinct_by_selector({left}, {fn})"
        key = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"dw.distinct_by_selector({left}, {key})"

    def _emit_order_by(
        self,
        left: str,
        right_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        order_scope = scope.child({"$": "_item", "item": "_item"})
        if isinstance(right_expr, Lambda):
            fn = self.emit_expr(right_expr, order_scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.sort_by_selector({left}, {fn})"
        if isinstance(right_expr, (IfElse, Selector, IndexSelector, BinaryOp, UnaryOp)):
            key = self.emit_expr(right_expr, order_scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.sort_by_selector({left}, lambda _item: {key})"
        if isinstance(right_expr, Identifier):
            return f"dw.sort_by_selector({left}, {right_expr.name!r})"
        key = self.emit_expr(right_expr, order_scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"dw.sort_by_selector({left}, {key})"

    def _emit_group_by(
        self,
        left: str,
        right_expr: Expr,
        scope: EmitScope,
        var_exprs: dict[str, str],
        fun_names: set[str],
        builtins: set[str],
    ) -> str:
        if isinstance(right_expr, Lambda):
            fn = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
            return f"dw.group_by_selector({left}, {fn})"
        if isinstance(right_expr, Selector) and isinstance(right_expr.left, Identifier) and right_expr.left.name == "$":
            return f"dw.group_by_selector({left}, {right_expr.field!r})"
        key = self.emit_expr(right_expr, scope, var_exprs=var_exprs, fun_names=fun_names, builtins=builtins)
        return f"dw.group_by_selector({left}, {key})"


__all__ = ["PythonEmitter", "EmitScope"]
