import pandas as pd
import numpy as np
import re

def get_values_unique_in_column(df : pd.DataFrame, col):
    """
    Get unique values in a column of a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to query.
        col (str): The column name to get unique values from.
    
    Returns:
        list: A list of unique values in the specified column.
    """
    return df[col].unique().tolist()

def search_value_in_column(df : pd.DataFrame, col_name : str, value_search: str):
    """

    Args:
        df (pd.DataFrame): dataset revit API
        col_name (str): name column in dataframe
        value_search (str): values need search

    Returns:
        list: A list of elements have value contains value need search.
    """
    category_column = [col for col in df.columns if col_name.lower() in col.lower()]
    walls = [wall for wall in df[category_column[0]] if value_search.lower() in wall.lower()]
    return walls