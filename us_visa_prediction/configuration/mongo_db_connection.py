import os
import sys
import pymongo
from us_visa_prediction.constant import *
from us_visa_prediction.logger import logging
from us_visa_prediction.exception import USvisaException
import certifi

ca = certifi.where()

class MongoDBclient:
    """
    class Name:     export_daa_into_feature_store
    Description:    This method exports the dataframe from mongodb feature store as dataframe
    output:         connection to mongodb database
    on failure:     raise exception
    """
    client = None

    def __init__(self, database_name = DATABASE_NAME)-> None:
        try:
            if MongoDBclient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBclient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBclient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection Successfull")
        except Exception as e:
            raise USvisaException(e, sys)

