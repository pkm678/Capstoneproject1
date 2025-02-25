import sys

from lib import utils

from lib.logger import Log4j

if __name__ == "__main__":

    if(len(sys.argv) < 3):
        print("Usage: this project {local, qa, prod} {load_date}: Arguments Missing")
        sys.exit(1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = utils.get_spark_session(job_run_env)
    logger = Log4j(spark)

    logger.info("Finished the spark session")
    logger.warn("Finished the spark session")