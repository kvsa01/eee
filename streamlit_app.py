import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('data/data.csv')

# Assuming 'x' is the common column for all graphs and 'ResNet50', 'AlexNet', 'Inceptionv3' are the values for each plot
x = data['x']
resnet50 = data['ResNet50']
alexnet = data['AlexNet']
inceptionv3 = data['Inceptionv3']

# Create subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Plotting the area plot
ax[0].fill_between(x, resnet50, color='blue', alpha=0.3, label='ResNet50')
ax[0].fill_between(x, alexnet, color='red', alpha=0.3, label='AlexNet')
ax[0].fill_between(x, inceptionv3, color='green', alpha=0.3, label='Inceptionv3')
ax[0].set_title('Area Plot')
ax[0].legend()

# Plotting the line graph
ax[1].plot(x, resnet50, color='blue', label='ResNet50')
ax[1].plot(x, alexnet, color='red', label='AlexNet')
ax[1].plot(x, inceptionv3, color='green', label='Inceptionv3')
ax[1].set_title('Line Graph')
ax[1].legend()

# Plotting the bar chart
ax[2].bar(x, resnet50, color='blue', alpha=0.5, label='ResNet50')
ax[2].bar(x, alexnet, color='red', alpha=0.5, label='AlexNet')
ax[2].bar(x, inceptionv3, color='green', alpha=0.5, label='Inceptionv3')
ax[2].set_title('Bar Chart')
ax[2].legend()

# Display the plot using Streamlit
st.pyplot(fig)
