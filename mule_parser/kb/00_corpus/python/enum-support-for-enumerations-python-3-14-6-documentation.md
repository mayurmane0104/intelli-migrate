# enum — Support for enumerations — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/enum.html](https://docs.python.org/library/enum.html)

---

`enum` — Support for enumerations[¶](#module-enum)

Added in version 3.4.

**Source code:** [Lib/enum.py](https://github.com/python/cpython/tree/3.14/Lib/enum.py)

An enumeration:

- is a set of symbolic names (members) bound to unique values 
- can be iterated over to return its canonical (i.e. non-alias) members in definition order 
- uses - *call*syntax to return members by value
- uses - *index*syntax to return members by name

Enumerations are created either by using [ class](../reference/compound_stmts.html#class) syntax, or by
using function-call syntax:

```
>>> from enum import Enum
>>> # class syntax
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
>>> # functional syntax
>>> Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])
```
Even though we can use [ class](../reference/compound_stmts.html#class) syntax to create Enums, Enums
are not normal Python classes.  See

[How are Enums different?](../howto/enum.html#enum-class-differences)for more details.

Note

Nomenclature

- The class - `Color`is an- *enumeration*(or- *enum*)
- The attributes - `Color.RED`,- `Color.GREEN`, etc., are- *enumeration members*(or- *members*) and are functionally constants.
- The enum members have - *names*and- *values*(the name of- `Color.RED`is- `RED`, the value of- `Color.BLUE`is- `3`, etc.)

## Module contents[¶](#module-contents)

The

`type`for Enum and its subclasses.Base class for creating enumerated constants.

Base class for creating enumerated constants that can be combined using the bitwise operations without losing their

[membership.](#enum.Flag)`Flag`An enumeration with the values

`CONTINUOUS`,`NAMED_FLAGS`, and`UNIQUE`, for use with[to ensure various constraints are met by a given enumeration.](#enum.verify)`verify()`An enumeration with the values

`STRICT`,`CONFORM`,`EJECT`, and`KEEP`which allows for more fine-grained control over how invalid values are dealt with in an enumeration.Instances are replaced with an appropriate value for Enum members.

[defaults to the lower-cased version of the member name, while other Enums default to 1 and increase from there.](#enum.StrEnum)`StrEnum`Allows

[members to have attributes without conflicting with member names. The](#enum.Enum)`Enum``value`and`name`attributes are implemented this way.Enum class decorator that ensures only one name is bound to any one value.

Enum class decorator that checks user-selectable constraints on an enumeration.

Make

`obj`a member. Can be used as a decorator.Do not make

`obj`a member. Can be used as a decorator.Return a list of all power-of-two integers contained in a flag.

Like built-in

[, except negative values are represented in two’s complement, and the leading bit always indicates sign (](functions.html#bin)`bin()``0`implies positive,`1`implies negative).

Added in version 3.6: `Flag`, `IntFlag`, `auto`

Added in version 3.11: `StrEnum`, `EnumCheck`, `ReprEnum`, `FlagBoundary`, `property`, `member`, `nonmember`, `global_enum`, `show_flag_values`

Added in version 3.13: `EnumDict`

## Data types[¶](#data-types)

- 
*class*enum.EnumType[¶](#enum.EnumType)
- *EnumType*is the- [metaclass](../glossary.html#term-metaclass)for- *enum*enumerations. It is possible to subclass- *EnumType*– see- [Subclassing EnumType](../howto/enum.html#enumtype-examples)for details.- `EnumType`is responsible for setting the correct- `__repr__()`,- `__str__()`,- `__format__()`, and- `__reduce__()`methods on the final- *enum*, as well as creating the enum members, properly handling duplicates, providing iteration over the enum class, etc.- Added in version 3.11: Before 3.11 - `EnumType`was called- `EnumMeta`, which is still available as an alias.- 
__call__(*cls*,*value*,*names=None*,***,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[¶](#enum.EnumType.__call__)
- This method is called in two different ways: - to look up an existing member: - cls:
- The enum class being called. 
- value:
- The value to lookup. 
 
- to use the - `cls`enum to create a new enum (only if the existing enum does not have any members):- cls:
- The enum class being called. 
- value:
- The name of the new Enum to create. 
- names:
- The names/values of the members for the new Enum. 
- module:
- The name of the module the new Enum is created in. 
- qualname:
- The actual location in the module where this Enum can be found. 
- type:
- A mix-in type for the new Enum. 
- start:
- The first integer value for the Enum (used by - `auto`
- boundary:
- How to handle out-of-range values from bit operations ( - `Flag`
 
 
 - 
__contains__(*cls*,*member*)[¶](#enum.EnumType.__contains__)
- Returns - `True`if member belongs to the- `cls`:- >>> some_var = Color.RED >>> some_var in Color True >>> Color.RED.value in Color True - Changed in version 3.12: Before Python 3.12, a - `TypeError`is raised if a non-Enum-member is used in a containment check.
 - 
__dir__(*cls*)[¶](#enum.EnumType.__dir__)
- Returns - `['__class__', '__doc__', '__members__', '__module__']`and the names of the members in- *cls*:- >>> dir(Color) ['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__'] 
 - 
__getitem__(*cls*,*name*)[¶](#enum.EnumType.__getitem__)
- Returns the Enum member in - *cls*matching- *name*, or raises a- `KeyError`- >>> Color['BLUE'] <Color.BLUE: 3> 
 - 
__iter__(*cls*)[¶](#enum.EnumType.__iter__)
- Returns each member in - *cls*in definition order:- >>> list(Color) [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>] 
 - 
__len__(*cls*)[¶](#enum.EnumType.__len__)
- Returns the number of members in - *cls*:- >>> len(Color) 3 
 - 
__members__[¶](#enum.EnumType.__members__)
- Returns a mapping of every enum name to its member, including aliases 
 - 
__reversed__(*cls*)[¶](#enum.EnumType.__reversed__)
- Returns each member in - *cls*in reverse definition order:- >>> list(reversed(Color)) [<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>] 
 
- 
__call__(

- 
*class*enum.Enum[¶](#enum.Enum)
- *Enum*is the base class for all- *enum*enumerations.- 
name[¶](#enum.Enum.name)
- The name used to define the - `Enum`member:- >>> Color.BLUE.name 'BLUE' 
 - 
value[¶](#enum.Enum.value)
- The value given to the - `Enum`member:- >>> Color.RED.value 1 - Value of the member, can be set in - `__new__()`- Note - Enum member values - Member values can be anything: - `int`- `str`- `auto`- `auto`for the details.- While mutable/unhashable values, such as - `dict`- `list`- `dataclass`
 - 
_name_[¶](#enum.Enum._name_)
- Name of the member. 
 - 
_order_[¶](#enum.Enum._order_)
- No longer used, kept for backward compatibility. (class attribute, removed during class creation). - The - `_order_`attribute can be provided to help keep Python 2 / Python 3 code in sync. It will be checked against the actual order of the enumeration and raise an error if the two do not match:- >>> class Color(Enum): ... _order_ = 'RED GREEN BLUE' ... RED = 1 ... BLUE = 3 ... GREEN = 2 ... Traceback (most recent call last): ... TypeError: member order does not match _order_: ['RED', 'BLUE', 'GREEN'] ['RED', 'GREEN', 'BLUE'] - Note - In Python 2 code the - `_order_`attribute is necessary as definition order is lost before it can be recorded.- Added in version 3.6. 
 - 
_ignore_[¶](#enum.Enum._ignore_)
- `_ignore_`is only used during creation and is removed from the enumeration once creation is complete.- `_ignore_`is a list of names that will not become members, and whose names will also be removed from the completed enumeration. See- [TimePeriod](../howto/enum.html#enum-time-period)for an example.- Added in version 3.7. 
 - 
__dir__(*self*)[¶](#enum.Enum.__dir__)
- Returns - `['__class__', '__doc__', '__module__', 'name', 'value']`and any public methods defined on- *self.__class__*:- >>> from enum import Enum >>> import datetime as dt >>> class Weekday(Enum): ... MONDAY = 1 ... TUESDAY = 2 ... WEDNESDAY = 3 ... THURSDAY = 4 ... FRIDAY = 5 ... SATURDAY = 6 ... SUNDAY = 7 ... @classmethod ... def today(cls): ... print(f'today is {cls(dt.date.today().isoweekday()).name}') ... >>> dir(Weekday.SATURDAY) ['__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value'] 
 - 
_generate_next_value_(*name*,*start*,*count*,*last_values*)[¶](#enum.Enum._generate_next_value_)
- name:
- The name of the member being defined (e.g. ‘RED’). 
- start:
- The start value for the Enum; the default is 1. 
- count:
- The number of members currently defined, not including this one. 
- last_values:
- A list of the previous values. 
 - A - *staticmethod*that is used to determine the next value returned by- `auto`- Note - For standard - `Enum`classes the next value chosen is the highest value seen incremented by one.- For - `Flag`- This method may be overridden, e.g.: - >>> from enum import auto, Enum >>> class PowersOfThree(Enum): ... @staticmethod ... def _generate_next_value_(name, start, count, last_values): ... return 3 ** (count + 1) ... FIRST = auto() ... SECOND = auto() ... >>> PowersOfThree.SECOND.value 9 - Added in version 3.6. - Changed in version 3.13: Prior versions would use the last seen value instead of the highest value. 
 - 
__init__(*self*,**args*,***kwds*)[¶](#enum.Enum.__init__)
- By default, does nothing. If multiple values are given in the member assignment, those values become separate arguments to - `__init__`; e.g.- >>> from enum import Enum >>> class Weekday(Enum): ... MONDAY = 1, 'Mon' - `Weekday.__init__()`would be called as- `Weekday.__init__(self, 1, 'Mon')`
 - 
__init_subclass__(*cls*,***kwds*)[¶](#enum.Enum.__init_subclass__)
- A - *classmethod*that is used to further configure subsequent subclasses. By default, does nothing.
 - 
_missing_(*cls*,*value*)[¶](#enum.Enum._missing_)
- A - *classmethod*for looking up values not found in- *cls*. By default it does nothing, but can be overridden to implement custom search behavior:- >>> from enum import auto, StrEnum >>> class Build(StrEnum): ... DEBUG = auto() ... OPTIMIZED = auto() ... @classmethod ... def _missing_(cls, value): ... value = value.lower() ... for member in cls: ... if member.value == value: ... return member ... return None ... >>> Build.DEBUG.value 'debug' >>> Build('deBUG') <Build.DEBUG: 'debug'> - Added in version 3.6. 
 - 
__new__(*cls*,**args*,***kwds*)[¶](#enum.Enum.__new__)
- By default, doesn’t exist. If specified, either in the enum class definition or in a mixin class (such as - `int`), all values given in the member assignment will be passed; e.g.- >>> from enum import Enum >>> class MyIntEnum(int, Enum): ... TWENTYSIX = '1a', 16 - results in the call - `int('1a', 16)`and a value of- `26`for the member.- Note - When writing a custom - `__new__`, do not use- `super().__new__`– call the appropriate- `__new__`instead.
 - 
__repr__(*self*)[¶](#enum.Enum.__repr__)
- Returns the string used for - *repr()*calls. By default, returns the- *Enum*name, member name, and value, but can be overridden:- >>> from enum import auto, Enum >>> class OtherStyle(Enum): ... ALTERNATE = auto() ... OTHER = auto() ... SOMETHING_ELSE = auto() ... def __repr__(self): ... cls_name = self.__class__.__name__ ... return f'{cls_name}.{self.name}' ... >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}" (OtherStyle.ALTERNATE, 'OtherStyle.ALTERNATE', 'OtherStyle.ALTERNATE') 
 - 
__str__(*self*)[¶](#enum.Enum.__str__)
- Returns the string used for - *str()*calls. By default, returns the- *Enum*name and member name, but can be overridden:- >>> from enum import auto, Enum >>> class OtherStyle(Enum): ... ALTERNATE = auto() ... OTHER = auto() ... SOMETHING_ELSE = auto() ... def __str__(self): ... return f'{self.name}' ... >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}" (<OtherStyle.ALTERNATE: 1>, 'ALTERNATE', 'ALTERNATE') 
 - 
__format__(*self*)[¶](#enum.Enum.__format__)
- Returns the string used for - *format()*and- *f-string*calls. By default, returns- `__str__()`- >>> from enum import auto, Enum >>> class OtherStyle(Enum): ... ALTERNATE = auto() ... OTHER = auto() ... SOMETHING_ELSE = auto() ... def __format__(self, spec): ... return f'{self.name}' ... >>> OtherStyle.ALTERNATE, str(OtherStyle.ALTERNATE), f"{OtherStyle.ALTERNATE}" (<OtherStyle.ALTERNATE: 1>, 'OtherStyle.ALTERNATE', 'ALTERNATE') 
 - Note - Using - `auto`- `Enum`results in integers of increasing value, starting with- `1`.- Changed in version 3.12: Added - [Dataclass support](../howto/enum.html#enum-dataclass-support)- 
_add_alias_()[¶](#enum.Enum._add_alias_)
- Adds a new name as an alias to an existing member: - >>> Color.RED._add_alias_("ERROR") >>> Color.ERROR <Color.RED: 1> - Raises a - `NameError`- Added in version 3.13. 
 - 
_add_value_alias_()[¶](#enum.Enum._add_value_alias_)
- Adds a new value as an alias to an existing member: - >>> Color.RED._add_value_alias_(42) >>> Color(42) <Color.RED: 1> Raises a- `ValueError`See- [MultiValueEnum](../howto/enum.html#multi-value-enum)for an example.- Added in version 3.13. 
 
- 
name

- 
*class*enum.IntEnum[¶](#enum.IntEnum)
- *IntEnum*is the same as- `Enum`- *IntEnum*member, the resulting value loses its enumeration status.- >>> from enum import IntEnum >>> class Number(IntEnum): ... ONE = 1 ... TWO = 2 ... THREE = 3 ... >>> Number.THREE <Number.THREE: 3> >>> Number.ONE + Number.TWO 3 >>> Number.THREE + 5 8 >>> Number.THREE == 3 True - Note - Using - `auto`- `IntEnum`results in integers of increasing value, starting with- `1`.- Changed in version 3.11: - `__str__()`- `int.__str__()`to better support the- *replacement of existing constants*use-case.- `__format__()`- `int.__format__()`for that same reason.

- 
*class*enum.StrEnum[¶](#enum.StrEnum)
- *StrEnum*is the same as- `Enum`- *StrEnum*member is not part of the enumeration.- >>> from enum import StrEnum, auto >>> class Color(StrEnum): ... RED = 'r' ... GREEN = 'g' ... BLUE = 'b' ... UNKNOWN = auto() ... >>> Color.RED <Color.RED: 'r'> >>> Color.UNKNOWN <Color.UNKNOWN: 'unknown'> >>> str(Color.UNKNOWN) 'unknown' - Note - There are places in the stdlib that check for an exact - `str`- `str`subclass (i.e.- `type(unknown) == str`instead of- `isinstance(unknown, str)`), and in those locations you will need to use- `str(MyStrEnum.MY_MEMBER)`.- Note - Using - `auto`- `StrEnum`results in the lower-cased member name as the value.- Note - `__str__()`- `str.__str__()`to better support the- *replacement of existing constants*use-case.- `__format__()`- `str.__format__()`for that same reason.- Added in version 3.11. 

- 
*class*enum.Flag[¶](#enum.Flag)
- `Flag`is the same as- `Enum`- `&`(- *AND*),- `|`(- *OR*),- `^`(- *XOR*), and- `~`(- *INVERT*); the results of those operations are (aliases of) members of the enumeration.- 
__contains__(*self*,*value*)[¶](#enum.Flag.__contains__)
- Returns - *True*if value is in self:- >>> from enum import Flag, auto >>> class Color(Flag): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> purple = Color.RED | Color.BLUE >>> white = Color.RED | Color.GREEN | Color.BLUE >>> Color.GREEN in purple False >>> Color.GREEN in white True >>> purple in white True >>> white in purple False 
 - 
__iter__(*self*)[¶](#enum.Flag.__iter__)
- Returns all contained non-alias members: - >>> list(Color.RED) [<Color.RED: 1>] >>> list(purple) [<Color.RED: 1>, <Color.BLUE: 4>] - Added in version 3.11. 
 - 
__len__(*self*)[¶](#enum.Flag.__len__)
- Returns number of members in flag: - >>> len(Color.GREEN) 1 >>> len(white) 3 - Added in version 3.11. 
 - 
__bool__(*self*)[¶](#enum.Flag.__bool__)
- Returns - *True*if any members in flag,- *False*otherwise:- >>> bool(Color.GREEN) True >>> bool(white) True >>> black = Color(0) >>> bool(black) False 
 - 
__or__(*self*,*other*)[¶](#enum.Flag.__or__)
- Returns current flag binary or’ed with other: - >>> Color.RED | Color.GREEN <Color.RED|GREEN: 3> 
 - 
__and__(*self*,*other*)[¶](#enum.Flag.__and__)
- Returns current flag binary and’ed with other: - >>> purple & white <Color.RED|BLUE: 5> >>> purple & Color.GREEN <Color: 0> 
 - 
__xor__(*self*,*other*)[¶](#enum.Flag.__xor__)
- Returns current flag binary xor’ed with other: - >>> purple ^ white <Color.GREEN: 2> >>> purple ^ Color.GREEN <Color.RED|GREEN|BLUE: 7> 
 - 
__invert__(*self*)[¶](#enum.Flag.__invert__)
- Returns all the flags in - *type(self)*that are not in- *self*:- >>> ~white <Color: 0> >>> ~purple <Color.GREEN: 2> >>> ~Color.RED <Color.GREEN|BLUE: 6> 
 - 
_numeric_repr_()[¶](#enum.Flag._numeric_repr_)
- Function used to format any remaining unnamed numeric values. Default is the value’s repr; common choices are - `hex()`- `oct()`
 - Note - Using - `auto`- `Flag`results in integers that are powers of two, starting with- `1`.- Changed in version 3.11: The - *repr()*of zero-valued flags has changed. It is now:- >>> Color(0) <Color: 0> 
- 
__contains__(

- 
*class*enum.IntFlag[¶](#enum.IntFlag)
- `IntFlag`is the same as- `Flag`- >>> from enum import IntFlag, auto >>> class Color(IntFlag): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> Color.RED & 2 <Color: 0> >>> Color.RED | 2 <Color.RED|GREEN: 3> - If any integer operation is performed with an - *IntFlag*member, the result is not an- *IntFlag*:- >>> Color.RED + 2 3 - If a - `Flag`- *IntFlag*member and:- the result is a valid - *IntFlag*: an- *IntFlag*is returned
- the result is not a valid - *IntFlag*: the result depends on the- `FlagBoundary`
 - The - `repr()`- >>> Color(0) <Color: 0> - Note - Using - `auto`- `IntFlag`results in integers that are powers of two, starting with- `1`.- Changed in version 3.11: - `__str__()`- `int.__str__()`to better support the- *replacement of existing constants*use-case.- `__format__()`- `int.__format__()`for that same reason.- Inversion of an - `IntFlag`now returns a positive value that is the union of all flags not in the given flag, rather than a negative value. This matches the existing- `Flag`

- 
*class*enum.ReprEnum[¶](#enum.ReprEnum)
- `ReprEnum`uses the- `repr()`- `Enum`- `str()`- Inherit from - `ReprEnum`to keep the- `str()`- `format()`- `Enum`- `str()`- Added in version 3.11. 

- 
*class*enum.EnumCheck[¶](#enum.EnumCheck)
- *EnumCheck*contains the options used by the- `verify()`- `ValueError`- 
UNIQUE[¶](#enum.EnumCheck.UNIQUE)
- Ensure that each value has only one name: - >>> from enum import Enum, verify, UNIQUE >>> @verify(UNIQUE) ... class Color(Enum): ... RED = 1 ... GREEN = 2 ... BLUE = 3 ... CRIMSON = 1 Traceback (most recent call last): ... ValueError: aliases found in <enum 'Color'>: CRIMSON -> RED 
 - 
CONTINUOUS[¶](#enum.EnumCheck.CONTINUOUS)
- Ensure that there are no missing values between the lowest-valued member and the highest-valued member: - >>> from enum import Enum, verify, CONTINUOUS >>> @verify(CONTINUOUS) ... class Color(Enum): ... RED = 1 ... GREEN = 2 ... BLUE = 5 Traceback (most recent call last): ... ValueError: invalid enum 'Color': missing values 3, 4 
 - 
NAMED_FLAGS[¶](#enum.EnumCheck.NAMED_FLAGS)
- Ensure that any flag groups/masks contain only named flags – useful when values are specified instead of being generated by - `auto()`- >>> from enum import Flag, verify, NAMED_FLAGS >>> @verify(NAMED_FLAGS) ... class Color(Flag): ... RED = 1 ... GREEN = 2 ... BLUE = 4 ... WHITE = 15 ... NEON = 31 Traceback (most recent call last): ... ValueError: invalid Flag 'Color': aliases WHITE and NEON are missing combined values of 0x18 [use enum.show_flag_values(value) for details] 
 - Note - CONTINUOUS and NAMED_FLAGS are designed to work with integer-valued members. - Added in version 3.11. 
- 
UNIQUE

- 
*class*enum.FlagBoundary[¶](#enum.FlagBoundary)
- `FlagBoundary`controls how out-of-range values are handled in- `Flag`- 
STRICT[¶](#enum.FlagBoundary.STRICT)
- Out-of-range values cause a - `ValueError`- `Flag`- >>> from enum import Flag, STRICT, auto >>> class StrictFlag(Flag, boundary=STRICT): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> StrictFlag(2**2 + 2**4) Traceback (most recent call last): ... ValueError: <flag 'StrictFlag'> invalid value 20 given 0b0 10100 allowed 0b0 00111 
 - 
CONFORM[¶](#enum.FlagBoundary.CONFORM)
- Out-of-range values have invalid values removed, leaving a valid - `Flag`- >>> from enum import Flag, CONFORM, auto >>> class ConformFlag(Flag, boundary=CONFORM): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> ConformFlag(2**2 + 2**4) <ConformFlag.BLUE: 4> 
 - 
EJECT[¶](#enum.FlagBoundary.EJECT)
- Out-of-range values lose their - `Flag`- `int`- >>> from enum import Flag, EJECT, auto >>> class EjectFlag(Flag, boundary=EJECT): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> EjectFlag(2**2 + 2**4) 20 
 - 
KEEP[¶](#enum.FlagBoundary.KEEP)
- Out-of-range values are kept, and the - `Flag`- `IntFlag`- >>> from enum import Flag, KEEP, auto >>> class KeepFlag(Flag, boundary=KEEP): ... RED = auto() ... GREEN = auto() ... BLUE = auto() ... >>> KeepFlag(2**2 + 2**4) <KeepFlag.BLUE|16: 20> 
 - Added in version 3.11. 
- 
STRICT

- 
*class*enum.EnumDict[¶](#enum.EnumDict)
- *EnumDict*is a subclass of- `dict`- [Preparing the class namespace](../reference/datamodel.html#prepare)). It is exposed to allow subclasses of- `EnumType`- Note that only the - `MutableMapping`- `__setitem__()`- `update()`- `dict`operations like- `|=`- 
member_names[¶](#enum.EnumDict.member_names)
- A list of member names. 
 - Added in version 3.13. 
- 
member_names

### Supported `__dunder__` names[¶](#supported-dunder-names)

[ __members__](#enum.EnumType.__members__) is a read-only ordered mapping of 

`member_name`:`member`
items.  It is only available on the class.[ __new__()](#enum.Enum.__new__), if specified, must create and return the enum members;
it is also a very good idea to set the member’s 

[appropriately. Once all the members are created it is no longer used.](#enum.Enum._value_)

`_value_`### Supported `_sunder_` names[¶](#supported-sunder-names)

- `_name_`
- `_value_`- `__new__`
- `_missing_()`
- `_ignore_`- `list`- `str`
- `_order_`
- `_generate_next_value_()`
- `_add_alias_()`
- `_add_value_alias_()`
- While - `_sunder_`names are generally reserved for the further development of the- `Enum`- `_repr_*`(e.g.- `_repr_html_`), as used in- [IPython’s rich display](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display)
 

Added in version 3.6: `_missing_`, `_order_`, `_generate_next_value_`

Added in version 3.7: `_ignore_`

Added in version 3.13: `_add_alias_`, `_add_value_alias_`, `_repr_*`

## Utilities and decorators[¶](#utilities-and-decorators)

- 
*class*enum.auto[¶](#enum.auto)
- *auto*can be used in place of a value. If used, the- *Enum*machinery will call an- `Enum`- `_generate_next_value_()`- `Enum`and- `IntEnum`- `Flag`- `IntFlag`- `StrEnum`- *auto()*with manually specified values.- *auto*instances are only resolved when at the top level of an assignment, either by itself or as part of a tuple:- `FIRST = auto()`will work (auto() is replaced with- `1`);
- `SECOND = auto(), -2`will work (auto is replaced with- `2`, so- `2, -2`is used to create the- `SECOND`enum member;
- `THREE = [auto(), -3]`will- *not*work (- `[<auto instance>, -3]`is used to create the- `THREE`enum member)
 - Changed in version 3.11.1: In prior versions, - `auto()`had to be the only thing on the assignment line to work properly.- `_generate_next_value_`can be overridden to customize the values used by- *auto*.- Note - in 3.13 the default - `_generate_next_value_`will always return the highest member value incremented by 1, and will fail if any member is an incompatible type.

- 
@enum.property[¶](#enum.property)
- A decorator similar to the built-in - *property*, but specifically for enumerations. It allows member attributes to have the same names as members themselves.- Note - the - *property*and the member must be defined in separate classes; for example, the- *value*and- *name*attributes are defined in the- *Enum*class, and- *Enum*subclasses can define members with the names- `value`and- `name`.- Added in version 3.11. 

- 
@enum.unique[¶](#enum.unique)
- A - `class`- `__members__`- `ValueError`- >>> from enum import Enum, unique >>> @unique ... class Mistake(Enum): ... ONE = 1 ... TWO = 2 ... THREE = 3 ... FOUR = 3 ... Traceback (most recent call last): ... ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE 

- 
@enum.verify[¶](#enum.verify)
- A - `class`- `EnumCheck`- Added in version 3.11. 

- 
@enum.member[¶](#enum.member)
- A decorator for use in enums: its target will become a member. - Added in version 3.11. 

- 
@enum.nonmember[¶](#enum.nonmember)
- A decorator for use in enums: its target will not become a member. - Added in version 3.11. 

- 
@enum.global_enum[¶](#enum.global_enum)
- A decorator to change the - `str()`- `repr()`- `re.RegexFlag`- Added in version 3.11. 

- 
enum.show_flag_values(*value*)[¶](#enum.show_flag_values)
- Return a list of all power-of-two integers contained in a flag - *value*.- Added in version 3.11. 

- 
enum.bin(*num*,*max_bits=None*)[¶](#enum.bin)
- Like built-in - `bin()`, except negative values are represented in two’s complement, and the leading bit always indicates sign (- `0`implies positive,- `1`implies negative).- >>> import enum >>> enum.bin(10) '0b0 1010' >>> enum.bin(~10) # ~10 is -11 '0b1 0101' - Added in version 3.11. 

## Notes[¶](#notes)

These three enum types are designed to be drop-in replacements for existing integer- and string-based values; as such, they have extra limitations:



`__str__`uses the value and not the name of the enum member

`__format__`, because it uses`__str__`, will also use the value of the enum member instead of its nameIf you do not need/want those limitations, you can either create your own base class by mixing in the

`int`or`str`type yourself:>>> from enum import Enum >>> class MyIntEnum(int, Enum): ... passor you can reassign the appropriate

[, etc., in your enum:](stdtypes.html#str)`str()`>>> from enum import Enum, IntEnum >>> class MyIntEnum(IntEnum): ... __str__ = Enum.__str__