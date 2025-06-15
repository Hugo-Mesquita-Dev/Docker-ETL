from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ETL_Loja_Docker") \
    .getOrCreate()

# Extração
df_vendas = spark.read.csv("/app/data/input/vendas_2023.csv", header=True, inferSchema=True)
df_produtos = spark.read.json("/app/data/input/produtos.json")

# Transformação
df_vendas = df_vendas.withColumn("data", to_date("data", "yyyy-MM-dd"))
df_final = df_vendas.join(df_produtos, "id_produto")

# Carregamento
df_final.write.parquet("/app/data/output/vendas_processadas.parquet")
print("ETL concluído! Resultados em /app/data/output/")

# Adicione após o processamento
df_final.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/vendas_db") \
    .option("dbtable", "vendas") \
    .option("user", "postgres") \
    .option("password", "senha123") \
    .mode("overwrite") \
    .save()