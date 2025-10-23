import pandas as pd
import numpy as np

print("\n-----DATAFRAME------\n")
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'], 'Max Speed': [380., 370., 24., 26.]})
print(df)

print("\n-----GROUP BY------\n")
grouped = df.groupby(['Animal'])
print(grouped.mean())


print("\n-----DATAFRAME------\n")
df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df)

print("\n-----APPLY 1------\n")
df.apply(np.sqrt)
df['A'] = df['A'].apply(lambda x: x + 1)
print(df)

print("\n-----APPLY 2------\n")
df['C'] = df.apply(lambda x: x['A'] + x['B'], axis=1)
print(df)