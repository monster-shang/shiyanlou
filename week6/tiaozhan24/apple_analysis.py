import pandas as pd
def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    data.index = pd.to_datetime(data['Date'])
    date = data.drop('Date',axis=1)
    date = date.resample('Q').sum()
    date = date.sort_values(by = 'Volume',ascending=False)
    second_volume = date.iloc[1].Volume
    return second_volume
