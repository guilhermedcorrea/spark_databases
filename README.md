
#SPARK APP



```Python


if __name__=='__main__':
    conf = SparkConf()
    conf.set("spark.master","local[*]")
    conf.set("spark.executor.memory", "4g")
    conf.set("spark.driver.memory", "4g")
    conf.set("spark.sql.adaptive.enabled","true")
    conf.set("spark.sql.adaptive.localShuffleReader.enabled","true")
    conf.set("spark.dynamicAllocation.enabled", "false")
    conf.set("spark.sql.adaptive.optimizeSkewsInRebalancePartitions.enabled","true")
    conf.set("spark.sql.adaptive.skewJoin.enabled","true")
    conf.set("spark.sql.statistics.size.autoUpdate.enabled","true")
    conf.set("spark.sql.inMemoryColumnarStorage.compressed","true")
    conf.set("hive.exec.dynamic.partition", "true")
    conf.set("hive.exec.dynamic.partition.mode", "nonstrict")

    spark = SparkSession.builder\
            .config(conf=conf)\
            .getOrCreate()
```

<b>Spark Session</b>

```Python

df = spark.read.option("inferSchema",True) \
                 .options(header='True', inferSchema='True', delimiter=';') \
                .csv(r"/home/guilherme/docker-livy/code/apps/SEG_TIM_TREINAR_MODELO_V2_ABR_31-05_1_1.CSV")

df.createOrReplaceTempView("ProdutosView")

```

<b>Reader csv</b>



```Python

host = 'http://localhost:8998'
data = {'kind': 'spark'}
headers = {'Content-Type': 'application/json'}
r = requests.post(host + '/sessions', data=json.dumps(data), headers=headers)
r.json()
```


<b>Abrindo Sessao Livy</b>




```Python

data = {
  'code': textwrap.dedent("""
    import random
    NUM_SAMPLES = 100000
    def sample(p):
      x, y = random.random(), random.random()
      return 1 if x*x + y*y < 1 else 0

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
    print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
    """)
}

r = requests.post(statements_url, data=json.dumps(data), headers=headers)
pprint.pprint(r.json())



```


<b>Enviand Codigo Python para o Cluster</b>