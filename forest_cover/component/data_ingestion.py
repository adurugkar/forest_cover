from ast import For
from curses import raw
from distutils.command.check import HAS_DOCUTILS
import sys , os
import forest_cover
from forest_cover.exception import ForestException
from forest_cover.logger import logging
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from forest_cover.entity.artifact_entity import DataIngestionArtifact
from forest_cover.entity.config_entity import DataIngestionConfig
from forest_cover.constant import *

class DataIngestion:
    
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion log started. {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ForestException(e,sys) from e

    def download_forest_cover_data(self)->str:
        try:
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            os.makedirs(tgz_download_dir, exist_ok=True)

            forest_cover_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir, forest_cover_file_name)

            logging.info(f"Downloading file from : [{download_url}] into : [{tgz_file_path}]")
            urllib.request.urlrentrieve(download_url,tgz_file_path)
            logging.info(f"File : [{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path
        except Exception as e:
            raise ForestException(e,sys) from e

    
    def extract_tgz_file(self, tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir, exist_ok=True)

            logging.info(f"Extracting tgz file : [{tgz_file_path}] into dir : [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as forest_cover_file_obj:
                forest_cover_file_obj.extract(path = raw_data_dir)
            logging.info(f"Extraction completed")
        except Exception as e:
            raise ForestException(e,sys) from e

    
    def split_data_as_train_test(self)-> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            forest_cover_file_path = os.path.join(raw_data_dir, file_name)

            logging.info(f"Reading csv file : [{forest_cover_file_path}]")
            forest_cover_data_frame = pd.read_csv(forest_cover_file_path)

            
        except Exception as e:
            raise ForestException(e,sys) from e 

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path =  self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise ForestException(e,sys) from e