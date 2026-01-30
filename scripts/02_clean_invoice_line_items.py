# -*- coding: utf-8 -*-
"""
Script: 02_clean_invoice_line_items.py
Purpose: Clean and prepare the invoice line item dataset for analysis
Author: Leah Carroll
Python version: 3.12.11

"""

import pandas as pd


#1. Load and inspect data
df = pd.read_csv('Invoice_line_items.csv')
print(df.head())
print(df.info())
#Data loaded successfully; correct data types and no missing values


#2. Clean duplicates 
#Count number of duplicate rows
print(f'Number of duplicate rows: {df.duplicated().sum()}')
#No duplicate rows detected

#Check for duplicate InvoiceLine IDs
print(f'Duplicate InvoiceLineIDs: {
    df[df['InvoiceLineID'].duplicated(keep=False)]
    }')
#No duplicates detected


#3. Clean numeric columns
#Check for outliers
print(df.describe())
#No outliers or inconsistencies detected; no further cleaning required


#4. Add new 'Total Revenue' column
df['TotalRevenue'] = df['UnitPrice'] * df['Quantity']
#Confirm new column has been added
print(df.sample(15))


#5. Check that all Invoice IDs exist in Invoice dataset
#Load Invoice dataset
invoices = pd.read_csv('Invoices.csv')

#Identify invoice lines with Invoice IDs not present in Invoice dataset
invalid_invoice_IDs = df[~df['InvoiceID'].isin(invoices['InvoiceID'])]

print('\nInvoice Lines with invalid Invoice IDs:')
print(invalid_invoice_IDs)


#6. Check that all Track IDs exist in Track dataset
#Load Track dataset
tracks = pd.read_csv('Tracks.csv')

#Identify invoice lines with Track IDs not present in Track dataset
invalid_track_IDs = df[~df['TrackID'].isin(tracks['TrackID'])]

print('\nInvoice Lines with invalid Track IDs:')
print(invalid_track_IDs)


#7.Perform final checks
print(df.info())
print(df.sample(10))

#8. Save cleaned Dataframe
df.to_csv('Invoice_line_items_clean.csv', index=False, encoding='utf-8')