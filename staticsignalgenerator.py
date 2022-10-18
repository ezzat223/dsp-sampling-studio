import itertools
import time as tm
from itertools import count
from signal import signal

import matplotlib.pyplot as plt
import mpld3
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from matplotlib.animation import FuncAnimation

import streamlit as st
import streamlit.components.v1 as components

st.title("Sampling Studio")
st.sidebar.title("Options")
samp_freq=st.sidebar.slider("Sampling Frequency",min_value=0,max_value=100,value=20)
# org_freq=st.sidebar.slider("Frequency",min_value=0,max_value=100,value=20,step=5)
checked=st.sidebar.checkbox("Add noise",value=False) 
snr_db=0
if checked:
     snr_db=st.sidebar.number_input("SNR level",value=0,min_value=0,max_value=120,step=5)

st.markdown("""
<tr>
""",True)
st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
 visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
st.markdown("""
<style>
.css-12gp8ed.eknhn3m4
{
 visibility:hidden;
}
</style>
""",unsafe_allow_html=True)

st.write('''# Sine Wave!''')
# Generating time data using arange function from numpy
# time = np.arange(0, 20*np.pi, 0.01) 
frequency = st.sidebar.slider('frequency',1, 10, 1, 1)  # freq (Hz)
amplitude=st.sidebar.slider('amplitude',1,10,1,1)
timex = np.linspace(0, 3, 1200) #time steps
sine = amplitude * np.sin(2 * np.pi * frequency* timex) # sine wave 
plt.subplot(3,1,1)
#power signal 
power=sine**2
signal_average_power=np.mean(power)
signal_averagePower_db=10*np.log10(signal_average_power)
noise_db=signal_averagePower_db-snr_db
noise_watts=10**(noise_db/10)

mean_noise=0
noise=np.random.normal(mean_noise,np.sqrt(noise_watts),len(sine))
noise_signal=sine+noise
# Finding amplitude at each time
def periodicf(li,lf,f,x):
    if x>=li and x<=lf :
        return f(x)
    elif x>lf:
        x_new=x-(lf-li)
        return periodicf(li,lf,f,x_new)
    elif x<(li):
        x_new=x+(lf-li)
        return periodicf(li,lf,f,x_new)



# Finally displaying the plot
#plt.show()
fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(1,1,1)



# Settng title for the plot in blue color
plt.title('Sine Wave', color='b')

# Setting x axis label for the plot
plt.xlabel('Time'+ r'$\rightarrow$')

# Setting y axis label for the plot
plt.ylabel('Sin(time) '+ r'$\rightarrow$')

# Showing grid
plt.grid()

# Highlighting axis at x=0 and y=0
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Plotting time vs amplitude using plot function from pyplot
if checked:
    plt.plot(timex, noise_signal,'r-')
else:
        plt.plot(timex, sine,'r-')
st.pyplot(fig)

