# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Cleans 'spatial' and 'subject' metadata columns

# Imports 
import pandas as pd
import re 

# Read all-metadata.csv 
df = pd.read_csv('{FILE-PATH}/all_metadata.csv')

# Currently, the 'spatial' and 'subject' data are lists of string(s) represented as strings.
# This is inconvenient to work with, so let's turn them into true lists of strings

# Fill in empty cells with empty lists (represented as strings) for consistency 
df = df.replace(np.nan, "[\"None\"]", regex = True)

# Convert lists represented as strings into actual lists 
df['spatial'] = [eval(row) for row in df['spatial']]
df['subject'] = [eval(row) for row in df['subject']]

# Remove all non-alphabetic characters exceptfor standard punctuation: . , ! ? ' "
def clean_string(text):
    return re.sub(r'[^a-zA-Z\s.,!?\'"-]', '', text)

df['spatial'] = [[clean_string(word) for word in row] for row in df['spatial']]
df['subject'] = [[clean_string(word) for word in row] for row in df['subject']]

# Export
df.to_csv('{FILE-PATH}/data/cleaned_df.csv', index = False)