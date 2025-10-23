from pyspark import SparkContext
# Instanciar a variável com o SparkContext() para poder utilizar mais de uma vez, pois só pode ser iniciado somente uma vez diretamente, sem ser por variável.
spark_contexto = SparkContext()
# Iniciando uma lista de elementos
lista = [1, 2, 3, 4, 5, 3]
# Transformando a lista em um RDD
lista_rdd = spark_contexto.parallelize(lista)
# Ação de contar os elementos do RDD
resul = lista_rdd.count()
print(resul)
# Função lambda que recebe um número e retorna um par formado pelo número e pelo mesmo número multiplicado por 10
par_ordenado = lambda numero: (numero, numero*10)
# Aplicando a transformação "flatMap" com a ação "collect"
resultado = lista_rdd.flatMap(par_ordenado).collect()
# Mostra o resultado
print(resultado)
# Aplicando a transformação "map" com a ação "collect"
result = lista_rdd.map(par_ordenado).collect()
# Mostra o resultado
print(result)
# fecha a seção
spark_contexto.stop