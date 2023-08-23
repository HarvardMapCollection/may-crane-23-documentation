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

# Imports 
import pandas as pd
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderUnavailable

# Read all-metadata.csv 
df = pd.read_csv('{FILE-PATH}/cleaned_df.csv')

# US States
states_abbs = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

states_pairs = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

states = [states_pairs.get(state) for state in states_abbs]

# Create a geocoder object with API key
api_key = '{API-KEY}'
geolocator = GoogleV3(api_key = api_key)

# Make calls to geolocator for each entry in 'spatial' to get the full location data
def get_location(loc):
    try:
        print(loc)
        location = geolocator.geocode(loc)
        if location is not None:
            return location.raw.get("formatted_address").split(",")
        else:
            return 'Geocoding information not found'
    except GeocoderTimedOut:
        time.sleep(5)  # Delay for 5 second before retry
        return get_location(loc)
    except GeocoderUnavailable:
        time.sleep(5)  # Delay for 5 second before retry
        return get_location(loc)  

# Apply the get_location function to each row of the DataFrame
location = df.apply(lambda row: get_location(row['spatial'][0]), axis = 1)

# Display the updated DataFrame
print(location)

# Export
df.to_csv('{FILE-PATH}/data/full_df.csv', index = False)