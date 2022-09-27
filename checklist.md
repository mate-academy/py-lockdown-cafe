# Сheck Your Code Against the Following Points

## Code Efficiency

Don't compare a variable to `0` if there is no need:

Good example:

```python
if number_of_students:
    pass
```

Bad example:

```python
if number_of_students != 0:
    pass
```

## Code Style

1. Use one style of quotes in your code. Double quotes are preferable.
2. Use `( )` while importing multiple classes/modules:

Good example:

```python
from app.main import (
    KnightWithArmour,
    KnightWithoutArmour,
    SuperHeroKnightWithGun
)
```

Bad example:

```python
from app.main import KnightWithArmour, \
    KnightWithoutArmour, \
    SuperHeroKnightWithGun
```

3. Use descriptive error messages:

Good example:

```python
if error:
    raise CustomError("We have an error on the line 16.")
```

Bad examples:

```python
if error:
    raise CustomError
```

```python
if error:
    raise CustomError("CustomError")
```

4. Avoid using unnecessary `else`:

Good example:

```python
def go_to_cinema(condition: bool) -> str:
    if condition:
        return "We are going to the cinema!"
    return "We are not going to the cinema("
```

Bad example:

```python
def go_to_cinema(condition: bool) -> str:
    if condition:
        return "We are going to the cinema!"
    else:
        return "We are not going to the cinema("
```

5. Use annotation, it is a good practice:

Good example:

```python
def multiply_by_2(number: int) -> int:
    return number * 2
```

Bad example:

```python
def multiply_by_2(number):
    return number * 2
```

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
