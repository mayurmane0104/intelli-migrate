# Arithmetics - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/jle-arithmetics.html](https://docs.aws.amazon.com/quick/latest/userguide/jle-arithmetics.html)

---

The following table shows arithmetic expressions that can be used with JSON expression language.

| Operation | Expression | Input | Output | 
|---|---|---|---|
| Addition | `["+", operand1, operand2]` | `{ sum: ["+", 2, 4] }` | `{ sum: 6 }` | 
| Subtraction | `["-", operand1, operand2]` | `{ difference: ["-", 10, 3] }` | `{ difference: 7 }` | 
| Multiplication | `["*", operand1, operand2]` | `{ product: ["*", 5, 6] }` | `{ product: 30 }` | 
| Division | `["/", operand1, operand2]` | `{ quotient: ["/", 20, 4] }` | `{ quotient: 5 }` | 
| Modulo | `["%", operand1, operand2]` | `{ remainder: ["%", 15, 4] }` | `{ remainder: 3 }` | 
| Exponentiation | `["**", base, exponent]` | `{ power: ["**", 2, 3] }` | `{ power: 8 }` | 
| Absolute Value | `["abs", operand]` | `{ absolute: ["abs", -5] }` | `{ absolute: 5 }` | 
| Square Root | `["sqrt", operand]` | `{ sqroot: ["sqrt", 16] }` | `{ sqroot: 4 }` | 
| Logarithm (base 10) | `["log10", operand]` | `{ log: ["log10", 100] }` | `{ log: 2 }` | 
| Natural Logarithm | `["ln", operand]` | `{ ln: ["ln", Math.E] }` | `{ ln: 1 }` | 
| Round | `["round", operand]` | `{ rounded: ["round", 3.7] }` | `{ rounded: 4 }` | 
| Floor | `["floor", operand]` | `{ floor: ["floor", 3.7] }` | `{ floor: 3 }` | 
| Ceiling | `["ceil", operand]` | `{ ceiling: ["ceil", 3.2] }` | `{ ceiling: 4 }` | 
| Sine | `["sin", operand]` | `{ sine: ["sin", 0] }` | `{ sine: 0 }` | 
| Cosine | `["cos", operand]` | `{ cosine: ["cos", 0] }` | `{ cosine: 1 }` | 
| Tangent | `["tan", operand]` | `{ tangent: ["tan", Math.PI] }` | `{ tangent: 0 }` |