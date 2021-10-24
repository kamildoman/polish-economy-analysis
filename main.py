#the program analyzes changes in Polish economy for years 1990 - 2020. The data was downloaded from world's bank website
#generated plots are in the catalog "plots"

import pandas as pd


data = pd.read_csv("worldbankdata.csv")

indicators_wanted = [data.loc[data["Indicator Name"] == "Age dependency ratio (% of working-age population)"],
        data.loc[data["Indicator Name"] == "Exports of goods and services (% of GDP)"],
        data.loc[data["Indicator Name"] == "GDP per capita (current LCU)"],
        data.loc[data["Indicator Name"] == "Life expectancy at birth. male (years)"],
        data.loc[data["Indicator Name"] == "Inflation. GDP deflator: linked series (annual %)"]]

df_indicators = pd.concat(indicators_wanted)
#creating desired dataframe for 5 indicators for years 1990-2020
df = df_indicators[[str(years) for years in range(1990, 2021)]]
df.insert(loc = 0, column = "Indicator Name", value = df_indicators["Indicator Name"])

df = df.transpose()

#indicator names as index
df.index.astype(str)
header = df.iloc[0]
df = df[1:]
df.columns = header

df=df.astype(float)

#conclusions:

for row in df.columns:
    #some data is incomplete. I find the first and the last year with data for each column
    year_start = ""
    year_stop = ""
    for i in range(1990, 2020):
        if str(df[row][str(i)]) != 'nan':
            year_start = i
            break
    for i in range(1990, 2020):
        if str(df[row][str(i)]) != 'nan':
            year_stop = i

    value_first = df[row][str(year_start)]
    value_second = df[row][str(year_stop)]
    print(f"{row}: \nAverage: {df[row].mean()}\nIn {year_start}: {value_first}\nIn {year_stop}: {value_second}")
    percent_change = round((value_second - value_first) * 100 / value_first, 2)
    print(f"The change is {percent_change}%\n\n")
    


#plots:

# df4["Age dependency ratio (% of working-age population)"].plot()
# df4["Exports of goods and services (% of GDP)"].plot()
# df4["GDP per capita (current LCU)"].plot()
# df4["Life expectancy at birth. male (years)"].plot()
# df4["Inflation. GDP deflator: linked series (annual %)"].plot()
