
def load_data_from_url(url):
    """Load data from a URL into a pandas DataFrame.

    Parameters
    -----------
    url : str
        The URL of the data to load.

    Returns
    -------
    df : pandas.DataFrame
        The loaded data.
    """
    import pandas as pd

    df = pd.read_csv(url)
    return df
    
