from ast import For
from distutils.log import set_verbosity
import yaml
import sys,os
from forest_cover.exception import ForestException
import numpy as np
import dill
import pandas as pd
from forest_cover.constant import *


#write yaml file

def write_yaml_file(file_path:str, data:dict=None):
    """create ymal file with
    file_pat:str
    data : dict"""

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise ForestException(e,sys) from e

def read_yaml_file(file_path:str)->dict:
    """reads a yaml file and returen the constents file path :str"""
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ForestException(e,sys) from e


def save_numpy_data(file_path:str, array:np.array):
    """Save numpy array data to file
    file_path: str location of the file to save 
    array :np.array data to save"""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise ForestException(e,sys) from e

def load_numpy_data(file_path : str)->np.array:
    """load numpy array data from file
    file_path: str location of file to load 
    return: np.array data loaded"""

    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ForestException(e,sys) from e

def save_object(file_path: str, obj):
    """ file_path:str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise ForestException(e,sys) from e
