# Geocoding de locacion a coordenadas
# la API tiene como politica una consulta cada segundo, por lo que utilizo metodos para limitar las consultas de a un segundo

import pandas as pd
from geopy.geocoders import Nominatim
import time
from geopy.extra.rate_limiter import RateLimiter
import sqlite3

geolocator = Nominatim(user_agent='cctmexico')
df = pd.read_csv('location_clean.csv')
    # Cape Canaveral AFS, Florida, USA → Tipo de address que se debe utilizar


start = time.time()

geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df['Location'] = df['Location'].apply(geocode)
df['coordenadas'] = df['Location'].apply(lambda x: (x.latitude, x.longitude))


end = time.time()
elapsed = end - start


conn = sqlite3.connect('space_missions_insights.sqlite')
cur = conn.cursor()

df.to_sql('locations_to_coords', conn, if_exists='replace', index=False)
conn.close()

