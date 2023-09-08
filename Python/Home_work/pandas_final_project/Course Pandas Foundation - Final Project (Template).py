# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 30 December 2021
# 
# **Author**: Kasidis Satangmongkol (Toy DataRockie)
# 
# **Course**: `Pandas Foundation`


from pandas import DataFrame
# import data
import pandas as pd
df  = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
import pandas as pd
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df[['Order Date', 'Ship Date']].head()

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# count country
df['Segment'].unique()

# TODO - Explore this dataset on your owns, ask your own questions
    
    # Which segment is higher sale?
import pandas as pd
my1_question = df.groupby(['Segment', 'Category', 'Sub-Category'])['Sales']\
    .sum().reset_index()\
    .sort_values('Sales', ascending = False)\
    .head(1)
print("Question 1")
print(my1_question)
print("-------------------------------------------------------------")
print(f"""The higher sales segment is Consumer. 
Category is Furniture that it is Chairs can sales $ 172862.742""")
print("--------------------------------------------------------------")

    # Which product can make the most profit (top 3)
my2_question = df.groupby(['Segment', 'Category', 'Sub-Category'])['Profit']\
    .sum().reset_index()\
    .sort_values('Profit', ascending = False)\
    .head(3)
print("Question 2")
print(my2_question)
print(f"""The higher profitable is Copiers. It can make a profit $ 24083.71.
Following phones, $ 23837.11 and Accessories, $ 20735.92.
""")
print("--------------------------------------------------------------------")

    # What is the top 5 Sub-Category by Quantity
my3_question = df.groupby(['State', 'City', 'Sub-Category'])['Quantity']\
    .agg('sum','count').reset_index()\
    .sort_values('Quantity', ascending = False)\
    .head(5)
print("Question 3")
print(my3_question)
print(f"""
New York city is the first and second sub-category is Binders at 562 quantity, 
and Paper at 464 quantity. Following by California, Paper at 454 quantity and 
Binders at 360 quantity. The last one is Washington, sub-category is Binders 
at 329 quantity.
""")

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.shape

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
df.isna().sum().sort_values(ascending= False)

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
df_cali = df.query('State == "California"').dropna()
df_cali.to_csv('df_cali.csv')

df_cali

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
df_order_cali_tex = df[((df['State'] == 'California') | (df['State'] == 'Texas')) & (df['Order Date'].dt.strftime('%Y') == '2017')]
df_order_cali_tex.to_csv("df_order_cali_tex.csv")

df_order_cali_tex

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df[df['Order Date'].dt.strftime('%Y') == '2017']['Sales']\
    .agg(['sum','average', 'std'])\
    .round()




# TODO 06 - which Segment has the highest profit in 2018
df_2018 = df[df['Order Date'].dt.year == 2018]

df_2018.groupby(['Segment', 'Category', 'Sub-Category', 'Order Date'])['Profit']\
    .sum().reset_index()\
    .sort_values('Profit', ascending = False)\
    .round()\
    .head(3)

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df[(df['Order Date'] > '2019-04-15') & (df['Order Date'] < '2019-12-31')]\
    .groupby(['State'])['Sales']\
    .agg('sum')\
    .reset_index()\
    .sort_values('Sales', ascending = True)\
    .head(5)\
    .round()

# TODO 08 - what is the proportion of total sales (%) in West + Central('Region') in 2019 e.g. 25% 
import pandas as pd
    # sum total sales
total_sales_2019  = df[df['Order Date'].dt.strftime('%Y') == '2019']['Sales'].sum().round()

    # sum total sales of West and Central
total_west_central_sales = df[((df['Region'] == 'West') | (df['Region'] == 'Central'))\
    & (df['Order Date'].dt.strftime('%Y') == '2019')]['Sales']\
    .sum()\
    .round()

    # the proportion of total sales(%)
per_sale_wc = (total_west_central_sales / total_sales_2019) * 100

print(f"The proportion of total sales (%) in West and Central in 2019 is {per_sale_wc.round()}")

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
import pandas as pd
df_19_20 = df[df['Order Date'].dt.year.isin([2019, 2020])]


top10_product_19_20 = df_19_20.groupby(['Product Name'])['Order ID']\
    .agg('count')\
    .reset_index()\
    .sort_values('Order ID', ascending = False)\
    .head(10)

print(f"The top 10 popular products during in 2019-2020 is\n {top10_product_19_20}")



# TODO 10 - plot at least 2 plots, any plot you think interesting :)

    # [1] Which Segment is the higher sales during Year 2019 - 2020

df_19_20.groupby(['Segment'])['Sales']\
    .agg('sum')\
    .round()\
    .plot(kind = 'bar',\
          x = 'Segment',\
          y = 'Total Sales',\
          color = ['salmon', 'orange', 'yellow']);

# TODO 10 - plot at least 2 plots, any plot you think interesting :)

    #

    # unique Year
#df['Order Date'].dt.year.unique()

    #filter year 2020
df_2020 = df[df['Order Date'].dt.year.isin([2020])]

    # Top 10 City Orders by Product names
df_2020.groupby(['Region'])['Sales']\
    .sum()\
    .round()\
    .reset_index()\
    .sort_values('Sales', ascending = False)\
    .plot(kind = 'bar',\
          x = 'Region',\
          y = 'Sales',\
          color = ['pink', 'orange', 'gold', 'yellow']);

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
import pandas as pd
import numpy as np

# find mean of Quantity
avg_quantity = df_2020['Quantity'].mean().round()
print(f'The mean of Quantity is {avg_quantity}')

# if quantity <= 4 , Restock, Remain

import numpy as np

quan_restock = df_2020.groupby(['Category','Sub-Category', 'Quantity'])['Profit']\
    .sum()\
    .round()\
    .reset_index()\
    .sort_values('Profit', ascending = False)


quan_restock['Restock'] = np.where(quan_restock["Quantity"] <= 4, "Yes", "No")

# count yes no

count_yn = quan_restock['Restock'].value_counts().reset_index()


print(f'The question is Should we need to restock the product by using quantity.')
print(f'The mean of Quantity is {avg_quantity}, If quantity is <= 4, it should be restock, else is should be remain')
print("----------------------------------------------------------------------------------------------------")
print(quan_restock)
print("----------------------------------------------------------------------------------------------------")
print(f"""
In column 'Restock', the number of product that should be restock is 68 
and product that should remain is 110.\n 
{count_yn}
""")

