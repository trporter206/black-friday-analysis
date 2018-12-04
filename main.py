import csv
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

bf_data = pd.read_csv("BlackFriday.csv")

# print bf_data.isna().any()


#clean--------------------------------------------------------------------------
bf_data.fillna(value=0, inplace=True)
bf_data['Product_Category_2'] = bf_data['Product_Category_2'].astype(int)
bf_data['Product_Category_3'] = bf_data['Product_Category_3'].astype(int)

bf_data.drop(columns = ['User_ID', 'Product_ID'], inplace=True)

#explore------------------------------------------------------------------------
def genders():
    sns.countplot(bf_data['Gender'])

def ages():
    sns.countplot(bf_data['Age'], hue=bf_data['Gender'])

def marriage():
    sns.countplot(bf_data['Age'], hue=bf_data['Marital_Status'])

def occupation():
    sns.countplot(bf_data['Occupation'], hue=bf_data['Marital_Status'])

occupation()
plt.show()
