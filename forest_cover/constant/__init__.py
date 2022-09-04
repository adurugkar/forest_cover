import imp


import os
from datetime import datetime

from app import ROOT_DIR

def get_current_time_stamp():
    date_time = datetime.now()
    return f"{date_time.strftime('%Y-%m-%d-%H-%M-%S')}"

#config file path
ROOT_DIR = os.getcwd()
CONFIG_DIR = 'config'
CONFIG_FILE_NAME = 'config.yaml'
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

#current_Time_stamp
CURRENT_TIME_STAMP = get_current_time_stamp()

# Training pipline relatted variable
TRANING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRANING_PIPELINE_NAME_KEY = 'pipeline_name'
TRANING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'

# Data Ingestion related variable

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"