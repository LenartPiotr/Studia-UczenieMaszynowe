import pandas as pd

def readData(filePath):
    """
    Read rada from CSV file and saves into DataFrame.

    Args:
    filePath (str): Path to CSV file.

    Returns:
    pandas.DataFrame: DataFrame object contains data.
    """
    return pd.read_csv(filePath, delimiter=',')