import pandas as pd

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
concat = pd.concat([s1, s2], axis=1)

print("\n------DATA FRAME 1------\n")
print(s1)

print("\n------DATA FRAME 2------\n")
print(s2)

print("\n------CONCAT DF 1 AND DF 2------\n")
print(concat)


print("\n------DATA FRAME 3------\n")
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 5]})
# # Replace the name of column lkey for key
# df1_rename = df1.rename(columns={'lkey': 'key'})
print(df1)

print("\n------DATA FRAME 4------\n")
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})
# # Replace the name of column rkey for key
# df2_rename = df2.rename(columns={'rkey': 'key'})
print(df2)

print("\n---------MERGE DF 3 AND DF 4---------\n")
## Dealing with columns of the same name
# merge = df1_rename.merge(df2_rename, on='key', suffixes=("_left", "_right"))
merge = df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=("_left", "_right"))
print(merge)


print("\n------DATA FRAME 5------\n")
df_vendas = pd.DataFrame({'Vendas': [100, 200, 50]}, index=['P1', 'P2', 'P3'])
print(df_vendas)

print("\n------DATA FRAME 6------\n")
df_estoque = pd.DataFrame({'Estoque': [500, 300, 100, 800]}, index=['P1', 'P2', 'P3', 'P4'])
print(df_estoque)

print("\n---JOIN Index-on-Index---\n")
# O join é instantâneo e limpo
join = df_vendas.join(df_estoque, how='left')
print(join)