import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def co2_gdp_plot():
    df_climate = pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    co2 = co2.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    co2 = co2.set_index('Country code')
    co2 = co2.replace({'..':pd.np.NaN})
    co2 = co2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    co2 = co2.sum(axis=1)
    gdp = df_climate[df_climate['Series code']=='NY.GDP.MKTP.CD']
    gdp = gdp.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    gdp = gdp.set_index('Country code')
    gdp = gdp.replace({'..':pd.np.NaN})
    gdp = gdp.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    gdp = gdp.sum(axis=1)
    df = pd.concat([co2,gdp],axis=1)
    df.columns=['CO2-SUM','GDP-SUM']
    df = df.replace({pd.np.NaN:0})
    df_min_max = (df-df.min())/(df.max()-df.min())
    fig = plt.subplot()
    df_min_max.plot(kind='line',title='GDP-CO2',ax=fig)
    country_list = ['CHN','USA','GBR','FRA','RUS']
    indexs = []
    countries = []
    for i in range(len(df_min_max)):
        if df_min_max.index[i] in country_list:
            countries.append(df_min_max.index[i])
            indexs.append(i)
    plt.xticks(indexs,countries,rotation='vertical')
    plt.xlabel('Countries')
    plt.ylabel('Values')
    plt.show()
    Co2 = df_min_max.loc['CHN','CO2-SUM']
    Co2 = round(Co2,3)
    Gdp = df_min_max.loc['CHN','GDP-SUM']
    Gdp = round(Gdp,3)
    china = [Co2,Gdp]
    return fig,china
if __name__=='__main__':
    co2_gdp_plot()
