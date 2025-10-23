from pyspark import SparkContext
import numpy as np

spark_contexto = SparkContext()

vetor = np.array([10, 20, 30, 40, 50])

paralelo = spark_contexto.parallelize(vetor)

print(paralelo)

mapa = paralelo.map(lambda x : x**2+x)

# Deixa o resultado sem o "np.int64"
resultado_limpo = [int(x) for x in mapa.collect()]

print(resultado_limpo)

# EXEMPLO 2 (Método mais simples que o Count_words)

paralelo = spark_contexto.parallelize(["distribuida", "distribuida", "spark", "rdd", "spark", "spark"])

funcao_lambda = lambda x:(x, 1)

from operator import add

mapa = paralelo.map(funcao_lambda).reduceByKey(add).collect()

for (w, c) in mapa:
    print("{}: {}".format(w, c))

spark_contexto.stop()