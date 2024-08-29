import pandas as pd

df = pd.read_csv('main.csv')

df_fraction = df.sample(frac = 0.2, random_state=1)

df_fraction.to_csv('fraction_of_the_main.csv', index=False)

