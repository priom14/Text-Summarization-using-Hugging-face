from src.components.data_transformation import DataTransformation
from src.config.configuration import ConfigurationManager
from src.logger import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transforamtion = DataTransformation(config=data_transformation_config)
        
        data_transforamtion.convert()
        
        