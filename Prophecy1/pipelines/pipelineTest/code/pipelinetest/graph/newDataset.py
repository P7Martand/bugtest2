from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipelinetest.config.ConfigStore import *
from pipelinetest.functions import *

def newDataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("col1", StringType(), True), StructField("customer_id", StringType(), True), StructField("c_config", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/tmp/auomation_csv/single_file.csv")
