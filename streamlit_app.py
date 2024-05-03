#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


#######################
# Page configuration
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data
df_reshaped = pd.read_csv('data/us-population-2010-2019-reshaped.csv')

# Create line chart
fig = px.line(df_reshaped, x='date_column', y='value_column', title='Line Chart Title')

# Add chart to Streamlit app
st.plotly_chart(fig)
