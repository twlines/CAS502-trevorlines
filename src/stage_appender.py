"""
Appends df with wave at which ventures reach each stage. 

Primary output: find_first_transitions() - identifies the wave at which each
respondent first reached Launched, Sustainable, and Scalable stages and appends it to the df.
"""

import pandas as pd
from success_classifier import (
    _has_valid_value,
    STAGE_SCALABLE,
    STAGE_SUSTAINABLE,
    STAGE_LAUNCHED,
    STAGE_OTHER
)

WAVES = ['A', 'B', 'C', 'D', 'E', 'F']

def _classify_wave(row, prefix):
    """Classify single respondents stage for a given wave."""
    column_revenue = f"{prefix}E13"
    column_profitable = f"{prefix}E15"
    column_salary = f"{prefix}E17"
    column_employees = f"{prefix}G3"

    is_sustainable = (_has_valid_value(row[column_profitable], ["Yes"]) and _has_valid_value(row[column_salary], ["Yes"]))

    if is_sustainable and _has_valid_value(row[column_employees], ["Yes"]):
        return STAGE_SCALABLE
    if is_sustainable:
        return STAGE_SUSTAINABLE
    if _has_valid_value(row[column_revenue], ["Yes"]):
        return STAGE_LAUNCHED
    return STAGE_OTHER

def find_first_transitions(df):
    """
    Find the wave of each respondents stage transition.

    Returns DF with columns: 
        first_launched, first_sustainable, first_scalable
    Values are wave letters A - F or None if never reached.""" 

    #first classify all the waves.
    for wave in WAVES:
        column_name = f"venture_stage_{wave}"
        df[column_name] = df.apply(lambda row: _classify_wave(row, wave), axis=1)

    #then define which stage counts as a milestone
    launched_stages = {STAGE_LAUNCHED, STAGE_SUSTAINABLE, STAGE_SCALABLE}
    sustainable_stages = {STAGE_SUSTAINABLE, STAGE_SCALABLE}
    scalable_stages = {STAGE_SCALABLE}

    #helper function that users whatever set we pass
    def find_first(row, target_stages):
        for wave in WAVES: 
            if row[f"venture_stage_{wave}"] in target_stages:
                return wave
        return None

    #Then call the helper with each set
    df['fist_launched'] = df.apply(lambda row: find_first(row, launched_stages), axis=1)
    df['find_sustainable'] = df.apply(lambda row: find_first(row, sustainable_stages), axis=1)
    df['find_scalable'] = df.apply(lambda row: find_first(row, scalable_stages), axis=1)

    return df
