import pandas as pd
from sklearn.datasets import load_iris
import plotly.express as px

data = load_iris()
iris_df = pd.DataFrame(data.data, columns=data.feature_names)
iris_df['encoded_target'] = data.target
target_names = data.target_names
def map_specie(x):
    return target_names[x]

# Adiciona a coluna 'especie' ao iris_df
iris_df['especie'] = iris_df['encoded_target'].apply(lambda x: map_specie(x))

df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
fig.show()

fig = px.histogram(
    iris_df,
    x = "petal length (cm)",
    title = "Dados Numéricos - Histograma"
)
fig.show()

fig = px.scatter(
    iris_df,
    x = "petal length (cm)",
    y = "petal width (cm)",
    color = "especie",
    title = "Dados Numéricos - Gráfico de Dispersão"
)
fig.show()

long_df = px.data.medals_long()
fig = px.bar(
    long_df,
    x="nation",
    y="count",
    color="medal",
    title="Dados Categóricos - Gráfico de Barras"
)
fig.show()
print(long_df)

df = px.data.tips()
fig = px.pie(
    df,
    values="tip",
    names="day",
    title="Dados Categóricos - Gráfico de Pizza/Torta"
)
fig.show()

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(
    df,
    x="year",
    y="lifeExp",
    color="country",
    title="Dados Numéricos - Gráfico de Linha"
)
fig.show()

df = px.data.iris()
fig = px.scatter_3d(
    df,
    x="sepal_length",
    y="sepal_width",
    z="petal_width",
    color="species",
    size="petal_length",
    size_max=18,
    symbol="species",
    opacity=0.7,
    title="Dados Numéricos - Gráfico de Dispersão 3D"
)
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

fig.show()