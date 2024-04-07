import numpy as np
import sys
import pandas as pd

from typing import Optional

from us_visa_prediction.configuration.mongo_db_connection import MongoDBclient
from us_visa_prediction.constant import DATABASE_NAME
from us_visa_prediction.exception import USvisaException

class USvisaData:
    """
    This class is to export the mongodb records to dataframe (we are converting dictonary format to dataframe) 
    because mongodb will store the data in json format
    """

    def __init__(self):

        try:
            self.mongo_client = MongoDBclient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)
        
    def export_collection_as_dataframe(self, collection_name, database_name:Optional[str]=None)-> pd.DataFrame:
        try:
            """
            exporting the entire collections as dataframe
            returning pd.Datafram of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df.drop(columns=["_id"], axis = 1, inplace=True)
            df.replace({"na":np.nan}, inplace = True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)