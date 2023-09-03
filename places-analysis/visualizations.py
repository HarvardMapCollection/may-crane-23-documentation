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

# Makes visualizations!

# Imports 
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Read full_df.csv 
df = pd.read_csv('{FILE-PATH}/full_df.csv')

# Top 15 visualization
## Get counts
spatial_counts = Counter([string for sublist in df['spatial'] for string in sublist])
top_15 = spatial_counts.most_common(15)

## Extract the keys and counts
top_keys = [key for key, _ in top_15]
top_values = [value for _, value in top_15]

## Create bar plot with the top 15 counts
fig = plt.figure(figsize = (8, 8))
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys, top_values)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.title('Top 15 Places')
plt.savefig('top15.png')

# Top 15 visualization - GeoTIFF
## Get counts
spatial_counts_geotiff = Counter([string for sublist in df[df['format'] == "GeoTIFF"]['spatial'] for string in sublist])
top_15_geotiff = spatial_counts_geotiff.most_common(15)

## Extract the keys and counts
top_keys_geotiff = [key for key, _ in top_15_geotiff]
top_values_geotiff = [value for _, value in top_15_geotiff]

## Create bar plot with the top 15 counts
fig = plt.figure(figsize = (8, 8))
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys_geotiff, top_values_geotiff)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.title('Top 15 Places - GeoTIFF Format')
plt.savefig('top15_geotiff.png')

# Top 15 visualization - Shapefile
## Get counts
spatial_counts_shapefile = Counter([string for sublist in df[df['format'] == "Shapefile"]['spatial'] for string in sublist])
top_15_shapefile = spatial_counts_shapefile.most_common(15)

## Extract the keys and counts
top_keys_shapefile = [key for key, _ in top_15_shapefile]
top_values_shapefile = [value for _, value in top_15_shapefile]

## Create bar plot with the top 15 counts
fig = plt.figure(figsize = (8, 8))
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys_shapefile, top_values_shapefile)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.title('Top 15 Places - Shapefile Format')
plt.savefig('top15_shapefile.png')

# Top places by format
## Look at places with at least 150 count
trim_threshold = 150
trimmed_spatial_shapefile = Counter({key: count for key, count in spatial_counts_shapefile.items() if count > trim_threshold})
sorted_spatial_shapefile = sorted(trimmed_spatial_shapefile.items(), key=lambda x: x[1], reverse=True)
trimmed_spatial_geotiff = Counter({key: count for key, count in spatial_counts_geotiff.items() if count > trim_threshold})
sorted_spatial_geotiff = sorted(trimmed_spatial_geotiff.items(), key=lambda x: x[1], reverse=True)

df_trimmed = pd.DataFrame([trimmed_spatial_shapefile, trimmed_spatial_geotiff]).T.reset_index()
df_trimmed.columns = ["Place", "Shapefile Count", "GeoTIFF Count"]

## Plot
fig = plt.figure(figsize = (30, 30))
fig.clf()

ax = df_try.plot(x='Place', kind = 'bar', stacked = False, title = 'Top Places - By Format')
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.savefig('top_by_format.png')
plt.show()

# Wordcloud!
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(spatial_counts)

plt.figure(figsize = (15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig('wordcloud.png')

# Top 15 states
state_counts = Counter([string for string in df[df['state'] != "None"]['state']])
top_15 = state_counts.most_common(15)
top_keys = [key for key, _ in top_15]
top_values = [value for _, value in top_15]

fig = plt.figure(figsize = (8, 8))
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys, top_values)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.tight_layout()
plt.title('Top 15 States')
plt.savefig('states.png')

# Top 15 countries
country_counts = Counter([string for string in df[df['country'] != "None"]['country']])
top_15 = country_counts.most_common(15)
top_keys = [key for key, _ in top_15]
top_values = [value for _, value in top_15]

fig = plt.figure()
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys, top_values)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.title('Top 15 Countries')
plt.tight_layout()
plt.savefig('countries.png')
plt.tight_layout()

# Top continents
cont_counts = Counter([string for string in df[df['continent'] != "None"]['continent']])
top_15 = cont_counts.most_common(15)
top_keys = [key for key, _ in top_15]
top_values = [value for _, value in top_15]

fig = plt.figure()
fig.clf()
ax = fig.add_subplot(111)
plt.bar(top_keys, top_values)
plt.setp(ax.get_xticklabels(), rotation = 45, horizontalalignment='right', fontsize='x-small')
plt.title('Top Continents')
plt.tight_layout()
plt.savefig('continents.png')
plt.tight_layout()
