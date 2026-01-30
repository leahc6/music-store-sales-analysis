# -*- coding: utf-8 -*-
"""
Script: 03_clean_tracks.py
Purpose: Clean and prepare the tracks dataset for analysis
Author: Leah Carroll
Python version: 3.12.11

"""

import pandas as pd

#1. Load and inspect data
df = pd.read_csv('Tracks.csv')
print(df.head())
print(df.info())
#Data loaded successfully
#Identified missing values in Composer column. Data types are correct.


#2. Clean missing values
#Count missing values in Composer column
print('\nNumber of missing values:')
print(df['Composer'].isna().sum())

#Fill missing values with 'Unknown'
df['Composer'] = df['Composer'].fillna('Unknown')

#Verify changes
print(df['Composer'].sample(10))
print('\nUpdated number of missing values:')
print(df['Composer'].isna().sum())


#3. Clean duplicates
#Count number of duplicate rows
print(f'No. of duplicated rows: {df.duplicated().sum()}')
print(df[df.duplicated(keep=False)])
#No duplicated rows found

#Check for duplicate Track IDs
print(f"Duplicated TrackIDs: {df[df['TrackID'].duplicated(keep=False)]}")
#No duplicate Track IDs found

#Check for duplicate Track Names within the same album
print('\nDuplicate Track Names:')
print(df[df[['Name', 'AlbumID']].duplicated(keep=False)])
#Identified duplicate track names within the same album 
#Tracks have different durations and sizes, indicating distinct versions
#No records were removed or altered


#4. Clean text columns
#Remove leading/trailing spaces
df['Name'] = df['Name'].str.strip()
df['Composer'] = df['Composer'].str.strip()

#Check for incorrect spelling/formatting in Name column
#Spot-check rare Names
print(df['Name'].value_counts().tail(50))

#Check total number of unique track names
print('\nNumber of Unique Track Names:')
print(df['Name'].nunique())
#Confirmed that 3256 Names are unique

#Sample 20% of unique Names for inspection
unique_names = pd.Series(df['Name'].unique())
sampled_names = unique_names.sample(700)
#Save the sample to CSV for easier inspection
sampled_names.to_csv('Sample_track_names.csv')

#Correct error in track name
df['Name'] = df['Name'].replace(
    "Intro- Churchill S Speech","Intro - Churchill's Speech"
    )

#Check for incorrect spelling/formatting in Composer column
#Spot check for inconsistencies
print(df['Composer'].value_counts().head(50))
print(df['Composer'].sample(50))

#Inspect unique values in Composer column
print('\nNumber of Unique Composers:')
print(df['Composer'].nunique())

print('\nUnique Composers:')
print(df['Composer'].unique())

#Correct errors found in Composer
df['Composer'] = df['Composer'].replace({
    'jim croce':'Jim Croce',
    'ervin drake':'Ervin Drake',
    'cole porter':'Cole Porter',
    'bart  howard':'Bart Howard'
    })

#Verify changes
print('Composer errors after update:')
print(df[df['Composer'].isin([
    'jim croce', 'ervin drake', 'cole porter', 'bart  howard'
     ])])


#5. Clean numeric columns
#Check for outliers
print(df.describe())
print(df[['GenreID', 'Milliseconds']].describe())
#No outliers or inconsistencies detected
#GenreID and Milliseconds were reviewed separately due to wide output display


#6. Check that all Album IDs exist in Album dataset
#Load Album dataset
albums = pd.read_csv('Albums.csv')

#Identify tracks with Album IDs not present in Album dataset
invalid_album_IDs = df[~df['AlbumID'].isin(albums['AlbumID'])]

print('\nTracks with invalid Album IDs:')
print(invalid_album_IDs)


#7. Check that all Genre IDs exist in Genre dataset
#Load Genre dataset
genres = pd.read_csv('Genres.csv')

#Identify tracks with Genre IDs not present in Genre dataset
invalid_genre_IDs = df[~df['GenreID'].isin(genres['GenreID'])]

print('\nTracks with invalid Genre IDs:')
print(invalid_genre_IDs)


#8.Perform final checks
print(df.info())
print(df.isna().sum())
print(df.sample(10))


#9. Save cleaned Dataframe
df.to_csv('Tracks_clean.csv', encoding='utf-8', index=False)