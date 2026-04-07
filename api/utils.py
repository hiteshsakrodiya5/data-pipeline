import pandas as pd

def transform(data):
    df = pd.DataFrame(data)

    df.dropna(inplace=True)
    df.columns = [col.lower() for col in df.columns]

    return df.to_dict(orient='records')