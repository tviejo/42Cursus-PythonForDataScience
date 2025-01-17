import pandas

def load(path: str) -> pandas.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    DataSet = pandas.read_csv(path)
    print ("Loading dataset of dimensions: ", DataSet.shape)
    return DataSet