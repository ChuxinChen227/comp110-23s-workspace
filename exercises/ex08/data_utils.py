"""EX08: Data Wrangling."""

__author__ = "730564297"

from csv import DictReader
from typing import TextIO

DATA_FILE_PATH: str = "../../data/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle: TextIO = open(filename, "r", encoding="utf8")
    csv_reader: DictReader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], col: str) -> list[str]:
    """Produce a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        result.append(row[col])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], nbr: int) -> dict[str, list[str]]:
    """Return a new table with only the first `n` rows for each column."""
    result: dict[str, list[str]] = {}
    for col_name in table.keys():
        col_data: list[str] = []
        for row in table[col_name]:
            if len(col_data) < nbr:
                col_data.append(row)
        result[col_name] = col_data
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for col_name in columns:
        col_data: str = table[col_name]
        result[col_name] = col_data
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] += table2[column]
        else:
            result[column] = table2[column]
    return result


def count(items: list[str]) -> dict[str, int]:
    """Count how many times a certain value appears in the input list."""
    result: dict[str, int] = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
