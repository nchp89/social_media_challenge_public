import pandas as pd
import numpy as np


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    

def drop_identifiers(df):
    ''' 
    function to remove undesirable columns from SMC dataframe
    
    input: dataframe
    return: dataframe
    '''
    drop_cols = [
        'First Name',
        'Last Name',
        'Email Address',
        'DEMO_academic_year',
        'DEMO_grad_year',
        'DEMO_major',
        'DEMO_gender',
        'DEMO_ethnicity',
        'DEMO_smartphone'
    ]
    unnamed_cols = [c for c in df.columns if c.startswith('Unnamed')]
    
    for col in drop_cols + unnamed_cols:
        try:
            df = df.drop(col, axis=1)
        except:
            # if column is missing, pass silently
            continue
    return df

