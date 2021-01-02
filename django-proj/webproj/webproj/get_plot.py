import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

airdf = pd.read_csv('Measurement_summary.csv')
airdf.head()
date_time = airdf['Measurement date'].str.split(' ', n=1, expand=True)
airdf = airdf.drop(['Measurement date'], axis=1)
airdf['date'] = date_time[0]
date_time[1] = date_time[1].str.split(':', n=1, expand=True)
airdf['time'] = date_time[1]
airdf['time'] = airdf['time'].astype('int')
des = airdf.describe()
airdf_date = airdf.groupby(['date'], as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})
airdf_time = airdf.groupby(['time'], as_index=False).agg({'SO2':'mean', 'NO2':'mean', 'O3':'mean', 'CO':'mean', 'PM10':'mean', 'PM2.5':'mean'})
