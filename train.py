# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import classification_report

# data = pd.read_csv('/home/becca/Downloads/archives/password-strength/data.csv', error_bad_lines=False)
data = pd.read_csv("/home/becca/Downloads/archive (14)/Restaurant_Reviews.tsv", sep='\t')
print(data)

print(data.info())

print(data['Liked'].unique())

# - 0 - Weak Password
# - 1 - Moderate Strength Password
# - 2 - Great Password

# Check for null values
print(data.isnull().sum())

# Dropping the null record
print(data.dropna(inplace=True))

# Again checking the null values
print(data.isna().sum())

# Plotting the strength of password distribution
print(sns.countplot(data['Liked']))

sentiment_array = np.array(data)
print(sentiment_array)

print(random.shuffle(sentiment_array))

x = [labels[0] for labels in sentiment_array]
y = [labels[1] for labels in sentiment_array]


def word_divide(inputs):
    c = []
    for i in inputs:
        c.append(i)
    return c


vectorizer = TfidfVectorizer(tokenizer=word_divide)
X = vectorizer.fit_transform(x)

print(X.shape)

print(vectorizer.get_feature_names())

first_document_vector = X[0]
print(first_document_vector)

print(first_document_vector.T.todense())

# Creating a dataframe for TF-IDF
df = pd.DataFrame(first_document_vector.T.todense(), index=vectorizer.get_feature_names(), columns=['TF-IDF'])
print(df)

# Most used symbol or letter or character
print(df.sort_values(by=['TF-IDF'], ascending=False))

# Splitting the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(X_train.shape)

# Logostic Regression
classifier = LogisticRegression(random_state=0, multi_class='multinomial')
print(classifier.fit(X_train, y_train))

# Predicting results using logistic regression
dt = np.array(['Great'])
pred = vectorizer.transform(dt)
print(classifier.predict(pred))

y_pred = classifier.predict(X_test)
print(y_pred)

cm = confusion_matrix(y_test, y_pred)
print(cm)

print(accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

# saving the model
import pickle

pickle_out = open("classifier.pkl", mode="wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()
