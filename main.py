from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseMOdelTrainingPipeline
from cnnClassifier.pipeline.stage03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04_evaluation import EvaluationPipeline
from cnnClassifier.utils.common import logger

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>>>> STAGE {STAGE_NAME} started... <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    raise e

STAGE_NAME = "Prepare Base Model"


try:
    logger.info(f">>>>>>> STAGE {STAGE_NAME} started... <<<<<<<")
    prepare_base_model = PrepareBaseMOdelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f"*********************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")

except Exception as e:
    raise e

STAGE_NAME = "Evaluation"

try:
    logger.info(f"*********************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(
        f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e
