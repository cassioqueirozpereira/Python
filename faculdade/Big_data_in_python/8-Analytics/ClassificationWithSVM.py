import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

data = load_iris()
iris_df = pd.DataFrame(data.data, columns=data.feature_names)
iris_df['encoded_target'] = data.target
target_names = data.target_names
def map_specie(x):
    return target_names[x]

# Adiciona a coluna 'especie' ao iris_df
iris_df['especie'] = iris_df['encoded_target'].apply(lambda x: map_specie(x))