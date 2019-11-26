import pandas as pd
from logging import getLogger

TRAIN_DATA = './input/train.csv'
TEST_DATA = './input/test.csv'

logger = getLogger(__name__)

def load_data(path):
	logger.debug('reading ' + path)
	df = pd.read_csv(path)
	logger.debug('done')
	return df

def load_train_data():
	df = load_data(TRAIN_DATA)
	return df

def load_test_data():
	df = load_data(TEST_DATA)
	return df

	
