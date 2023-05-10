# -*- coding: utf-8 -*-
"""
Created on Mon May  8 14:47:18 2023

@author: forti
"""

from prophet import Prophet
import pandas as pd
#import matplotlib.pyplot as plt
import streamlit as st
import plotly.io as pio
import plotly.express as px
#from plotly import graph_objs as go
from prophet.plot import plot_plotly
import numpy as np


pio.renderers.default = "browser"

st.title("Forecast and Optimization of Inventory")
st.header("""
This Web App predicts the demand of your products. 
""")
st.write('\n')
st.write('\n')
st.write('\n')


#sidebar for streamlit
product = st.sidebar.selectbox("Product", ("Milk", "The rest of your products here..."))
st.sidebar.title(":blue[EOQ Model for Inventory:]")
k = st.sidebar.slider("Choose k (fixed cost of a single transaction of your product) in dollars", 25, 80)
h = st.sidebar.slider("Choose h (yearly holding cost  per unit) in dollars", 1, 10)
L = st.sidebar.slider("Choose L (waiting time between order and reception) in days", 1, 20)
L = L/365


#reads data
milk = pd.read_csv('milk_production.csv', parse_dates=['month'], )
milk.columns = ['year', 'gallons']

milk_02 = milk.iloc[:151]

#plots figure
figure_01=px.line(milk_02,x="year",y="gallons")
figure_01.layout.update(title_text="Demand of Milk",xaxis_rangeslider_visible=True)
st.plotly_chart(figure_01)

#plots dataframe
st.dataframe(milk_02)

#changes names of columns to process in prophet
milk.columns = ['ds', 'y']


idx = round(len(milk) * 0.90)
train = milk[:idx]
test = milk[idx:]
#print(f'Train: {train.shape}')
#print(f'Test: {test.shape}')

#milk.set_index('ds').plot(title='Monthly Milk Production')

model = Prophet().fit(train)
future = model.make_future_dataframe(len(test), freq='MS')
forecast = model.predict(future)
cols = ['ds', 'yhat', 'yhat_lower', 'yhat_upper']

pd.concat([forecast['yhat'].iloc[0:5], train['y'].iloc[0:5]], axis=1)
pd.concat([forecast['yhat'].iloc[-5:], test['y'].iloc[-5:]], axis=1)


##############################################################################

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(forecast)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='milk_forecast.csv',
    mime='text/csv',
)

###############################################################################


#model.plot(forecast)
fig1 = plot_plotly(model, forecast)
fig1.layout.update(title_text="Forecast of Milk")
st.plotly_chart(fig1)

#plots dataframe in streamlit
#st.dataframe(forecast)

#plots forecast components in streamlit
st.write("Forecast components")
fig2 = model.plot_components(forecast)
st.write(fig2)


st.sidebar.subheader(':green[Forecasted yearly demand:]')

F = forecast['yhat'].iloc[151:].sum()
F = round(F)
st.sidebar.subheader(f":green[F  = {F} units of your product.]")
st.sidebar.subheader(':red[How much should I order?]. To minimize the cost of your inventory it is recommended to order:')
st.sidebar.markdown(":white[Q = $\sqrt{kF/h}$]")




#st.sidebar.subheader(f"Q  = {h} units of your product")


st.sidebar.subheader(':red[When should I order?]. When your inventory stock reaches:')
st.sidebar.markdown(":white[S = $F*L$]")

result_2 = st.sidebar.button("Calculate Q and S")
if result_2:
    Q = np.sqrt((k*F)/h)
    Q = round(Q)
    S = F*L
    S = round(S)
    st.sidebar.write(f"Q  = {Q} units of your product")
    st.sidebar.write(f"S  = {S} units of your product")

#st.sidebar.title(":blue[Safety Stock:]")


