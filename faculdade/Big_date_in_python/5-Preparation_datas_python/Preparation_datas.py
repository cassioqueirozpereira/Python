import pandas as pd
from sklearn.datasets import load_iris
import numpy as np
from sklearn.preprocessing import MinMaxScaler

example1 = pd.read_csv('../4-Base_python/ordf.csv')
print("\n---------------------SHOW EXAMPLE---------------------------\n")
print(example1)

print("\n-------------------------------------SHOW DATAFRAME EXAMPLE-------------------------------------\n")
data = load_iris()

iris_df = pd.DataFrame(data.data, columns=data.feature_names)

iris_df['encoded_target'] = data.target
print(iris_df)

print("\n-------------------------------------SHOW DATAFRAME EXAMPLE WITH NONE VALUES, IMPOSSIBLE VALUES AND STRING VALUES-------------------------------------\n")
iris_df.iloc[0, 0] = None
iris_df.iloc[0, 1] = None
iris_df.iloc[0, 2] = None
iris_df.iloc[1, 0] = None
iris_df.iloc[4, 3] = None
iris_df.iloc[3, 3] = -999999999999999999
iris_df.iloc[149, 2] = "cwevawevberbqb"
print(iris_df)

print("\n-------------------------------------SHOW 'ISNA' = TRUE AND ISNOTNAN = FALSE-------------------------------------\n")
print(iris_df.isna())

print("\n-------------------------------------SHOW ONLY THE LINES WITH NONE VALUES-------------------------------------\n")
lines_isna = iris_df[iris_df.isna().any(axis=1)]
print(lines_isna)

print("\n-------------------------------------SHOW ONLY THE LINES WITH VALUES-------------------------------------\n")
iris_df_rem = iris_df.dropna()
print(iris_df_rem)

print("\n-------------------------------------REPLACE NAN WITH MEAN VALUE-------------------------------------\n")
# There are three ways to do it
iris_df_mean = iris_df.fillna(iris_df.mean(numeric_only=True)) # replace with mean. Although, since a column has "float" and "string", this NAN isnt replace
print(iris_df_mean)

print("\n-------------------------------------REPLACE NAN WITH ZERO VALUE-------------------------------------\n")
iris_df_zero = iris_df.fillna(0) # replace with zero
print(iris_df_zero)

print("\n-------------------------------------REPLACE NAN WITH IMPOSSIBLE VALUE-------------------------------------\n")
iris_df_values_impossible = iris_df.fillna(-999) # replace with impossible values
print(iris_df_values_impossible)

print("\n-------------------------------------IDENTIFYING CORRUPTED DATA-------------------------------------\n")
iris_df = iris_df_zero
print(iris_df.info())
# Temos tbm o describe que resulta na descrição de estatísticas bem básicas, por exemplo, a contagem de cada coluna (count), quantos valores únicos de cada variável (unique) e quantas categorias, bem como o primeiro registro (top) e a frequência (freq.).

print(iris_df['petal length (cm)'].unique()) # unique() mostra somente os dados sem repetições do mesmo.

print("\n-------------------------------------DEALING WITH CORRUPTED DATA-------------------------------------\n")
iris_df = iris_df[iris_df['petal length (cm)'] != 'cwevawevberbqb'].reset_index(drop=True)
print(iris_df)

print("\n-------------------------------------IDENTIFYING POINTS OUTSIDE THE CURVE-------------------------------------\n")
print(iris_df['petal width (cm)'].unique())
iris_df = iris_df[iris_df['petal width (cm)'] != -1.0e+18].reset_index(drop=True)
print(iris_df)

print("\n-------------------------------------ADDING IRREGULAR DATA-------------------------------------\n")
iris_df['artificial'] = np.random.uniform(100, 1000, iris_df.shape[0]).round(2)
print(iris_df)

print("\n-------------------------------------REGUALIZING DATA-------------------------------------\n")
scaler = MinMaxScaler()
scaler.fit(iris_df)
novo_iris_df = scaler.transform(iris_df)
novo_iris_df = pd.DataFrame(novo_iris_df, columns=iris_df.columns).round(2)
print(novo_iris_df)

print("\n-------------------------------------SHOW UNIQUE COLUMN VALUE 'encoded_target'-------------------------------------\n")
encoded_target = novo_iris_df['encoded_target'].unique()
print(encoded_target)

print("\n-------------------------------------SHOW UNIQUE COLUMN VALUE 'petal width (cm)'-------------------------------------\n")
petal_width = novo_iris_df['petal width (cm)'].unique()
print(petal_width)

print("\n-------------------------------------SHOW UNIQUE COLUMN VALUE 'artificial'-------------------------------------\n")
artificial = novo_iris_df['artificial'].unique()
print(artificial)