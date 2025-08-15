import os
from src.logger import logger
from src.entity.config_entity import DataIngestionConfig
from datasets import load_dataset


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) :
        self.config = config
    
    def load_data(self):
        ds = load_dataset("knkarthick/samsum")
        
        ds.save_to_disk(os.path.join(self.config.local_data_path,"saved_samsum_dataset"))
        
        for split, dataset in ds.items():
            filepath = os.path.join(self.config.local_data_path, f"{split}.csv")
            dataset.to_csv(filepath)
            logger.info(f"Saved {split} data to {filepath}")
        logger.info("Dataset loaded")