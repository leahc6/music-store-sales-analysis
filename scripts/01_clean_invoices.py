# -*- coding: utf-8 -*-
"""
Script: 01_clean_invoices.py
Purpose: Clean and prepare the invoices dataset for analysis
Author: Leah Carroll
Python version: 3.12.11

"""

import pandas as pd


#1. Load and inspect data
df = pd.read_csv('Invoices.csv')
print(df.head())
print(df.info())
#Data loaded successfully
#Identified missing values and incorrect data type for InvoiceDate


#2. Clean missing values
#Count missing values per column
print('\nMissing values per column:')
print(df.isna().sum())
#Missing values detected in City, Country, Postal Code and State columns

#Inspect rows with missing City or Country 
missing_location = df.loc[(df['BillingCity'].isna()) | 
                          (df['BillingCountry'].isna()), 
                          ['BillingCity', 'BillingCountry', 'BillingAddress']]
print(f'Rows with missing location: {missing_location}')

#Fill missing Country values using mapping from City
city_country_map = {
    'Lyon':'France',
    'Paris':'France',
    'Winnipeg':'Canada',
    'Copenhagen':'Denmark',
    'Santiago':'Chile',
    'London':'United Kingdom',
    'Porto':'Portugal',
    'Vienne':'Austria',
    'São Paulo':'Brazil'
    }

df['BillingCountry'] = df['BillingCountry'].fillna(
    df['BillingCity'].map(city_country_map)
    )

#Fill missing Cities
df.loc[312, 'BillingCity'] = 'Lisbon'
df.loc[410, 'BillingCity'] = 'Toronto'

#Verify updates 
print(df.loc[312])
print(df.loc[410])

#Fill missing Postal Codes
df['BillingPostalCode'] = df['BillingPostalCode'].fillna('Unknown')

#Remove State column due to excessive number of missing values
df.drop('BillingState', axis=1, inplace=True)

#Verify that no missing values remain
print(df.isna().sum())


#3. Clean duplicates 
#Count duplicate rows
print(f'Number of duplicate rows: {df.duplicated().sum()}')
#Identified 1 duplicate row

#Remove duplicate row
df.drop_duplicates(inplace=True)
#Verify removal
print(f'Updated number of duplicate rows: {df.duplicated().sum()}')

#Check for duplicates in InvoiceID
print(f"Duplicate Invoice IDs: {df[df['InvoiceID'].duplicated(keep=False)]}")
#Duplicate InvoiceID found (row 402)

#Remove duplicate row
df.drop_duplicates(subset='InvoiceID', inplace=True)

#Verify removal 
duplicate_Invoice_IDs = df[df['InvoiceID'].duplicated(keep=False)]
print(f'Updated duplicate Invoice IDs: {duplicate_Invoice_IDs}')


#4. Clean text columns 
#Remove leading and trailing spaces
df['BillingAddress'] = df['BillingAddress'].str.strip()
df['BillingCity'] = df['BillingCity'].str.strip()
df['BillingCountry'] = df['BillingCountry'].str.strip()
df['BillingPostalCode'] = df['BillingPostalCode'].str.strip()
df['InvoiceDate'] = df['InvoiceDate'].str.strip()

#Standardise format
df['BillingAddress'] = df['BillingAddress'].str.title()
df['BillingCity'] = df['BillingCity'].str.title()
df['BillingCountry'] = df['BillingCountry'].str.title()


#Check for incorrect spelling/formatting in Billing City
print(df['BillingCity'].value_counts()) 
#Replace errors in Billing City
df['BillingCity'] = df['BillingCity'].replace({
    'Sidney':'Sydney',
    'Vienne':'Vienna',
    'Ny':'New York',
    'Pari':'Paris',
    'Roome':'Rome',
    'Rio':'Rio De Janeiro'
    })
#Verify change
print(df['BillingCity'].value_counts())

#Check for incorrect spelling/formatting in Billing Country
print(df['BillingCountry'].value_counts())
#Replace error in Billing Country
df['BillingCountry'] = df['BillingCountry'].replace('Usa','USA')
#Verify change
print(df['BillingCountry'].value_counts())


#5. Clean numeric columns
#Check for outliers
print(df[['InvoiceID', 'CustomerID', 'Total']].describe())
#No outliers detected; no further cleaning required 


#6. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(
    df['InvoiceDate'], dayfirst=True, errors='coerce'
    )

#Verify that no values failed to convert
print(df[df['InvoiceDate'].isna()])
#Check date range to identify outliers
print(df['InvoiceDate'].min(), df['InvoiceDate'].max())

#Confirm that data type for InvoiceDate is now datetime
print(df['InvoiceDate'].dtypes)


#7. Check that all Customer IDs exist in Customer dataset
#Load Customer dataset
customers = pd.read_csv('Customers.csv')

#Identify invoices with Customer IDs not present in Customer dataset
invalid_customer_IDs = df[~df['CustomerID'].isin(customers['CustomerID'])]

print('\nInvoices with invalid Customer IDs:')
print(invalid_customer_IDs)

#8. Perform final checks
print(df.info())
print(df.sample(10))


#8. Save cleaned DataFrame
df.to_csv('Invoices_clean.csv', index=False, encoding='utf-8', 
          date_format='%d/%m/%Y')