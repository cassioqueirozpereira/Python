import pandas as pd

df = pd.DataFrame({'a': range(1, 6), 'b': range(10, 0, -2), 'c': range(10, 5, -1)})

print("\n--------SHOW DATAFRAME-------\n")
print(df)

print("\n--------SHOW INDEX WHERE A > B-------\n")
print(df.query('a > b'))

print("\n--------SHOW INDEX WHERE B == C-------\n")
print(df.query('b == `c`'))

print("\n--------SHOW INDEX WHERE A > B WITHOUT QUERY-------\n")
print(df[df.a > df.b])

df.drop(columns=['a', 'b'], inplace=True)

print("\n--------SHOW DATAFRAME WITHOUT A AND B-------\n")
print(df)

df.drop(index=[1, 3], inplace=True)

print("\n--------SHOW DATAFRAME WITHOUT INDEX 1 AND 3-------\n")
print(df)

df = df.reset_index(drop=True, inplace=False)

print("\n--------SHOW DATAFRAME WITH REINDEXING-------\n")
print(df)