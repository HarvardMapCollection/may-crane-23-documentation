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

# Explores description column of metadata 

# Imports 
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Read all-metadata.csv 
df = pd.read_csv('{FILE-PATH}/full_df.csv')

# Print average length in characters
print(np.mean([len(desc) for desc in df['description']]))

# Print average length in words
print(np.mean([len(desc.split()) for desc in df['description']]))

# Print longest length in words
print(np.max([len(desc.split()) for desc in df['description']]))

# Print shortest length in words
print(np.min([len(desc.split()) for desc in df['description']]))

# Word count plot
word_counts = Counter([string for string in [len(desc.split()) for desc in df['description']]])
top_1000 = word_counts.most_common(1000)

# Extract the keys and counts
top_keys = [key for key, _ in top_1000]
top_values = [value for _, value in top_1000]

fig = plt.figure()
plt.bar(top_keys, top_values)
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.title("\"Description\" Word Count")
fig.savefig("wordcount.png", dpi = fig.dpi)

# Top 20 shortest
df_sorted = df.sort_values(by='description', key=lambda x: x.str.len())
top_20_shortest = df_sorted.head(20)
print(top_20_shortest)

# Top 20 longest
df_sorted_otherway = df.sort_values(by='description', key=lambda x: x.str.len(), ascending = False)
top_20_longest = df_sorted_otherway.head(20)
print(top_20_longest)
