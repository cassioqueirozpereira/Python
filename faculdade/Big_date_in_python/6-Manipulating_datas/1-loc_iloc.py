import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])

print("\n--------SHOW DATAFRAME-------\n")
print(df)

print("\n--------SHOW INDEX VIPER-------\n")
print(df.loc['viper'])

print("\n--------SHOW INDEX VIPER AND SIDEWINDER-------\n")
print(df.loc[['viper', 'sidewinder']])

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4}, {'a': 100, 'b': 200, 'c': 300, 'd': 400}, {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]

df = pd.DataFrame(mydict)

print("\n--------SHOW DATAFRAME-------\n")
print(df)

print("\n--------SHOW COLUMN ZERO-------\n")
print(df.iloc[0])

print("\n--------SHOW INDEX ZERO-------\n")
print(df.iloc[[0]])

print("\n--------SHOW INDEX ZERO AND ONE-------\n")
print(df.iloc[[0, 1]])

print("\n--------SHOW THE THREE FIRST INDEX-------\n")
print(df.iloc[:3])

print("\n--------SHOW ONLY THE INDEX WITH EVEN NUMBER-------\n")
print(df.iloc[lambda x: x.index % 2 == 0])

print("\n--------SHOW INDEX [0, 2] AND COLUMN [1, 3]-------\n")
print(df.iloc[[0, 2], [1, 3]])

print("\n--------SHOW INDEX [1 ATÉ O 2] AND COLUMN [0 ATÉ O 2]-------\n")
print(df.iloc[1:3, 0:3])