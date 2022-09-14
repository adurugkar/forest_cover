from collections import namedtuple
from datetime import datetime
import uuid
from forest_cover.component import data_ingestion
from forest_cover.config.configuration import Configuration
from forest_cover.logger import logging , get_log_file_name
from forest_cover.exception import ForestException
from threading import Thread
from typing import List
from multiprocessing import Process
from forest_cover.entity.artifact_entity import  *
from forest_cover.entity.config_entity import *
from forest_cover.component.data_ingestion import DataIngestion
from forest_cover.component.data_validation import DataValidation
from forest_cover.component.data_transformation import DataTransformation
import os, sys
import  pandas as pd

Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
                                       "running_status", "start_time", "stop_time", "execution_time", "message",
                                       "experiment_file_path", "accuracy", "is_model_accepted"])



class Pipelin(Thread):
    experiment: Experiment = Experiment(*([None]*11))
    experiment_file_path = None

    def __init__(self, config: Configuration) -> None:
        try:
            os.makedirs(config.training_pipline_config.artifact_dir, exist_ok=True)
            Pipelin.experiment_file_path=os.path.join(config.training_pipline_config.artifact_dir, EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(deamon=False, name="pipeline")
            self.config = config
        except Exception as e:
            raise ForestException(e,sys) from e

    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiarte_data_ingestion()
        except Exception as e:
            raise ForestException(e,sys) from e



