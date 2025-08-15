import os
from src.logger import logger
from datasets import load_from_disk
from transformers import AutoTokenizer
from src.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
        
    def convert_examples_to_feature(self, example_batch):
        dialogues = [str(d) if d is not None else "" for d in example_batch['dialogue']]
        summaries = [str(s) if s is not None else "" for s in example_batch['summary']]
        input_encodings = self.tokenizer(dialogues, max_length =  1024, truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(summaries, max_length = 128, truncation = True)
        
        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encoding['input_ids'] 
        }
        
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_feature, batched= True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))