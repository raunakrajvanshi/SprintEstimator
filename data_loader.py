import pandas as pd

def load_data(json_file='historical_sprint_data.json'):
    data = pd.read_json(json_file)
    return data
