# Forecasting-average-NFT-prices-of-the-Parallel-Alpha-nft

![Parallel Alpha](https://github.com/JoAmps/Forecasting-average-prices-of-the-Parallel-Alpha-nft/blob/main/parallel%20alpha.jpeg)

# Project Name
Parallel Alpha NFT price forecasting

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
* Python
* Various python libraries for data science and machine learning
* NLTK
* Visual studio code, jupyter
* Git
* PowerBI

## Project Description
#### Parallel Alpha NFT is one of the most popular NFTs, often in the top 10 rankings by popular websites. It has been traded over 65,000 times, meaning it's a very popular NFT that people have interests in. It is verified on the open sea(the world's largest nft marketplace) and has a huge community. Due to its popularity and high demand, knowing a lot about this nft, and being able to determine the future price of this NFT is likely to be a very profitable venture for all. All the financial details of this NFT, alongside tweets about this NFT, were obtained and used for this project. The analysis was done weekly, and the forecast was done two weeks ahead, meaning the following two weeks prices of this NFT were forecasted, to know if the NFT price would grow or decline, leading to a decision of whether to buy or sell. The results were outputted into a dashboard using Power BI, for all to see and understand.


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
2. Run [ingest_nft_data_from_api.py] using you own parsec credentials to ingest data from the api
3. Run [insert_nftdata_into_database.py] using you own postgresql credentials to insert the ingested parsec data into the database
4. Run [extract_and insert_twitterdata_into_database] to extract twitter data using the time range of your choice, and it inserts the twitter data into a postgresql database, using your own postresql credentials
5. Run the notebook, which performs every step of the process and stores the results into a csv file and saves it on your local drive


## Results


![Confusion Matrix](https://github.com/JoAmps/Churn-prediction-in-a-vehicle-insurance-company-in-Ghana/blob/main/confusion_matrix.png)

#### From the original dataset of customers which comprised of 8800 customers, after several experimentation, using different models, the xgboost model performed the best, with a recall of 95.9% and precision of 97.7%
#### 15 false positives, which indicates 15 customers who actually churned, were predicted as not churned, and 6 false negatives, which means 6 customers did not churn, and they were predicted as churned was obtained
#### Though this result is good, the performance was improved by hyper parameter tuning
#### Now theres a decision to determine which is more suited to the business, so theres a tradeoff between false positives and false negatives
#### More false positives suggests that there are more customers who churned, that the model did not pick up, in such a case, if the number is high, the company would have to spend money and resources on those customers to get them to not churn, for example more personalized advertissment, more incentives and discounts
#### More false negatives suggests that there are more customers who did not churn, but the model predicted them to churn, in this situation, if this number is high, the company woud be spending time and resources on the wrong customers

![Roc_auc](https://github.com/JoAmps/Churn-prediction-in-a-vehicle-insurance-company-in-Ghana/blob/main/roc_auc_curve.png)
#### So there is this tradeoff in what is important to the company, which situation they deem most profitable to pursue, using that knowledge, we adjust the threshold to take care of that
#### I used a threshold of 0.59, to reduce the false positives to 9, and increase the false negatives to 10, but this decision is based on the company needs and wants

![Feature importances](https://github.com/JoAmps/Churn-prediction-in-a-vehicle-insurance-company-in-Ghana/blob/main/feature_importance.png)

## Monitoring
I created a monitoring script, which detects if new data is available(more customers), and if new data is available, performs inference on the data and compares the new recall score to the previous score, if the new score is equal or higher than the previous, it suggests that model drift has not occurred, and if the score is lower, it is a possible indication that model drift has occurred, and further investigation is required, such as model retraining and the likes
