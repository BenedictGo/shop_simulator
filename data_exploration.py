#exploratory data analysis of shopper behaviour data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load data
df = pd.read_csv('Data/monday.csv', sep=';',parse_dates=True, index_col=0)

#total number of unique customers for each shop section
df.groupby('location').size()

#amount of customers per section over time
#fill in missing minutes
df_full = pd.DataFrame()

for customer in df['customer_no'].unique():
    df_customer = df[df['customer_no'] == int(customer)]
    df_customer= df_customer.resample("1min").first().interpolate(method='pad')
    df_full = pd.concat([df_full, df_customer])

#add minute and hour column
df_timecalc = df_full.groupby([df_full.index,'location']).size().unstack().fillna(0)

#visualize traffic at checkout
sns.lineplot(x=df_timecalc.index,y=df_timecalc['checkout'])

#time spend per customer
df_full = df_full.reset_index()
df_customertime = df_full.groupby('customer_no').timestamp.agg(['min', 'max'])
df_customertime['duration'] = df_customertime['max'] - df_customertime['min']

#total customers in shop over time
df_full.groupby('timestamp').size()

#revenue calculation
pricedata = {'fruit':4,
             'spices':3,
             'dairy':5,
             'drinks':6,
             'checkout':0}

df_full.groupby('location').size().index
revenue = df_full.groupby('location').size()

for location in revenue.index:
    print('revenue in ' + location + ' is:')
    print(str(pricedata[location]*revenue[location]) + ' EUR')



