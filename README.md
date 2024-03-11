# SENTIMENT ANALYSIS

## THE PROJECT ---

Developed a python programme that performs sentiment analysis on a dataset of product reviews. 
Sentiment analysis is widely used for social media monitoring, customer feedback analysis, brand monitoring, market research and competitive analysis.
In this project, sentiment analysis plays a pivotal role in analysing customer feedback for various products sold on Amazon. 

### Dataset:
"https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products?select=Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv"  downloaded from:  Consumer Reviews of Amazon Products (kaggle.com).

### How it works:
This programme takes in a customer review and returns a  polarity score which enables sentiment analysis. 
A polarity score > 0 indicates a positive sentiment, while a polarity score < 0 indicates a negative sentiment, and 
a polarity score of 0 indicates a neutral sentiment. 
By categorising feedback as positive, negative or neutral, companies can identify areas of improvement, address complaints, improve product quality 
and enhance customer satisfaction. 

#### Example screenshot 1: 1st Review Evaluation (Choosing 1st entry from dataframe):  
Review text: 'I thought it would be as big as small paper but turn out to be just like my palm. I think it is too small to read on it... not very comfortable as regular Kindle. Would definitely recommend a paperwhite instead.'

Processed text: think big small paper turn like palm think small read comfortable regular kindle definitely recommend paperwhite instead


<img width="478" alt="image" src="https://github.com/PDeepa4/finalCapstone/assets/151678876/10b409f0-5421-4104-8dec-d7d4d2583932">


#### Example screenshot 2: 2nd Review Evaluation (Choosing 6th entry from dataframe):  
Review text: “This make an excellent ebook reader. Don't expect much from this device except to read basic ebooks. The good thing is it's cheap and good to read in the sun.”

Processed text: excellent ebook reader expect device read basic ebook good thing cheap good read sun

<img width="507" alt="image" src="https://github.com/PDeepa4/finalCapstone/assets/151678876/00a442ce-e66b-4687-8e03-732d67bb2d72">




#### Installation Guide:
- Open a terminal or command prompt on your local machine.
- Clone the finalCapstone repository by using the git clone command, git clone "https://github.com/PDeepa4/finalCapstone" to your local machine.
- Use the cd command to navigate into the directory of the cloned repository.
- Now you can select the sentiment_analysis.py file and start using it to analyse sentiments.
- Different data sets can be used but the programme will need to be rerun by loading that specific dataset, will require renaming of dataframes,
  cleaning and preprocessing.
- If not datasets, reviews can be fed into the function to analyse sentiment. If the data is not cleaned, the accuracy of the prediction may be compromised.
