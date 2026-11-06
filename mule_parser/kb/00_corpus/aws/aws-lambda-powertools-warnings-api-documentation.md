# aws_lambda_powertools.warnings API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/warnings/index.html](https://docs.aws.amazon.com/powertools/python/latest/api/warnings/index.html)

---

# Module `aws_lambda_powertools.warnings`

Shared warnings that don't belong to a single utility

## Classes

- `class PowertoolsDeprecationWarning (message)`
- 
## Expand source code`class PowertoolsDeprecationWarning(DeprecationWarning): """ This class provides a DeprecationWarning custom Warning for utilities/parameters deprecated in v3. Examples: - Using development-only features in production environment. - Potential performance or security issues due to misconfiguration. Parameters ---------- message: str The warning message to be displayed. """ def __init__(self, message): self.message = message super().__init__(message) def __str__(self): return self.message`This class provides a DeprecationWarning custom Warning for utilities/parameters deprecated in v3. Examples: - Using development-only features in production environment. - Potential performance or security issues due to misconfiguration. ## Parameters- `message`- `str`
- The warning message to be displayed.
 ### Ancestors- builtins.DeprecationWarning
- builtins.Warning
- builtins.Exception
- builtins.BaseException
 
- `class PowertoolsUserWarning (message)`
- 
## Expand source code`class PowertoolsUserWarning(UserWarning): """ This class provides a custom Warning tailored for better clarity when certain situations occur. Examples: - Using development-only features in production environment. - Potential performance or security issues due to misconfiguration. Parameters ---------- message: str The warning message to be displayed. """ def __init__(self, message): self.message = message super().__init__(message) def __str__(self): return self.message`This class provides a custom Warning tailored for better clarity when certain situations occur. Examples: - Using development-only features in production environment. - Potential performance or security issues due to misconfiguration. ## Parameters- `message`- `str`
- The warning message to be displayed.
 ### Ancestors- builtins.UserWarning
- builtins.Warning
- builtins.Exception
- builtins.BaseException