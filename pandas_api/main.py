import json
import pandas as pd
import requests

api_json = requests.get('https://jsonplaceholder.typicode.com/users')
api_data=json.loads(api_json.text)

normalize = pd.json_normalize(api_data, meta=['name', 'username', 'email',['address', 'street'], ['address', 'suite'],
                                         ['addres', 'city'], ['address', 'zipcode'], ['address', 'geo'], 'phone',
                                         'website', 'company'])
normalize.to_csv(r'/Users/chandler/PycharmProjects/pandassql/test.csv', index=False)


