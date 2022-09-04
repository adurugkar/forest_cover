import sys , os
from forest_cover.exception import ForestException
from forest_cover.logger import logging
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from forest_cover.entity.artifact_entity import DataIngestionArtifact
from forest_cover.entity.config_entity import DataIngestionConfig




