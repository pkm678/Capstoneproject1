class Log4j:
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        # conf = spark.sparkContext.getConf()
        # app_name = conf.get("spark.app.name")
        root_class = "Capstoneproject1"
        self.logger = log4j.LogManager.getLogger(root_class )

    def warn(self, msg):
        self.logger.warn(msg)

    def info(self, msg):
        self.logger.info(msg)


    def error(self, msg):
        self.logger.error(msg)


    def debug(self, msg):
        self.logger.debug(msg)
