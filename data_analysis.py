# library in python code 
import pandas as pd
from IPython.display import display
import matplotlib as plt 
from matplotlib import pyplot as plt

print("Gross domestic product by economic activity at current basic prices for the years 2002-2009 (million dinars) with population")
print("Data analysis using Python")
# Read database
Economic_df = pd.read_csv("Economic_activity_current_basic_prices_years_2002_2009 _million_dinars.csv")
print("The Financial data :") 
print(Economic_df)
df1=pd.DataFrame(Economic_df)
# Show the data 
display(df1)
print("-------------------------------------------------------")
# Show the shap of data 
print("The Shape of Financial data :")
print(Economic_df.shape)
print("-------------------------------------------------------")
# Show the maximum value in each column in dataframe  
print("Display  the maximum value in each column")
display(df1.style.highlight_max())
print("-------------------------------------------------------")
# Show the minimum value in each column in dataframe  
print("Display the minimum value in each column")
display(df1.style.highlight_min())
print("-------------------------------------------------------")
# Show the first five column in dataframe  
print("Display first five column")
print(Economic_df.head())
print("-------------------------------------------------------")
# Show the last five column column in dataframe  
print("Display last five column")
print(Economic_df.tail())
print("-------------------------------------------------------")
# Show column names 
print("Display column names")
print(Economic_df.columns)
print("-------------------------------------------------------")
# Show the average net gross national income from 2002 to 2009
print("The average net gross national income from 2002 to 2009")
revenue_mean = Economic_df['Gross national income'].mean()
print(revenue_mean)
print("-------------------------------------------------------")
# Show The number of rows
print("The number of rows")
print(Economic_df.shape[0])
print("-------------------------------------------------------")
# Show The number of columns
print("The number of columns")
print(Economic_df.shape[1])
print("-------------------------------------------------------")

# Function check if there is a Miss value or null in datafram
def checkmissvalue():
  print("Checking if there is Any missing value :")
  test=Economic_df.isnull().values.any()
  if test==True:
           print("There is a missing value")
  else:
           print("There is no misssing value")
print("-------------------------------------------------------")

# The length of dataframe
print("The length of dataframe :")
print(len(Economic_df))
print("-------------------------------------------------------")

# database summary
print("The summary of dataframe :")
print((Economic_df.describe(include='all')))


# Show the maximum value in each column in dataframe  
print("Display  the maximum value in each column")
display(df1.style.highlight_max())

# Show the minimum value in each column in dataframe  
print("Display the minimum value in each column")
display(df1.style.highlight_min())

def bar_chart1():
    Year = Economic_df["Year"]
    values = Economic_df["number of population"]
    fig = plt.figure(figsize = (10, 5))

    plt.bar(Year, values)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("population (Million)")
    plt.title("A study of the relationship between population numbers with progress in years in Jordan")  
bar_chart1()
print("-----------------------------------")
print("According to what is apparent in the figure, it is a direct relationship between the average population in Jordan, which is increasing, that is, the direct relationship between population numbers and years.")
print("-----------------------------------")

def bar_chart2():
    Year = Economic_df["Year"]
    Agriculture = Economic_df["Agriculture, hunting, forestry and fishing"]
    fig = plt.figure(figsize = (10, 5) )
    plt.bar(Year, Agriculture)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("production rate of  Agriculture, hunting, forestry and fishing")
    plt.title("A study of the relationship between production rate of [Agriculture, hunting, forestry and fishing]  with progress in years in Jordan")
    plt.plot(color="r")
bar_chart2()  
print("---------------------------------")
print("According to what is apparent in the figure, it is a direct relationship between the rate of agricultural production in Jordan with the number of years, which leads to an increase in productivity over the years.")
print("---------------------------------")

print(" Show the relationship between the population number in Jordan and the average national income during 9 years ")
chart_data = pd.DataFrame(
        Economic_df,columns=['number of population', 'Gross national income'])
plt.xlabel("number of population in Million")
plt.ylabel("Gross national income")
plt.title("A study of the relationship between number of population and Gross national income during 9 years  ")
plt.plot(chart_data)
print("direct relationship")

print("-------------------------------------------------------")
print("Programming Challenge -- >> Community number 53")
print("-------------------------------------------------------")
# team summary
print("The team Info : ")
print("1. Shahed Al-khateeb ")
print("2. Rawan Abu Lali")
print("3. Raged Al-khateeb ")
print("4. Waed Al-khateeb ")


