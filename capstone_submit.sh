spark-submit --master yarn --deploy-mode cluster\
--py-files capstoone_lib.zip\
--files conf/Capstoneproject1.conf, conf/spark.conf, log4j.properties\
main.py qa 2022-08-02