from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.utils.common import logger

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>> STAGE {STAGE_NAME} started... <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    raise e
