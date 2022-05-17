# Forecasting-average-weekly-NFT-prices-of-the-Parallel-Alpha-nft

![Parallel Alpha](https://github.com/JoAmps/Forecasting-average-prices-of-the-Parallel-Alpha-nft/blob/main/parallel%20alpha.jpeg)

# Project Name
Parallel Alpha NFT price forecasting weekly

## Project Intro/Objective
The ability to forecast the prices of any commodity is crucial for companies, traders, and individuals, to know the price of their commodity in the future, so they make better plans using this knowledge. NFTs are the new craze that everyone is jumping on,theres potential money in it, and the ability to forecast their prices, to know if an NFT's price would grow or decline in the future, is very important, so people can make decisions to make profits on them.

### Methods Used
* Databases
* Social Media and Financial APIs
* Data exploration/descriptive statistics
* Dimensionality reduction
* Clustering
* Statistical Testing
* Data processing/cleaning
* Natural Language Processing(NLP)
* Time series forecasting
* Data Visualization
* Dashboard building

### Technologies
* PostgreSQL
* Parsec and Twitter APIs
* Python
* Various python libraries for data science and machine learning
* NLTK
* Visual studio code, jupyter
* Git
* Tableau

## Project Description
#### Parallel Alpha NFT is one of the most popular NFTs, often in the top 10 rankings by popular websites. It has been traded over 65,000 times, meaning it's a very popular NFT that people have interests in. It is verified on the open sea(the world's largest nft marketplace) and has a huge community. Due to its popularity and high demand, knowing a lot about this nft, and being able to determine the future price of this NFT is likely to be a very profitable venture for all. All the financial details of this NFT, alongside tweets about this NFT, were obtained and used for this project. The analysis was done weekly, and the forecast was done two weeks ahead, meaning the following two weeks prices of this NFT were forecasted, to know if the NFT price would grow or decline, leading to a decision of whether to buy or sell. The results were outputted into a dashboard using Tableau, for all to see and understand.


### The questions I deemed to explore were:
#### Can various tweets by users on this NFT help in forecasting the future price of this NFT?
#### How strong is the relationship between the twitter features and the financial features of this NFT?
#### Which model could better forecast the future price of this NFT with the least amount of error?

#### Dimensionality reduction was performed to reduce the number of data points needed for clustering, to speed up the process, and the clustering as mentioned was needed to group tweets in various clusters, and select only those that corresponded with tweets about the parallel alpha NFT, as there are various tweets on parallel alpha that does not correspond to this use case

### Some of the challenges faced were:
#### Which DateTime aggregation would be best to perform these forecasts optimally 
#### How to integrate the Twitter data with the financial data


## Getting Started and to use this:

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Run [ingest_nft_data_from_api.py] using your own parsec credentials to ingest data from the API
3. Run [insert_nftdata_into_database.py] using your own PostgreSQL credentials to insert the ingested parsec data into the database
4. Run [ingest_and_insert_twitter_into_database.py] to extract Twitter data using the time range of your choice, and it inserts the Twitter data into a PostgreSQL database, using your own PostgreSQL credentials
5. Run the notebook, which performs every step of the process and stores the results into a CSV file, and saves it on your local drive, ready to be deployed to Tableau


## Results


#### The data were aggregated weekly, so the average prices of the nft in that week were used. Three models were used for the forecasting, prophet, Arima, and random forest. They all forecast one week ahead of price. 
#### The data from Twitter was also aggregated weekly, and was joined to the financial data, these are the correlations among all the features. Remember the target is mean_price. There is quite a good correlation between the features and the target, especially the Twitter features.


![Correlations](https://github.com/JoAmps/Forecasting-average-prices-of-the-Parallel-Alpha-nft/blob/main/Correlations.png)

Arima is a univariate algorithm, which means it only takes into account one feature and the date, so it didn't take into account the Twitter data and the other financial data, Prophet and Random forest are multivariate algorithms, they take into account more than one feature, so all the features were fed to these algorithms, these are the mean absolute errors(MAE) of the 3 algorithms. Prophet had the lowest mae, and Arima had the highest, remember, the smaller the mae, the better, so the prophet model was the best model in this case.
![MAE](https://github.com/JoAmps/Forecasting-average-prices-of-the-Parallel-Alpha-nft/blob/main/mae.png)

As already mentioned, the models forecasted one week ahead, and these are the growth of the prices the model predicts, that is, the growth of price from the current week to the next week on average. Though all the models have different prices of what the parallel alpha nft could be in the next week, they all predict a growth in the price.
Remember, a negative value on the growth of a price means a decline, and a positive means a growth

![Forecasted price](https://github.com/JoAmps/Forecasting-average-weekly-prices-of-the-Parallel-Alpha-nft/blob/main/Growth%20of%20price.png)

## Summary
All the models had low mae which means they do well to forecast the price, but since the Arima model didn't consider any of the features aside from the date and the price, the focus is on the prophet and the random forest, which achieved better results anyway.  The prophet had the best results to forecast the price with the lowest mae, and it forecasts the price of the NFT to be 0.62, which is a growth of 0.05 from the previous week.  As mentioned, all the models predict there to be a growth in the prices in the following week, which suggests, this is an nft to pay attention to.

## Deploying to Tableau
Below is a screenshot of the Dashboard developed in Tableau, in which the output of the model and analysis is deployed onto
![Dashboard1](https://github.com/JoAmps/Forecasting-average-weekly-prices-of-the-Parallel-Alpha-nft/blob/main/Dashboard%201.png)
Its a very simple UI that non technical people can view and understand what is happening, the trend of the average prices of the nft weekly since last year august, and the forecast for the next week. The mean absolute error is displayed there, which can simply in lay man terms be explained as the amount of error between what our model preidicted, and what the prices actually were. It can clearly be seen that there was a growth in price, which is also written down there. Only the best performing model's(prophet) results is displayed.
The interactive dashboard can be found here --> https://public.tableau.com/app/profile/hyacinth.ampadu5719/viz/ForecastingPriceofParallelAlphaNFT/Dashboard1?publish=yes

## Updating
To get forecast for the following week in every week, the code has to be run in this process:
#### Run ingest_nft_data_from_api.py to ingest the latest data from the parsec api
#### Run insert_nftdata_into_database.py to insert the ingested parsec data into the postgresql database(using your credentials)
#### Run ingest_and_insert_twitter_into_database.py to ingest latest twitter data and insert into the postgresql database
#### Run the notebook forecasting weekly floor prices of parallel alpha.ipynb, that analyzes all the data, performs feature engineering, statistical testing and trains and evaluates the models and outputs it into a dataframe
#### After, take the outputted data and update the Tableau dashboard
