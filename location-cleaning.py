import pandas as pd
import re
import sqlite3


df = pd.read_csv('space_missions_normalized.csv')

# Define una función para eliminar la parte no deseada de las direcciones
def clean_address(address):
    cleaned_address = re.sub(r'^[^,]+,\s', '', address)
    return cleaned_address

# Aplica la función a la columna 'direcc' del DataFrame
df['Location'] = df['Location'].apply(clean_address)


df['Location'].to_csv('location_clean.csv', index=False)






# conn = sqlite3.connect('space_missions_insights.sqlite')
# cur = conn.cursor()

# df.to_sql('locations_to_coords', conn, if_exists='replace', index=False)
# conn.close()

