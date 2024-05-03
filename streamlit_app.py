#######################
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


#######################
# Page configuration
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

#######################
# Load data from a CSV file
data = pd.read_csv('data/data.csv')
#######################
# Plots

# Create line chart
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')

# Assuming 'x' is the common column for both graphs and 'y1', 'y2' are the values for each plot
x = data['x']
y1 = data['y1']
y2 = data['y2']

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Plotting the area plot for c1
ax[0].fill_between(x, y1, color='blue', alpha=0.3, label='a')
ax[0].fill_between(x, y2, color='red', alpha=0.3, label='b')
ax[0].set_title('Graph c1')
ax[0].legend()

# For the bar chart c2, we can simulate a different scenario or just reuse x, y1, y2 for simplicity
# To simulate more bar-like data, you can use:
y1_bars = y1[0:len(x):2]  # Select every second element for bar chart
y2_bars = y2[0:len(x):2]
x_bars = x[0:len(x):2]

# Plotting the bar chart for c2
ax[1].bar(x_bars - 0.5, y1_bars, width=0.5, color='blue', label='a')
ax[1].bar(x_bars, y2_bars, width=0.5, color='red', label='b')
ax[1].set_title('Graph c2')
ax[1].legend()

# Display the plot using Streamlit
st.pyplot(fig)
