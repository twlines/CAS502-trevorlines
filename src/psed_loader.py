import json
import pandas as pd
import numpy as np

def load_codebook(json_path):
    """Load codebook JSON file and return it as a dictionary"""
    with open(json_path, 'r') as file:
        return json.load(file)

def load_raw(tsv_path):
    """Load TSV file into a pandas DataFrame.
    
    PSED data from ICPSR comes as tab-separated values (TSV)
    the integer codes require decoding via the codebook
    """
    return pd.read_csv(tsv_path, sep='\t')

def decode_categorical(df, column, codebook_entry):
    """Map codes in a column to their string labels from codebook
    
    Example: AA4 column values 1, 5, 8, become "Yes", "No", "Don't Know"
    """
    # Builds categorical data in dataframe by converting their numerical codes to coresponding codebook labels
    # Converts codebook keys from strings to integers (JSON stores keys as strings)
    codes = codebook_entry['codes']
    mapping = {int(key): value for key, value in codes.items()}
    df[column] = df[column].map(mapping)
    return df

def clean_continuous(df, column, sentinels):
    """Replace sentinel values with NaN in a continuous variable.
    
    PSED uses special numerical codes (98 = "Don't Know" and "99 = "Refused") 
    if we don't replace these values with NaN, we corrupt our calculations"""
    df[column] = df[column].replace(sentinels, np.nan)
    return df
