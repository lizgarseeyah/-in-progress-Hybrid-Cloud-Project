#!/usr/bin/env python
# coding: utf-8

# In[84]:


# https://towardsdatascience.com/covid-19-data-visualization-using-python-3c8bcfaeff5f
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import mpld3
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objects as go
import pickle
from flask import Flask, url_for, request, render_template, jsonify, redirect
from markupsafe import escape
from jinja2 import Template


# In[85]:


username='username11111'
api_key='EmCaCOlb3DfERiYwBEBr'
app = Flask(__name__)


# In[86]:


chart_studio.tools.set_credentials_file(username, api_key)


# ## Load the data

# In[87]:


path = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-25-2020.csv'
df = pd.read_csv(path)
df.info()
df.head()


# In[88]:


df.drop(['FIPS', 'Admin2','Last_Update','Province_State', 'Combined_Key'], axis=1, inplace=True)
df.rename(columns={'Country_Region': "Country"}, inplace=True)
df.head()


# In[89]:


world = df.groupby("Country")['Confirmed','Active','Recovered','Deaths'].sum().reset_index()
world.head()


# In[ ]:


confirmed = str(world.loc[world['Country']=='US', 'Confirmed'])

@app.route('/', methods=['POST'])
def print_m():
    flask.render_template('confirmed.html', confirmed=confirmed)
    return jsonify(confirmed)

@app.route('/', methods = ['GET'])
def result():
    return render_template("confirmed.html",confirmed=confirmed)


# In[ ]:


active = world.loc[world['Country']=='US', 'Active']


# In[18]:


recovered = world.loc[world['Country']=='US', 'Recovered']


# In[19]:


death = world.loc[world['Country']=='US', 'Deaths']


# In[20]:


### Find top 20 countries with maximum number of confirmed cases
top_20 = world.sort_values(by=['Confirmed'], ascending=False).head(20)
### Generate a Barplot
plt.figure(figsize=(6,5))

# plot = sns.barplot(top_20['Confirmed'], top_20['Country'])
# # plot = px.bar(top_20['Confirmed'], top_20['Country'])
# for i,(value,name) in enumerate(zip(top_20['Confirmed'],top_20['Country'])):
#     plot.text(value,i-0.05,f'{value:,.0f}',size=10)
# plt.show()

fig = go.Figure(data=[go.Bar(x=top_20['Country'],y=top_20['Confirmed'], text=top_20['Country'])])

fig.show()


# In[32]:


py.plot(fig, filename='bar_chart', auto_open=False)


# In[33]:


top_5 = world.sort_values(by=['Confirmed'], ascending=False).head()
### Generate a Barplot
plt.figure(figsize=(15,5))
confirmed = sns.barplot(top_5['Confirmed'], top_5['Country'], color = 'red', label='Confirmed')
recovered = sns.barplot(top_5['Recovered'], top_5['Country'], color = 'green', label='Recovered')
### Add Texts for Barplots
for i,(value,name) in enumerate(zip(top_5['Confirmed'],top_5['Country'])):
    confirmed.text(value,i-0.05,f'{value:,.0f}',size=9)
for i,(value,name) in enumerate(zip(top_5['Recovered'],top_5['Country'])):
    recovered.text(value,i-0.05,f'{value:,.0f}',size=9)
plt.legend(loc=4)
plt.show()
plt.savefig('test.png')


# In[ ]:


figure = px.choropleth(world,locations='Country', locationmode='country names', color='Confirmed', hover_name='Country', color_continuous_scale='tealgrn', range_color=[1,1000000],title='Countries with Confirmed cases')
figure.show()


# In[ ]:


py.plot(figure, filename='world_map', auto_open=False)


# In[ ]:


if __name__ == "__main__":
    app.run(debug=False)
    app.run()


# In[ ]:





# In[ ]:




