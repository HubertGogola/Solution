import pandas as pd
import re

def is_valid_column_name(name: str) -> bool:
    return re.fullmatch(r'[a-zA-Z_]+', name) is not None

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not is_valid_column_name(new_column):
        return df.iloc[0:0]

    role = role.strip()

    if not re.fullmatch(r'[a-zA-Z0-9_+\-*/\s]+', role):
        return df.iloc[0:0]

    tokens = re.findall(r'[a-zA-Z_]+', role)
    for token in tokens:
        if token not in df.columns:
            return df.iloc[0:0]

    try:
        df[new_column] = df.eval(role)
        return df
    except:
        return df.iloc[0:0]
