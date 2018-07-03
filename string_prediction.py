import pickle
import collections
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.svm
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from time import time
from multinomial_logistic import getClassifierAndVectorizer

def stringPrediction(word):
	x = []
	x.append(word)
	clf, vectorizer = getClassifierAndVectorizer()
	x_vector = vectorizer.transform(x)
	moral_proportion = clf.predict_proba(x_vector)
	return moral_proportion[0]

x='Liam'
print(stringPrediction(x))

