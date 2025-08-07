# Virtual Column Generator – Recruitment Task

This project contains a Python function `add_virtual_column()` designed to extend a `pandas.DataFrame` by adding a new virtual column based on a string expression. The function performs strict input validation and safe evaluation of arithmetic expressions using existing DataFrame columns.

>  This implementation was completed as part of a technical recruitment assignment.

---

##  Problem Statement

Create a function:

```python
def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame
