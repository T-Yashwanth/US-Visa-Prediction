import sys
from us_visa_prediction.pipeline.train_pipeline import TrainPipeline
from us_visa_prediction.exception import USvisaException

pipline = TrainPipeline()

pipline.run_pipeline()
