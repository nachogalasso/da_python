# Code to create our streamlit dashboard
# import the libraries
import pandas as pd
import numpy as np
import plotly.express as px
from regex import R
import streamlit as st

# Create the streamlit dashboard
st.set_page_config(
    page_title='People Analytics Dashboard', 
    page_icon=":bar_chart:", 
    layout='wide'
)

# Loading our data
df = pd.read_excel('C:\python_da\hr_panalytics\imb_analytics_2021.xlsx')

# print(df)
# To run our data in streamlit, we are required to run the command streamlit run name_of_the_file.py in our terminal
# st.dataframe(df)

# CREATING OUR WEB APP DASHBOARD

# ---------- SIDEBAR ----------
st.sidebar.header('Data filters:')
#  Adding the filters
# We need to save the data into a variable
gender = st.sidebar.multiselect(
    # now we specify the label of the filter
    'Gender:',
    # inidicate the column and values that will be displayed
    options=df['Gender'].unique(),
    # If needed we can create a default displayed value
    default=df['Gender'].unique()
)

department = st.sidebar.multiselect(
    'Department:',
    options=df['Department'].unique(),
    default=df['Department'].unique()
)

attrition = st.sidebar.multiselect(
    'Attrition:',
    options= df['Attrition'].unique(),
    default= df['Attrition'].unique()
)

# To filter the data we need to use the st.selection command, the data will be saved into a variable
# this will help us to filter the data
df_selection = df.query(
    # here we add the filter we created in our sidebar
    # First we indicate the variable we are going to use and then we specify the value to filter adding first the @
    "Gender == @gender & Department == @department & Attrition == @attrition"
)

# Replace the original dataframe with the new one df_selection
st.dataframe(df_selection)

# ---------- MAINPAGE ----------
# Now is time to develop our main page with the charts and the KPI
# Let's put a title
st.title(':busts_in_silhouette: People Analytics')
st.markdown('##')

# Our KPI
# Total rows
total_rows = len(df_selection)

# GENDER
df_gender_female = df_selection[df_selection['Gender'] == 'Female']
df_gender_male = df_selection[df_selection['Gender'] == 'Male']
# Total and percentage variables to use on our charts
female_count = df_gender_female.shape[0]
male_count = df_gender_male.shape[0]
female_percentage = round((female_count / total_rows) * 100, 0)
male_percentage = round((male_count / total_rows) * 100, 0)
gender_female_count = ":woman:" + str((df_selection['Gender']=='Female').sum())
gender_male_count = ":man:" + str((df_selection['Gender']=='Male').sum())

# ATTRITION
df_attrition_yes = df_selection[df_selection['Attrition'] == 'Yes']
yes_count = df_attrition_yes.shape[0]
attrition_percentage = round((yes_count / total_rows) * 100, 2)

# Inserting the data into web columns
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Gender count:')
    st.subheader(f"{gender}")
with middle_column:
    st.subheader('Attrition YES:')
    st.subheader(f"{yes_count}")
with right_column:
    st.subheader('Attrition rate:')
    st.subheader(f"{attrition_percentage}")
    
# Seperating the different data
st.markdown('- - -')