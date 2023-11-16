
## import pandas & numpy
import pandas as  pd
import numpy as np

amazon_sales = pd.read_csv("amazon_sales.csv")
amazon_sales

## info datafram
amazon_sales.info()

## NA (check missing values)
amazon_sales.isna().sum()

## How many columns, rows in this datasset
amazon_sales.shape

## Question 1: What is the best selling product?
    ## import pandas as pd
import pandas as pd

q1 =  amazon_sales.groupby(['product_id', 'product_name'])['net_price']\
        .agg(sum)\
        .reset_index()\
        .sort_values('net_price', ascending = False)\
        .head(5)    
q1

## Plot chart
# Question 1:

q1.plot.bar(x = 'product_name',\
            y = 'net_price',\
            legend = False)


## Question 2: Which category is the best-selling?
    ## import pandas as pd
import pandas as pd
q2 = amazon_sales.groupby(['category'])['net_price']\
        .agg(sum)\
        .round()\
        .reset_index()\
        .sort_values('net_price', ascending = False)\
        .head(5)
q2


## Question 3: Which products have been highly rated at 5
    ## improt pandas as pd
import pandas as pd

amazon_sales[['product_name', 'rating']]\
    [amazon_sales['rating'] == 5]


## Question 4: What is the average net price for each category in the dataset?
import numpy as np
import pandas as pd
amazon_sales.rename(columns={'net_price': 'avg_price'})\
    .groupby(['category'])['avg_price']\
    .mean()\
    .round()\
    .reset_index()\
    .sort_values('avg_price', ascending = False)


## Plot chart sample
# Question 4:
amazon_sales.groupby(['category'])['net_price']\
    .mean()\
    .round()\
    .reset_index()\
    .sort_values('net_price', ascending = False)\
    .plot.bar(x = 'category',\
              y = 'net_price',\
              legend = False)



## ML for net price

## ML
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split

## prepare data

x = amazon_sales[['actual_price','discounted_price']]
y = amazon_sales['net_price']


## split data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)


## train model
model = BaggingRegressor()
model.fit(x_train, y_train)

## prediction

p = model.predict(x_test)

# Scoring
model.score(x_test, y_test)


## Ml for discount price

## ML
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split

## prepare data

x = amazon_sales.drop(['product_id', 
                       'product_name',
                       'category',
                       'sub_category',
                       'rating_rate_count',
                       'rating_total',
                       'rating_count',
                       'discounted_price',
                       'discount_percentage'], axis=1)
y = amazon_sales['discounted_price']


## split data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42)


## train model
model = BaggingRegressor()
model.fit(x_train, y_train)

## prediction

p = model.predict(x_test)

# Scoring
model.score(x_test, y_test)
