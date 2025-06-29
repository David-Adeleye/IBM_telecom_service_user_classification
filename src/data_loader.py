"""
This module contains functions for loading telecom user data from a URL.
"""

import pandas as pd

def load_data_from_url(url):
    """Load data from a URL into a pandas DataFrame.

    Parameters
    ----------
    url : str
        The URL of the data to load.

    Returns
    -------
    pandas.DataFrame
        The loaded data.
    """
    df = pd.read_csv(url)
    return df
