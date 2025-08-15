from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                 config_path = CONFIG_FILE_PATH,
                 params_filepath = PARAMSS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.parmas = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            local_data_path = config.local_data_path
        )
        
        return data_ingestion_config