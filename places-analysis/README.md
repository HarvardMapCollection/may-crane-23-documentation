# All scripts

`all-jsons.py` retrieves all data fields from the Harvard Geospatial Library (HGL) [metadata .json files](https://github.com/harvard-library/harvard-geodata/tree/main/json) and makes one master pandas dataframe and exports it as all_metadata.csv.

`all-jsons.py` was adapted from Belle Lipton's [get-jsons.py](https://github.com/HarvardMapCollection/hgl-explr/blob/main/scripts/get-jsons.py), which retrieved select data fields from the metadata .json files.

Using all_metadata.csv, I did some exploratory data analysis in `exploratory.ipynb`.

I took these insights and worked in `cleaning.py` to clean the data in all_metadata.csv and export it as cleaned_df.csv.

`spatial_levels.py` uses the [Google geocode API](https://developers.google.com/maps/documentation/geocoding/overview) to match the existing data for 'spatial' to the full description (city, state, country, continent) available online. The resulting dataframe is exported out as full_df.csv.

`visualizations.py` makes use of full_df.csv to create simple visualizations of the spatial metadata available at the HGL.

# Documentation instructions
*With each big step, explain the why of functions and decisions. Ensure anyone interested in replication/learning can understand and do.*

First, I pulled all available data fields from the GBL .json files using `all-jsons.py`. I did a little bit of exploration and investigation into the formatting of the spatial field in our original metadata with `exploratory.ipynb`. Then, I cleaned the data using `cleaning.py` to have standardized alphabetic and punctuation strings in lists. Next, I expanded the 'spatial' field in `spatial_levels.py` by pulling in more corresponding data about city, state, country, and continent. Lastly, I made visualizations in `visualizations.py` using all our cleaned data.