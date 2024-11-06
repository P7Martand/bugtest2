from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipelinetest.config.ConfigStore import *
from pipelinetest.functions import *

def newDataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("jdbc")\
        .option("url", "")\
        .option("user", "")\
        .option("password", "")\
        .option("dbtable", None)\
        .option("pushDownPredicate", True)\
        .option("driver", "")\
        .load()
