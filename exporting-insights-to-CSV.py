import sqlite3
import pandas as pd

# Conecta a la base de datos SQLite
conn = sqlite3.connect('space_missions_insights.sqlite')

# Lista de nombres de tablas que deseas exportar
tables_to_export = ['Act_Ret_rockets','companies_country','gral_rockt_info','launches_per_year','ratios','top5_launc_loc',
                    'top_suc_mission','top_uns_mission','total_launches_country']

# Crea un DataFrame para cada tabla y concaténalos en uno solo
for table in tables_to_export:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    df.to_csv(f'Insights CSV/{table}.csv')


# Cierra la conexión a la base de datos
conn.close()