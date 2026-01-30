# -*- coding: utf-8 -*-
"""
Script: 04_clean_artists.py 
Purpose: Clean and prepare the Artists dataset for analysis 
Author: Leah Carroll 
Python version: 3.12.11 

""" 

import pandas as pd 


#1. Load and inspect data
df = pd.read_csv('Artists.csv') 
print(df.head()) 
print(df.info()) 
#Data loaded successfully; correct data types and no missing values


#2. Clean duplicates 
#Count duplicate rows 
print('\nNumber of duplicate rows:')
print(df.duplicated().sum()) 
#Identified 4 duplicate rows 

#Remove duplicate rows 
df.drop_duplicates(inplace=True) 

#Verify removal of rows 
print('\nUpdated number of duplicate rows:')
print(df.duplicated().sum()) 

#Check for duplicates in ArtistID 
print('\nDuplicate Artist IDs:')
print(df[df['ArtistID'].duplicated(keep=False)]) 


#3. Clean text columns 
#Remove leading and trailing spaces 
df['Name'] = df['Name'].str.strip() 

#Check for incorrect spelling or formatting
print('\nAll Artists:')
print(df['Name'].sort_values().unique()) 
#Identified multiple names with format inconsistencies 

#Correct formatting for identified names
df['Name'] = df['Name'].replace({ 
    'IRON MAIDEN':'Iron Maiden',
    'QUEEN':'Queen',
    'RODOX':'Rodox',
    'RUSH':'Rush',
    'ben harper':'Ben Harper',
    'chris cornell':'Chris Cornell',
    'def leppard':'Def Leppard',
    'gerald moore':'Gerald Moore',
    'guns n roses':"Guns N' Roses",
    'maurizio pollini':'Maurizio Pollini'
    })

#Verify formatting corrections
print('\nAll Artists Updated:')
print(df['Name'].sort_values().unique())


#4. Perform final checks
print(df.isna().sum())
print(df.describe())
print(df.info())
print(df.sample(10))
#No outliers or missing values detected. Correct data types confirmed.


#5. Save cleaned DataFrame
df.to_csv('Artists_clean.csv', index=False, encoding='utf-8')
