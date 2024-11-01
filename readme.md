# ricetypes

This is a little library that defines some nice type constructs that I like to have.

## Install

```sh
pip install ricetypes
```

### Enums (Discriminated Unions)

I have implemented something approximating rust enums.

``` python
from ricetypes import Enum, Scalar_Variant, Struct_Variant

@Enum
class Color:
    Red:   Scalar_Variant
    Blue:  Scalar_Variant
    Green: Scalar_Variant

    RGB: Struct_Variant(int, int, int, alpha=float)


r = Color.Red
b = Color.Blue
g = Color.Green


whilte = Color.RGB(100,100,100, alpha=.1)

print(white.alpha)
print(white._0, white._1, white_2)

print(white.tuple)
print(white.dict)

match r:
    case Color.Red:
        print('red')
    case Color.Blue:
        print('blue')
    case Color.Green:
        print('green')

# unfortunatly you cant use Struct_Variants in a match statment

```

### Result 

It includes the Result type:
``` python
from ricetypes import Result

r = Result.Ok(10)

from math import sqrt
r.map(sqrt).unwrap()

r = Result.Error('sad').maperr(str.upper)

if r.error:
    print(r._error)

try:
    r.with_exception(KeyError).unwrap()
except KeyError as e:
    print(e)

try:
    r.unwrap()
except Exception as e:
    print(e)

# We can chain functions together using map
inc = lambda n: n+1
Result.Ok(0).map(inc).map(inc).map(sqrt)

# And we can chain functions that return an Option together using a bind
def foo(x: int, y:int):
    if x < y:
        return Result.Ok(y)
    return Result.Error(f'y must be bigger then x but x={x}, y={y}')

Result.Ok(0).bind(foo, 10).bind(foo,30).bind(foo,20).or_else(-1)
```


### Option
``` python
from ricetypes import Option
op = Option.Some('value')

if op.something:
    print(op.value)

op.map(str.upper)

op = Option.Nothing

op.or_else('hi')

```


