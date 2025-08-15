from src.logger import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started ..........")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} is completed!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transforamtion Stage"

try:
    logger.info(f"{STAGE_NAME} started ..........")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} is completed!")
except Exception as e:
    logger.exception(e)
    raise e