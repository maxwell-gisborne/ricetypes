# nicetypes

_warnning: I wrote this markdown document directly and have not actlualy run the code examples, so there may be typeos, but the underlying features do work_

This is a little library that defines some nice type constructs that I like to have.


### Result 

It includes the Result type:
``` python
from nicetypes import Result

r = Result.Ok(10):

from math import sqrt
r.map(sqrt).unwrap()

r = Result.Error('sad').maperr(string.upper)

if r.error:
    print(r._error)

try:
    r.with_exception(KeyError).unwrap()
excpect KeyError as e:
    print(e)

try:
    r.unwrap()
excpect Exception as e:
    print(e)

# We can chain functions together using map
inc = lambda n: n+1
Result.Ok(0).map(inc).map(inc).map(sqrt)

# And we can chain functions that return an Option together using a bind
def foo(x: int, y:int):
    if x < y:
        return Result.Some(y)
    return Result.Error(f'y must be bigger then x but x={x}, y={y}')

Result.Ok(0).bind(foo, 10).bind(foo,30).bind(foo,20).or_else(-1)
```


### Option
``` python
from nicetypes import Option
op = Option.Some('value')

if op.something:
    print(op.value)

op.map(str.upper)

op = Option.Nothing

op.or_else('hi')

```


### Enums (Descriminated Unions)

I have implemented a something approximating rust enums.

``` python
from nicetypes import Enum, Scailar_Variant, Struct_Variant

@Enum
class Color:
    Red:   Scailar_Variant
    Blue:  Scailar_Variant
    Green: Scailar_Variant

    RGB: Struct_Variant(int, int int)


r = Color.Red
b = Color.Blue
g = Color.Green


whilte = Color.RGB(100,100,100)


match r:
    case Color.Red:
        print('red')
    case Color.Blue:
        print('blue')
    case Color.Green:
        print('green')

# unfortunatly you cant use Struct_Variants in a match statment

```
