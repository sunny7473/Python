import numpy as np
import pandas as pd
import csv

train=pd.read_csv('train.csv',low_memory=False)
train=train.drop('user_id',1)
train=train[train['gender']!=0]

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
column_lst=['online_time','1_total_fee','3_total_fee','4_total_fee','month_traffic','contract_time','pay_times','pay_num','last_month_traffic','local_trafffic_month','local_caller_time','age','service1_caller_time','service2_caller_time','former_complaint_num','former_complaint_fee']
for i in range(len(column_lst)):
            train[column_lst[i]]=MinMaxScaler().fit_transform(train[column_lst[i]].values.reshape(-1,1))

service_type = pd.get_dummies(train, columns=['service_type'], prefix='service_type')
contract_type = pd.get_dummies(service_type, columns=['contract_type'], prefix='contract_type')
gender = pd.get_dummies(contract_type, columns=['gender'], prefix='gender')
complaint_level = pd.get_dummies(gender, columns=['complaint_level'], prefix='complaint_level')
net_service = pd.get_dummies(complaint_level, columns=['net_service'], prefix='net_service')
train = net_service

train['current_service']=train['current_service'].replace(90063345,1)
train['current_service']=train['current_service'].replace(90109916,2)
train['current_service']=train['current_service'].replace(90155946,3)
train['current_service']=train['current_service'].replace(99104722,4)
train['current_service']=train['current_service'].replace(89016252,5)
train['current_service']=train['current_service'].replace(89016253,6)
train['current_service']=train['current_service'].replace(89016259,7)
train['current_service']=train['current_service'].replace(89950166,8)
train['current_service']=train['current_service'].replace(89950167,9)
train['current_service']=train['current_service'].replace(89950168,10)
train['current_service']=train['current_service'].replace(99999825,11)
train['current_service']=train['current_service'].replace(99999826,12)
train['current_service']=train['current_service'].replace(99999827,13)
train['current_service']=train['current_service'].replace(99999828,14)
train['current_service']=train['current_service'].replace(99999830,15)

