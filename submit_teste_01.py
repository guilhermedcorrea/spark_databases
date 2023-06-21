
from os.path import abspath
import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkContext, SparkConf



def retorna_spark_session():
   
    spark = SparkSession \
        .builder \
        .appName("Analytics") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    return spark



def reader_csv() -> None:
    spark = retorna_spark_session()

    df = spark.read.option("inferSchema",True) \
                 .options(header='True', inferSchema='True', delimiter=';') \
                .csv(r"/home/guilherme/docker-livy/code/apps/SEG_TIM_TREINAR_MODELO_V2_ABR_31-05_1_1.CSV")
    

    print(df.show(10))

    df.createOrReplaceTempView("ProdutosView")
    print(df)
    