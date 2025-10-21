import pandas as pd
from sklearn.datasets import load_iris

print("\n----------------------------DATA FRAME------------------------------------\n")
data = load_iris()
iris_df = pd.DataFrame(data.data, columns=data.feature_names)
iris_df['encoded_target'] = data.target

# Replaces (cm) with empty, that is, eliminate (cm). Also replaces space with underline.
iris_df.columns = [c.replace("(cm)", "").rstrip().replace(" ", "_") for c in iris_df.columns]
print(iris_df)

print("\n------------------------SHOW COLUMNS------------------------------\n")
print(iris_df.columns)

print("\n---------------------SHOW INFO---------------------------\n")
print(iris_df.info())

print("\n-------------------------------SHOW DESCRIBE--------------------------------\n")
print(iris_df.describe())

print("\n---------------------SHOW FIRST LINE---------------------------\n")
print(iris_df.loc[0])

print("\n------SHOW ONLY INDEX MEAN OF DESCRIBE------\n")
print(iris_df.describe().loc['mean'])

print("\n------SHOW ONLY THE INDEX IN THE SECOND POSITION OF THE DF------\n")
print(iris_df.iloc[1])

print("\n------SHOW ONLY THE CELL OF THE DF------\n")
print(iris_df.iloc[1, 2])

print("\n-----------------------SHOW DF WITHOUT INDEX 0-----------------------------\n")
drop = iris_df.drop([0])
print(drop)

print("\n-----------------------SHOW DF WITHOUT THE INDEX WHERE SEPAL LENGTH >= 4.5-----------------------------\n")
drop_query = iris_df.drop(iris_df.query("sepal_length >= 4.5").index)
print(drop_query)

print("\n----------------------------------RESET INDEX--------------------------------\n")
reset_index = iris_df.drop(iris_df.query("sepal_length >= 4.5").index).reset_index()
reset_index = reset_index.drop(columns=['index'])
print(reset_index)


print("\n-----------------------SHOW DF WITH NEW COLUMN 'SPECIE'-----------------------------\n")
target_names = data.target_names
def map_specie(x):
    return target_names[x]

iris_df['especie'] = iris_df['encoded_target'].apply(lambda x: map_specie(x))
print(iris_df)