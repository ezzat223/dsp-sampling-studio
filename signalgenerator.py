from select import select
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
frequency = st.slider('frequency',1, 10, 1, 1)  # freq (Hz)
amplitude=st.slider('amplitude',1,10,1,1)
x=np.linspace(0, 3, 1000)

y=[]
for i in range(0,len(x),1):
    y.append(amplitude*np.sin(2 * np.pi * frequency*x[i]))
print("x: ", len(x))
print("y: ", len(y))


dataframe={'time': x,
'amplitude':y}
df=pd.DataFrame(dataframe)
print(df)


#dynamic
timeaxis= df['time'].tolist()
amplitude = df['amplitude'].tolist()
#defining containers
header = st.container()
select_param = st.container()
plot_spot = st.empty()
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