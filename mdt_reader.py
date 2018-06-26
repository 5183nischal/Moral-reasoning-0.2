import pickle
import collections
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import sklearn.svm


def reader(x = ""):

	if n ==
	PKL_PATH = "bb2genis.pkl"

	def loadDataset(pklPath):
	    with open(pklPath, "rb") as pklFile:
	        return np.array(pickle.load(pklFile, encoding="utf-8"))

	mdt = loadDataset(PKL_PATH)
	mdt = mdt.tolist()


