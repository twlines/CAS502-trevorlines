import pandas as pd

# Stage constants
STAGE_SCALABLE = "Scalable"
STAGE_SUSTAINABLE = "Sustainable"
STAGE_LAUNCHED = "Launched"
STAGE_OTHER = "other"

def _has_valid_value(value, valid_values):
    """Check if value is valid (not NaN) and in valid_values (e.g., 'Yes')"""
    if pd.isna(value):
        return False
    return value in valid_values

def _is_launched(row):
    """Check if respondent has first revenue"""
    return _has_valid_value(row['AE13'], ["Yes"])

def _is_sustainable(row):
    """Check if respondent is paying self a salary and profitable"""
    return _has_valid_value(row['AE15'], ["Yes"]) and _has_valid_value(row['AE17'], ["Yes"])

def _is_scalable(row):
    """Check if respondent is profitable, has employees, and paying self-salary"""
    return _is_sustainable(row) and _has_valid_value(row['AG3'], ["Yes"])

def _classify_row(row):
    """Classify single respondent's stage."""
    if _is_scalable(row):
        return STAGE_SCALABLE
    if _is_sustainable(row):
        return STAGE_SUSTAINABLE
    if _is_launched(row):
        return STAGE_LAUNCHED
     
    return STAGE_OTHER

def classify_success_stage(df):
    """Classify venture stage for all respondents in DF."""
    df['venture_stage'] = df.apply(_classify_row, axis=1)
    return df
