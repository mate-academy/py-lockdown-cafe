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

5. Use annotation, it is a good practice. Specify the expected argument instances in type annotations for clarity:

Good example:

```python
def multiply_by_2(number: int, cars: list[Car]) -> int:
    return number * 2
```

Bad example:

```python
def multiply_by_2(number, cars: list):
    return number * 2
```

6. Ensure each file ends with a single blank line.

7. Add a blank line between different groups of imports and ensure appropriate ordering of imports.
    
 Imports should be grouped in the following order:

    1.Standard library imports.
    2.Related third party imports.
    3.Local application/library specific imports.

 Good example

```python
import datetime

from app.errors import NotVaccinatedError
```

Bad example:

```python
from app.errors import NotVaccinatedError
import datetime
```

8. Use absolute imports instead of relative imports 
  
Good example:


```python
from app.errors import NotVaccinatedError
```

Bad example:

```python
from .errors import NotVaccinatedError
```
## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
