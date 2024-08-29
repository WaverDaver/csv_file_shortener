import pandas as pd

df = pd.read_csv('quotes.csv')

df_fraction = df.sample(frac = 0.2, random_state=1)

df_fraction.to_csv('quotes_smaller_file.csv', index=False)

