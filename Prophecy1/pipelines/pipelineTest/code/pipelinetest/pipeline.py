from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipelinetest.config.ConfigStore import *
from pipelinetest.functions import *
from prophecy.utils import *
from pipelinetest.graph import *

def pipeline(spark: SparkSession) -> None:
    df_newDataset = newDataset(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipelineTest")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipelineTest")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipelineTest", config = Config)(pipeline)

if __name__ == "__main__":
    main()
