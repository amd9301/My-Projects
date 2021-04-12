"""
Created on 12 th April 2021
Author: Mounika Durga

"""

import pandas as pd
import requests

#1. Get the website URL ,Data Collection 
url='https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid-19-pandemic-data'
req =requests.get(url)


data_list = pd.read_html(req.text)

target_df  = data_list[0]

# 2.Data Cleaning

#We are only considering column no 1,2,3,4

#Giving the column Names as our wish
target_df.columns=['Col0','CountryName','Total Cases','Total Deaths','Total Recoveries','Col5']

#Issue : Extra Columns
#Extracting required cols and saving them

target_df = target_df[['CountryName','Total Cases','Total Deaths','Total Recoveries']]

#Issue : Extra Rows
#240,239,238

#target_df = target_df.drop([238,239,240])

last_idx=target_df.index[-1]
target_df = target_df.drop([last_idx,last_idx-1,last_idx-2])

#Issues : Incosistent Country Names
#Use Regular Expressions

#Use str replace fn of pandas lib

target_df['CountryName'] = target_df['CountryName'].str.replace('\[.*\]','')
target_df['Total Deaths'] = target_df['Total Deaths'].str.replace('+','')

#Issue : No data in Col 4  , we will use replace function
target_df['Total Recoveries'] = target_df['Total Recoveries'].str.replace('No data','0')

# Issue : Wrong data type ,convert to  number from string
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])

#We are done with Data Collection and Data Cleaning

# 3 . Now we have to do Data Organization

#Export the data

target_df.to_csv(r'covid19_dataset.csv')
#target_df.to_excel(r'covid19_dataset.xlsx')


