# -----<<<< CAPSTONE PROJECT - NLP APPLICATIONS >>>------

import pandas as pd
import numpy as np
import spacy
from textblob import TextBlob
nlp = spacy.load('en_core_web_sm')

# LOADING THE DATA SET ------------------------------------------------------------------------

# load dataset using pandas
amazon_reviews = pd.read_csv("amazon_product_reviews.csv")


# DATA CLEANING -------------------------------------------------------------------------------

# extracting the required columns
clean_data = amazon_reviews['reviews.text']

# counting null values in each column
clean_data.isnull().sum()

# dropping null values
clean_data = amazon_reviews.dropna(subset=['reviews.text'])

# checking that all null values are dropped
clean_data.isnull().sum()

text = clean_data['reviews.text']


# PREPROCESSING -------------------------------------------------------------------------------

# defining function to preprocess text: lowercasing, tokenising, lemmatising, removing stop words and punctuations
def preprocess(text):
   doc = nlp(text.lower().strip())
   processed = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
   
   return ' '.join(processed)

# creating a new column to store 'processed.text' data
clean_data['processed.text'] = clean_data['reviews.text'].apply(preprocess)

# reviewing first five entries with new 'processed.text' column
clean_data.head()



# CREATING A FUNCTION FOR SENTIMENT ANALYSIS ---------------------------------------------------

# Choosing 'processed.text' column for sentiment analaysis
text1 = clean_data['processed.text']

# Defining function that takes in review as parameter and returns polarity score and sentiment
def analyse_polarity(text1):
   
    # Analysing sentiment using TextBlob
    blob = TextBlob(text1)
    polarity = blob.sentiment.polarity
    
    return polarity



# SENTIMENT ANALYSIS TEST - 1 -------------------------------------------------------------------

# Assigning 1st entry from 'processed.txt' using indexing 
my_review_of_choice = clean_data['processed.text'][0]

# applying function to analyse sentiment and reveal polarity score for review 
polarity_score = analyse_polarity(my_review_of_choice)

# polarity score conditions for analysing sentiment
if polarity_score > 0:
    sentiment = 'positive'
elif polarity_score < 0:
    sentiment = 'negative'
else:
    sentiment = 'neutral'

# output text with polarity score and sentiment prediction
print(f"Text: {my_review_of_choice}\nPolarity score: {polarity_score}\nSentiment: {sentiment}")

# RESULT --> Polarity score: -0.016666666666666663 & Sentiment: Negative



# SENTIMENT ANALYSIS TEST -2 ---------------------------------------------------------------------

# Assigning 6th entry from 'processed.txt' using indexing 
my_review_of_choice = clean_data['processed.text'][5]

# applying function to analyse sentiment and reveal polarity score for review 
polarity_score = analyse_polarity(my_review_of_choice)

# polarity score conditions for analysing sentiment
if polarity_score > 0:
    sentiment = 'positive'
elif polarity_score < 0:
    sentiment = 'negative'
else:
    sentiment = 'neutral'

# output text with polarity score and sentiment prediction
print(f"Text: {my_review_of_choice}\nPolarity score: {polarity_score}\nSentiment: {sentiment}")

# RESULT --> Polarity score: 0.5599999999999999 Sentiment: Positive
