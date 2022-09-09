import pandas as pd
import requests as res
uri = 'https://data.nationalgrideso.com/api/3/action/datastore_search?resource_id=ddc4afde-d2bd-424d-891c-56ad49c13d1a'

data = res.get(uri).json()
df = pd.read_json(uri,orient='records')

for index, row in df.iterrows():
    print(df['help'])