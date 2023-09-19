#Import relevant libraries
import pandas as pandas
import numpy as np

#Load both crawls into pandas as seperate DataFrames, selecting certain columns to work with
#The 'Internal_HTML' export from Screaming Frog works well here
dfMobile = pd.DataFrame(pd.read_csv('mobile_crawl_path.csv', low_memory=False, header=1))
dfMobile = dfMobile[['Address', 'Status Code', 'Word Count', 'Outlinks', 'Unique Outlinks', 'Inlinks', 'Unique Inlinks', 'Canonical Link Element 1']].copy()

#And repeat for Desktop crawl
dfDesktop = pd.DataFrame(pd.read_csv('desktop_crawl_path.csv', low_memory=False, header=1))
dfDesktop = dfDesktop[['Address', 'Status Code', 'Word Count', 'Outlinks', 'Unique Outlinks', 'Inlinks', 'Unique Inlinks', 'Canonical Link Element 1']].copy()

#Combine the 2 crawls into a single dataframe, merging on common Address
df = pd.merge(dfMobile, dfDesktop, left_on='Address', right_on='Address', how='outer')

#Check differences between the two crawls
df['Diff Wordcount'] = df['Word Count_y'] - df['Word Count_x']
df['Diff Outlinks'] = df['Outlinks_y'] - df['Outlinks_x']
df['Diff Unique Outlinks'] = df['Unique Outlinks_y'] - df['Unique Outlinks_x']
df['Diff Inlinks'] = df['Inlinks_y'] - df['Inlinks_x']
df['Diff Unique Inlinks'] = df['Unique Inlinks_y'] - df['Unique Inlinks_x']
df['Canonicals are equal'] = np.where((df['Canonical Link Element 1_y'] == df['Canonical Link Element 1_x']), 'Yes', 'No')

#Export as Excel file
df.to_excel('crawl_comparison_path.xlsx')

#Or export as CSV file
df.to_csv('crawl_comparison_path.csv')