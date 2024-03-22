# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

!git add "SEC_Filings.py"
!git commit -m "SEC_Data_Pulls"
!git push origin master

import requests
import pandas as pd

# Create Request Header
headers = {'User-Agent': "rboletcafaro@gmail.com"}


# Get all companies data
companyTickers = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)

# review response keys

print(companyTickers.json().keys())

# format response to dictionary and get first key / value

firstEntry = companyTickers.json()['0']

# Parse CIK // without leading zeros

directCik = companyTickers.json()['0']['cik_str']

companyData = pd.DataFrame.from_dict(companyTickers.json(), orient='index')

# add leading zeros to CIK
companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)

# Review Data
print(companyData[:1])

cik = companyData[0:1].cik_str[0]

# Get Company Specific Filing Metadata
filingMetadata = requests.get(f'https://data.sec.gov/submissions/CIK{cik}.json', headers=headers)


# Review json
print(filingMetadata.json().keys())
filingMetadata.json()['filings']
filingMetadata.json()['filings'].keys()
filingMetadata.json()['filings']['recent']
filingMetadata.json()['filings']['recent'].keys()

# Dictionary to Dataframe
allForms = pd.DataFrame.from_dict(filingMetadata.json()['filings']['recent'])


# Review Columns
allForms.columns
allForms[['accessionNumber', 'reportDate', 'form']].head(50)

#  Metadata by row
allForms.iloc[11]

# Get Company Facts Data
companyFacts = requests.get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',headers=headers)

# Review Data
companyFacts.json().keys()
companyFacts.json()['facts']
companyFacts.json()['facts'].keys()

# Filing Metadata (DEI)
companyFacts.json()['facts']['dei']
companyFacts.json()['facts']['dei'].keys()
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding']
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding'].keys()
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding']['units']
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding']['units'].keys()
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding']['units']['shares']
companyFacts.json()['facts']['dei']['EntityCommonStockSharesOutstanding']['units']['shares'][0]

# Filing Metadata (US GAAP)
companyFacts.json()['facts']['us-gaap']
companyFacts.json()['facts']['us-gaap'].keys()
companyFacts.json()['facts']['us-gaap']['Revenues']
companyFacts.json()['facts']['us-gaap']['Assets']

# Get Company Concept Data
companyConcept = requests.get((f'https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}'f'/us-gaap/Assets.json'), headers=headers)

# Review Data
companyConcept.json().keys()
companyConcept.json()['units']
companyConcept.json()['units'].keys()
companyConcept.json()['units']['USD']
companyConcept.json()['units']['USD'][0]

# Parse Assetss form single filing
companyConcept.json()['units']['USD'][0]['val']

# Get all filings data
assetsData = pd.DataFrame.from_dict((companyConcept.json()['units']['USD']))

# Review Data
assetsData.columns
assetsData.form

# Get Assets From 10Q forms and reset index
assets10Q = assetsData[assetsData.form == '10-Q']
assets10Q = assets10Q.reset_index(drop=True)

# Plot Data
assets10Q.plot(x='end', y='val')
