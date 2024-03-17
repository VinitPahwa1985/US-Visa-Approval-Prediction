from us_visa.logger import logging
from us_visa.pipeline.training_pipeline import TrainPipeline

logging.info("Exporting data from mongodb")



pipline  = TrainPipeline()
pipline.run_pipeline()
