import numpy as np
import pandas as pd

df = pd.DataFrame( {'first_name': {0: 'Tom', 1: float('nan'), 2: 'Hugh', 3: 'Oprah', 4: 'Emma'}, 'last_name': {0: 'Hanks', 1: float('nan'), 2: 'Jackman', 3: 'Winfrey', 4: 'Stone'}, 'age': {0: 63.0, 1: float('nan'), 2: 51.0, 3: 66.0, 4: 31.0}, 'sex': {0: 'm', 1: float('nan'), 2: 'm', 3: 'f', 4: 'f'}, 'pre_movie_score': {0: 8.0, 1: float('nan'), 2: float('nan'), 3: 6.0, 4: 7.0}, 'post_movie_score': {0: 10.0, 1: float('nan'), 2: float('nan'), 3: 8.0, 4: 9.0}} )
###############################################
print(80*'-')
print('Starting Missing Data')
print(80*'-')
###############################################
print(df.head())

# detect nulls
df.isnull() # returns boolean true false matrix with nulls being true
df.notnull() #opposite matrix to ^

# You can utilise the boolean output by looking at one col and using it for indexing into the df
df[df['pre_movie_score'].notnull()]







