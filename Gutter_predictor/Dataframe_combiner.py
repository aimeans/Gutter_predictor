import pandas as pd
Square_footage = pd.read_csv("Square_ft_random.csv")
Color_chart = pd.read_csv("Color_chart.csv")
Gutter_style = pd.read_csv("Gutter_type.csv")


Square_footage.rename(columns = {'Unnamed: 0':'Date'}, inplace = True)
Color_chart.rename(columns = {'Unnamed: 0':'Date'}, inplace = True)
Gutter_style.rename(columns = {'Unnamed: 0':'Date'}, inplace = True)




Square_footage.set_index('Date',inplace=True)
Color_chart.set_index('Date',inplace=True)
Gutter_style.set_index('Date',inplace=True)


df = Square_footage.merge(Color_chart,on='Date').merge(Gutter_style,on='Date')

df.to_csv('Merged_data.csv')


