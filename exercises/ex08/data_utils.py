"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Produces a list of values for a single column when given column name."""
    result: list[str] = []
    for row in table:
        item: str = row[column_name]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table from a list of rows to a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """A function that produces a new table with only the first N data selected for each column."""
    result: dict[str, list[str]] = {}
    for columns in table:
        if len(table[columns]) < number_rows:
            return table
        first_n_values: list[str] = []
        i: int = 0 
        while i < number_rows:
            first_n_values.append(table[columns][i])
            i += 1
        result[columns] = first_n_values
    return result
        

def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """A function that produces a column-based table w/ only a select group of orig. columns."""
    result: dict[str, list[str]] = {}
    for names in column_names:
        if names in table:
            result[names] = table[names]
    return result


def concat(a_dict: dict[str, list[str]], b_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """A function that produces a new table that combines two other tables."""
    result: dict[str, list[str]] = {}
    for columns in a_dict:
        result[columns] = a_dict[columns]
    for columns in b_dict:
        if columns in result:
            result[columns] += b_dict[columns]
        else:
            result[columns] = b_dict[columns]
    return result


def concat_2(a_dict: dict[str, int], b_dict: dict[str, int]) -> dict[str, int]:
    """A function that produces a new table that combines two other tables."""
    result: dict[str, int] = {}
    for values in a_dict:
        result[values] = a_dict[values]
    for values in b_dict:
        if values in result:
            result[values] += b_dict[values]
        else:
            result[values] = b_dict[values]
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """A function that provides a count of values from given list."""
    result: dict[str, int] = {}
    for item in a_list:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result


def high_exp(col: list[str], wanted_data: str) -> list[bool]:
    """A function that creates a mask for prior_exp col that is 1-2 years, or Over 2 years."""
    result: list[bool] = []
    for item in col:
        result.append(item == wanted_data)
    return result


def masked(col: list[str], mask: list[bool]) -> list[str]:
    """A function that takes a mask and returns values that are in the mask but associated with a decided column."""
    result: list[str] = []
    for i in range(len(mask)):
        if mask[i]:
            result.append(col[i])
    return result


# create a count function that has a dictionary with 1, 2 - 7 already established, check to see if the rating is 1 - 7, then add the count to it
def organize_count(a_dict: dict[str, int]) -> dict[str, int]:
    """A function that organizes a dictionary count into numerical order."""
    result: dict[str, int] = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0}
    for rating in a_dict:
        if rating in result:
            result[rating] += a_dict[rating]
        else:
            result[rating] = a_dict[rating]
    return result
