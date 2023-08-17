## load library
library(tidyverse)
library(readxl)
library(caret)
library(ggplot2)

## import .xlsx 

HPI <- read_excel("House Price India.xlsx")

## Check NA

HPI %>%
  complete.cases() %>%
  mean()



## Visualization predict variable price before prepare data

plot_1 <- ggplot(HPI, aes(Price)) +
  geom_density() +
  theme_minimal() +
  labs(
    title = "House Price India Distribution",
    x = "Price",
    y = "Count",
    caption = "Source: Dataset House Price India from data.world"
  )

cor(HPI$`Number of schools nearby`,HPI$Price)

plot_1

## select parameter

hpi_data <- HPI %>% 
  select( price = Price,
          distance_airport = `Distance from the airport`,
          no_bedrooms = `number of bedrooms`,
          no_bathrooms = `number of bathrooms`,
          no_schools = `Number of schools nearby`,
          living_area = `living area`)

  
## Visualization after log_Price 
  
plot_2 <- ggplot(HPI, aes(log(Price))) +
    geom_density() +
    theme_minimal() +
    labs(
      title = "House Price India Distribution",
      x = "Price",
      y = "Count",
      caption = "Source: Dataset House Price India from data.world"
    )
  
plot_2
  

## normal distribution by take log_price
hpi_log <- hpi_data
hpi_log$price <- hpi_data$price %>%
  log()


## 1. train test split 
## create function

split_data <- function(HPI, train_size = 0.8) {
  set.seed(24)
  n <- nrow(hpi_data)
  id <- sample(1:n, size = n * train_size)
  train_data <- hpi_data[id,]
  test_data <- hpi_data[-id,]
  list(train = train_data, 
       test = test_data)
}

  ## prep data 

prep_data <- split_data(hpi_data)
train_data <- prep_data[[1]]
test_data <- prep_data[[2]]

## normalize price before train model
tr_log <- train_data 
tr_log$price <- train_data$price %>%
  log()

ts_log <- test_data
ts_log$price <- test_data$price %>%
  log()


## 2. train_model

set.seed(24)
model <- train(price ~. ,
               data = tr_log,
               method = "lm")
  #view model
model


## 3. scoring

p_log <- predict(model, newdata = ts_log)

p <- p_log %>%
  exp()


  # view predict
p


## 4. evaluate # before price_log


cal_mae <- function(actual, pred){
  error <- actual - pred
  mean(abs(error))
}

cal_mse <- function(actual, pred){
  error <- actual - pred
  mean(error ** 2)
}

cal_rmse <- function(actual, pred){
  error <- actual - pred
  sqrt(mean(error ** 2))
}


## evaulate price_log

cal_rmse(ts_log$price, p_log)
cal_mse(ts_log$price, p_log)
cal_mae(ts_log$price, p_log)

## evaulate exp(log_price)

cal_rmse(ts_log$price, p)
cal_mse(ts_log$price, p)
cal_mae(ts_log$price, p)





## finalModel

model$finalModel %>%
  summary()

## varImp

varImp(model)
