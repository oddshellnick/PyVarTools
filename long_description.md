# PyVarTools: A Python Library for variables

PyVarTools is a Python library providing a comprehensive suite of tools designed to streamline various tasks related to variable manipulation, inspection, and formatting. From simplifying complex formatting operations to providing utilities for introspection and date manipulation, PyVarTools aims to boost your productivity and enhance code clarity.

## Key Features

*   **Formatting:** Effortlessly format numbers, data structures, and more with flexible options for customization. Create visually appealing representations of complex data, making it easier to understand and analyze.
*   **Data Handling:** Manipulate and work with data structures effectively. Utilities are provided for common tasks like generating date ranges, managing collections, and performing data validation.
*   **Python Introspection:** Gain deeper insights into your code with tools for inspecting functions, classes, and other Python objects. Retrieve parameters, fields, and other metadata to understand the structure and behavior of your code.
*   **Variable Utilities:** Access a collection of helpful functions for various variable-related operations, such as type checking, value comparisons, and data transformations. PyVarTools handles many common variable-related tasks efficiently.

## Installation

* **With pip:**
    ```bash
    pip install PyVarTools
    ```

* **With git:**
    ```bash
    pip install git+https://github.com/oddshellnick/PyVarTools.git
    ```

## Usage Examples

The following examples illustrate a small subset of PyVarTools’ capabilities. Refer to the detailed documentation for more comprehensive examples and usage instructions.

**Formatting pandas.DataFrame:**

```python
# Formatting
from PyVarTools.format_tools import format_data_frame
import pandas as pd

df = pd.DataFrame({'A': [1, 2.5, 3], 'B': [4, 5, 6]})
formatted_df = format_data_frame(df)
print(formatted_df)
```

**Yielding datetime in range:**

```python
# Date Manipulation
from datetime import datetime, timedelta
from PyVarTools.var_utilities import date_range

start = datetime(2024, 1, 1)
end = datetime(2024, 1, 5)
delta = timedelta(days=1)

for date in date_range(start, end, delta):
    print(date)
```

This overview provides a glimpse of PyVarTools’ functionality. Explore the full documentation to uncover the full potential of this versatile library.

## Future Notes

PyVarTools is actively maintained and will continue to evolve with the addition of new utilities and enhancements to existing features. Community contributions and suggestions are highly encouraged. Please feel free to report any issues, propose new features, or submit pull requests.