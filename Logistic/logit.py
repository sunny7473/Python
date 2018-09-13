import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn import preprocessing
from scipy.stats import anderson
train= pd.read_csv('train.csv',low_memory=False)
train_1=train.dropna(how='all',axis=1)
