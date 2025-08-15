from src.logger import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} started ..........")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} is completed!")
except Exception as e:
    logger.exception(e)
    raise e