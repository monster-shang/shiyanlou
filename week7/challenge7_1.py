import pandas as pd
def co2():
    data = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    data  = data[data['Series code']=='EN.ATM.CO2E.KT']
    data = data.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data = data.set_index('Country code')
    data = data.replace({'..':pd.np.NaN})
    data = data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    data = data.dropna(how='all')
    data['Sum emissions'] = data.sum(axis=1)
    data_sum = data['Sum emissions']
    country = pd.read_excel('ClimateChange.xlsx',sheetname='Country')
    country = country.drop(['Capital city','Region','Lending category'],axis=1)
    country = country.set_index('Country code')
    df = pd.concat([data_sum,country],axis=1)
    df_sum = df.groupby('Income group').sum()
    high_country = df.sort_values(by='Sum emissions', ascending=False).groupby('Income group').head(1).set_index('Income group')['Country name']
    high_emissions = df.sort_values(by='Sum emissions', ascending=False).groupby('Income group').head(1).set_index('Income group')['Sum emissions']
    low_country = df.sort_values(by='Sum emissions', ascending=True).groupby('Income group').head(1).set_index('Income group')['Country name']
    low_emissions = df.sort_values(by='Sum emissions', ascending=True).groupby('Income group').head(1).set_index('Income group')['Sum emissions']
    dataframe = pd.concat([df_sum,high_country,high_emissions,low_country,low_emissions],axis=1)
    dataframe.columns=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    return dataframe

