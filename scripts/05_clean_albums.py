# -*- coding: utf-8 -*-
"""
Script: 05_clean_albums.py
Purpose: Clean and prepare the albums dataset for analysis
Author: Leah Carroll
Python version: 3.12.11

"""

import pandas as pd

#1. Load and inspect data
df = pd.read_csv('Albums.csv')
print(df.head())
print(df.info())
#Data loaded successfully; correct data types and no missing values


#2. Clean duplicates 
#Count duplicate rows 
print('\nNumber of duplicate rows:')
print(df.duplicated().sum()) 
#No duplicate rows detected

#Check for duplicates in AlbumID 
print('\nDuplicate Album IDs:')
print(df[df['AlbumID'].duplicated(keep=False)]) 
#No duplicates Album IDs detected

#Check for duplicates in Title
print('\nDuplicate Titles:')
print(df[df['Title'].duplicated(keep=False)])
#No duplicates Titles detected

#3. Clean text columns 
#Remove leading and trailing spaces 
df['Title'] = df['Title'].str.strip() 

#Inspect unique values in Title column
print('\nNumber of Unique Titles:')
print(df['Title'].nunique()) 
#Confirmed that all 347 Titles are unique

print('\nUnique Titles:')
print(df['Title'].sort_values().unique())
#Identified multiple Titles with errors

#Correct errors for identified Titles
df['Title'] = df['Title'].replace({
    'A TempestadeTempestade Ou O Livro Dos Dias':'A Tempestade ou O Livro Dos Dias',
    'DUOS II':'Duos II',
    'fireball':'Fireball',
    'frank':'Frank',
    'GET BORN':'Get Born',
    'IRON MAIDEN':'Iron Maiden',
    'ZOOROPA':'ZOOROPA'
    })

#Verify corrections
print('\nUnique Titles Updates:')
print(df['Title'].sort_values().unique())


#4. Check that all Artist IDs exist in Artist dataset
#Load Artist dataset
artists = pd.read_csv('Artists.csv')

#Identify albums with Artist IDs not present in Artist dataset
invalid_artist_IDs = df[~df['ArtistID'].isin(artists['ArtistID'])]

print('\nAlbums with invalid Artist IDs:')
print(invalid_artist_IDs)


#5. Perform final checks
print(df.isna().sum())
print(df.describe())
print(df.info())
print(df.sample(10))
#No outliers or missing values detected. Correct data types confirmed.

#6. Save cleaned DataFrame
df.to_csv('Albums_clean.csv', index=False, encoding='utf-8')


