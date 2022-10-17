from select import select
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

df = pd.read_csv('ECG.csv')

timeaxis= df['time'].tolist()
amplitude = df['amplitude'].tolist()
#defining containers
header = st.container()
select_param = st.container()
plot_spot = st.empty()
#title
with header:
    st.title("Sampling Studio")
#select parmeter drop down
with select_param:
    param_lst = list(df.columns)
    param_lst.remove('time')
    select_param = st.selectbox('Select an Amplitude Parameter',   param_lst)
#function to make chart


def make_chart(df, y_col, ymin, ymax):
    fig = go.Figure(layout_yaxis_range=[ymin, ymax])
    fig.add_trace(go.Scatter(x=df['time'], y=df[y_col],           mode='lines'))
    fig.update_layout(width=900, height=570, xaxis_title='time',
    yaxis_title=y_col)
    st.write(fig)
    #func call
n = len(df)
ymax = max(df['amplitude'])+0.4
ymin = min(df['amplitude'])-0.4
for i in range(0, n-1, 1):
    df_tmp = df.iloc[i:i+500, :]
    with plot_spot:
        make_chart(df_tmp, select_param,ymin, ymax)
    time.sleep(0.05)