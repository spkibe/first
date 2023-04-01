import pandas as pd
import pprint
import requests
request = requests.get('https://randomuser.me/api/?gender=male&results=100&inc=name,gender,email')
result = request.json()

result.keys()
df = pd.DataFrame.from_dict(result['results'])

df.head()

gender_mail = df[['gender', 'email']]

name_df = df['name'].apply(pd.Series)
#pprint.pprint(name_df.head)

names = name_df[['first', 'last']]

main_df = pd.concat([gender_mail, names], axis=1)

pprint.pprint(main_df.head())