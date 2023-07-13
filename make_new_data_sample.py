
import pandas as pd

df = pd.read_csv('data/raw/train.csv')
sample_df = df.sample(n=1000, random_state=1234)
sample_df.to_csv('data/raw/train_new.csv', sep=',', index = False)
