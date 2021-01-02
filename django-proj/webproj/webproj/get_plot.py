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
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(airdf_date.corr(), cmap=cmap, annot=True, vmax=1, center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})
print(plt.plot())

airdf_date.plot(x='date', y= ['PM10','PM2.5'])
plt.plot()

f, ax = plt.subplots(4, 2, figsize=(20,15))
sns.scatterplot(x='NO2', y= 'PM10', data=airdf_date, ax=ax[0,0])
sns.scatterplot(x='NO2', y= 'PM2.5', data=airdf_date, ax=ax[0,1])
sns.scatterplot(x='CO', y= 'PM10', data=airdf_date, ax=ax[1,0])
sns.scatterplot(x='CO', y= 'PM2.5', data=airdf_date, ax=ax[1,1])
sns.scatterplot(x='SO2', y= 'PM10', data=airdf_date, ax=ax[2,0])
sns.scatterplot(x='SO2', y= 'PM2.5', data=airdf_date, ax=ax[2,1])
sns.scatterplot(x='O3', y= 'PM10', data=airdf_date, ax=ax[3,0])
sns.scatterplot(x='O3', y= 'PM2.5', data=airdf_date, ax=ax[3,1])
plt.plot()

f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(airdf_time.corr(), cmap=cmap, annot=True, vmax=1, center=0, square=True, linewidths=.5, cbar_kws={'shrink': .5})
plt.plot()

airdf_time.plot(x='time', y= ['PM10','PM2.5'])
plt.plot()

airdf_time.plot(x='time', y= 'O3')
plt.plot()

sns.scatterplot(x='O3', y= 'PM10', data=airdf_time)
sns.scatterplot(x='O3', y= 'PM2.5', data=airdf_time)
plt.plot()

f, ax = plt.subplots(1, 3, figsize=(15,5))
sns.scatterplot(x='O3', y= 'SO2', data=airdf_time, ax=ax[0])
sns.scatterplot(x='O3', y= 'NO2', data=airdf_time, ax=ax[1])
sns.scatterplot(x='O3', y= 'CO', data=airdf_time, ax=ax[2])
plt.plot()

