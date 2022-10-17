import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import itertools
st.write('''# Sine Wave!''')
# Generating time data using arange function from numpy
# time = np.arange(0, 20*np.pi, 0.01) 
frequency = st.slider('frequency',1, 10, 1, 1)  # freq (Hz)
amplitude=st.slider('amplitude',1,10,1,1)
timex = np.linspace(0, 3, 1200) #time steps
sine = amplitude * np.sin(2 * np.pi * frequency* timex) # sine wave 
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
plt.plot(timex, sine,'r-')
st.pyplot(fig)



chart = st.line_chart(np.zeros(shape=(1,1)))
import time
x = np.arange(0, 100*np.pi, 0.1)
for i in itertools.count(start=1):
    y = amplitude*np.sin(x[i]*frequency)
    #amplitude * np.sin(2 * np.pi * frequency* timex)
    chart.add_rows([y])
    time.sleep(0.01)


''' # 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

# the function, which is y = sin(x) here
y = np.sin(x)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y, 'b-')
# plot the function

st.write(fig) '''
