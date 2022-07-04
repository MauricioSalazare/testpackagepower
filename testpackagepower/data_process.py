import pkg_resources
import pandas as pd

def load_line():
    stream = pkg_resources.resource_stream(__name__, "data/Lines_34.csv")
    return pd.read_csv(stream, encoding='latin-1')