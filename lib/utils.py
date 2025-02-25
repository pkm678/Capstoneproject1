from pyspark.sql import SparkSession


def get_spark_session(env):
    if env == "local":
        return SparkSession \
            .builder \
            .config('spark.driver.extraJavaOptions',
                    '-Dlog4j.configuration=file:log4j.properties') \
            .master("local[3]") \
            .enableHiveSupport() \
            .appName("capstone_project") \
            .getOrCreate()
    else:
        return SparkSession \
            .builder \
            .enableHiveSupport() \
            .appName("capstone_project") \
            .getOrCreate()
