from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

data = [('John', 28), ('Anna', 24), ('Mike', 35)]
columns = ['Name', 'Age']
df = spark.createDataFrame(data, columns)

df.show()

df_filtered = df.filter(df.Age > 30)
df_filtered.show()

spark.stop()

