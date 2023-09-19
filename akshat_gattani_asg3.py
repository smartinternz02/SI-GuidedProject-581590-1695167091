# -*- coding: utf-8 -*-
"""Akshat Gattani Asg3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LGUbHKUVp04d1AnkqL1tIqyi-SPP5QKa
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv("Titanic-Dataset.csv")

data.head()

data.info()

data.describe()

data.isnull().any()

data.isnull().sum()

data.Age.fillna(data.Age.median(), inplace = True)

data.Cabin.fillna(data.Cabin.mode()[0], inplace = True)

data.Embarked.fillna(data.Embarked.mode()[0], inplace = True)

data.isnull().sum()

data.head()

plt.subplots(figsize = (15,10))
sns.heatmap(data.corr(), annot = True)

plt.hist(data.Survived, range = [0, 1])

plt.hist(data.Fare)

plt.hist(data.Age)

sns.barplot(x = data["Survived"].value_counts().index, y = data["Survived"].value_counts())

sns.barplot(x = data["Pclass"].value_counts().index, y = data["Pclass"].value_counts())

sns.boxplot(data.Age)

q1 = data.Age.quantile(0.25)
q3 = data.Age.quantile(0.75)

print(q1)
print(q3)

IQR = q3 - q1
IQR

upper_limit = q3 + 1.5*IQR
lower_limit = q1 - 1.5*IQR

print(upper_limit)
print(lower_limit)

data = data[data["Age"] < upper_limit]

data = data[data["Age"] > lower_limit]

sns.boxplot(data.Age)

data.head()

y = data.Survived

x = data.iloc[:, np.r_[2:3, 4:8, 9:12]]

print(type(x))
print(type(y))

x.head()

y.head()

x.Sex.value_counts()

le = LabelEncoder()

x.Sex

x.head()

x.Cabin.value_counts()

x.Embarked.value_counts()

emb = pd.get_dummies(x.Embarked, drop_first = True)

emb

x = pd.concat([x, emb], axis = 1)
x

x.drop(["Embarked"], axis=1, inplace = True)
x

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state = 0)

x_train.head()

from sklearn.linear_model import LinearRegression

lr = LinearRegression()