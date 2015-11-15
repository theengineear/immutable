# The Immutable Package

This package presents access to an `Immutable` object which adheres to the
Python Mapping and Sequence APIs. That is, function calls like `.items()`,
`.count()`, `.index()`, `.keys()`, etc will work.

It allows you to instantiate via a `tuple` or via `kwargs`. It simplifies the
case where you know ahead of time what the values of an `Immutable` should be
and you just need to instantiate it once.

It also allows for nested objects and Immutable object comparisons. It should
be noted that you *can* change these objects by accessing the `.__dict__` attr,
accessing the `self.__dict__['_ordered_dict']` object. The idea is that there
are enough red flags at that point to steer anyone away.

## Install

`pip install immutable`

## Details

### `Immutable`

This is the main class in the package. You can use it like this:

```
from immutable import Immutable

# This results in an unordered object.
imm = Immutable(zero=0, one=1, two=2, three=3)

# This results in an ordered object.
imm = Immutable(('zero', 0), ('one', 1), ('two', 2), ('three', 3))

# You can access like a Sequence with indices.
two = imm[2]

# You can also access via the '.' operator.
three = imm.three

# Iterating works as you'd expect.
for value in imm.values():
    print value

# Trying to set an attribute via the '.' operator will fail.
imm.two = 3  # ImmutableError

# Trying to set an attribute via the `[]` operator will fail.
imm[2] = 3  # ImmutableError

# Instantiating with a mutable will fail (which is desirable).
imm = Immutable(mutable=[1, 2, 3])  # Immutable Error

# You can nest Immutable objects too (which gets around using dicts).
imm = Immutable(
    key = 'something',
    sub_imm = Immutable(
        sub_key = (1, 2, 3)
    )
)
```
