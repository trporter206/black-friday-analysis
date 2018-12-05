import csv
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

bf_data = pd.read_csv("BlackFriday.csv")
bf_train = bf_data.head(10000)

# print bf_data.isna().any()


#clean--------------------------------------------------------------------------
bf_train.fillna(value=0, inplace=True)
bf_train['Product_Category_2'] = bf_train['Product_Category_2'].astype(int)
bf_train['Product_Category_3'] = bf_train['Product_Category_3'].astype(int)

bf_train.drop(columns = ['User_ID', 'Product_ID'], inplace=True)

#explore------------------------------------------------------------------------
def genders():
    # sns.countplot(bf_train['Gender'])
    sns.boxplot(x= 'Gender', y= 'Purchase', data= bf_train)

def ages():
    sns.countplot(bf_train['Age'], hue=bf_train['Gender'])
    # sns.boxplot(x='Age', y= 'Purchase', data=bf_train)

def marriage():
    women = bf_train[bf_train.Gender == 'F']
    sns.countplot(women['Age'], hue=women['Marital_Status'])
    # sns.boxplot(x='Marital_Status', y= 'Purchase', hue= 'Gender', data=bf_train)

def occupation():
    sns.boxplot(x='Occupation', y= 'Purchase', data=bf_train)

def cities():
    # sns.countplot(bf_train['City_Category'], hue=bf_train['Age'])
    sns.boxplot(x='City_Category', y= 'Purchase', data=bf_train)

def stay():
    # sns.countplot(bf_train['Stay_In_Current_City_Years'])
    sns.boxplot(x='Stay_In_Current_City_Years', y= 'Purchase', data=bf_train)

def purchasers():
    m0 = pd.Series(bf_train[(bf_train.Marital_Status == 0) & (bf_train.Gender == 'M')]['Purchase'])
    m1 = pd.Series(bf_train[(bf_train.Marital_Status == 1) & (bf_train.Gender == 'M')]['Purchase'])
    f0 = pd.Series(bf_train[(bf_train.Marital_Status == 0) & (bf_train.Gender == 'F')]['Purchase'])
    f1 = pd.Series(bf_train[(bf_train.Marital_Status == 1) & (bf_train.Gender == 'F')]['Purchase'])

    df = pd.DataFrame({'m0': m0, 'm1': m1, 'f0': f0, 'f1': f1})
    sns.boxplot(data=df)

    
purchasers()
plt.show()
