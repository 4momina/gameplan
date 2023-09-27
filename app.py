import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from faker import Faker
import random
from datetime import datetime, timedelta
import numpy as np

st.title("Willkommen!")

########################################################################################################  Set up the main window
st.header("Graphische Darstellung von Nitratwerten")
############################## PLOT FEATURE VS DATETIME
## read in data
#land_feature = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spolied_agriculture_extra_column_2.csv").dropna().groupby('Date')[
    #'Nitrat level2'].sum().reset_index()
land_feature = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spolied_agriculture_extra_column_2.csv").dropna()
companies_feature = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spolied_companies_extra_column_2.csv").dropna()
transport_feature = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spoiled_transport_extra_column_2.csv").dropna()
water_feature = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\fake_water_2.csv")
land_feature['Date'] = pd.to_datetime(land_feature['Date'])
companies_feature['Date'] = pd.to_datetime(companies_feature['Date'])
transport_feature['Date'] = pd.to_datetime(transport_feature['Date'])
water_feature['Date'] = pd.to_datetime(water_feature['Date'])
### ADD SCATTERPLOTS
## add plots to streamlit

#  LAND
st.subheader('Bevor man verschiedene Daten zusammenfasst')

# Create the line plot
fig_land_sc = px.scatter(land_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Landwirtschaft')

# Customize the plot (optional)
fig_land_sc.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_land_sc.update_xaxes(title_text='Date')
fig_land_sc.update_yaxes(title_text='Verdünnungsmittelnitratwert')

# Display the plot
st.plotly_chart(fig_land_sc)

#### Transport

#st.subheader('Graphische Darstellung von Nitratwerten im Verkehr')

# Create the line plot
fig_transport_sc = px.scatter(transport_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Verkehr')

# Customize the plot (optional)
fig_transport_sc.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_transport_sc.update_xaxes(title_text='Date')
fig_transport_sc.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_transport_sc)

#### Companies
#st.subheader('Graphische Darstellung von Nitratwerten im Wirtschaft')

# Create the line plot
fig_companies_sc= px.scatter(companies_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Wirtschaft')

# Customize the plot (optional)
fig_companies_sc.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_companies_sc.update_xaxes(title_text='Date')
fig_companies_sc.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_companies_sc)

land_feature = land_feature.groupby('Date')['Nitrat level2'].sum().reset_index()
transport_feature = transport_feature.groupby('Date')['Nitrat level2'].sum().reset_index()
companies_feature = companies_feature.groupby('Date')['Nitrat level2'].sum().reset_index()

########################################################################################################################
##### ADD LINEPLOTS
########################################################################################################################
st.subheader('Nachdem man verschiedene Daten zusammenfasst')

## add plots to streamlit

#  LAND
#st.subheader('Graphische Darstellung von Nitratwerten im Landwirtschaft')

# Create the line plot
fig_land = px.scatter(land_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Landwirtschaft')

# Customize the plot (optional)
fig_land.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_land.update_xaxes(title_text='Date')
fig_land.update_yaxes(title_text='Verdünnungsmittelnitratwert')

# Display the plot
st.plotly_chart(fig_land)

#### Transport

#st.subheader('Graphische Darstellung von Nitratwerten im Verkehr')

# Create the line plot
fig_transport = px.line(transport_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Verkehr')

# Customize the plot (optional)
fig_transport.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_transport.update_xaxes(title_text='Date')
fig_transport.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_transport)

#### Companies
#st.subheader('Graphische Darstellung von Nitratwerten im Wirtschaft')

# Create the line plot
fig_companies= px.line(companies_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Wirtschaft')

# Customize the plot (optional)
fig_companies.update_traces(marker=dict(color='#288BA8'), mode='markers')
fig_companies.update_xaxes(title_text='Date')
fig_companies.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_companies)
#####################################################################################################################
##### ADD LINES TO LINEPLOTS
##################################################################################################################
st.subheader('Man verbindet die Punkte mit einer Linie')

## add plots to streamlit

#  LAND
#st.subheader('Graphische Darstellung von Nitratwerten im Landwirtschaft')

# Create the line plot
fig_land_li = px.scatter(land_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Landwirtschaft')

# Customize the plot (optional)
fig_land_li.update_traces(marker=dict(color='#288BA8'), mode='markers+lines')
fig_land_li.update_xaxes(title_text='Date')
fig_land_li.update_yaxes(title_text='Verdünnungsmittelnitratwert')

# Display the plot
st.plotly_chart(fig_land_li)

#### Transport

#st.subheader('Graphische Darstellung von Nitratwerten im Verkehr')

# Create the line plot
fig_transport_li = px.line(transport_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Verkehr')

# Customize the plot (optional)
fig_transport_li.update_traces(line=dict(color='#288BA8'), mode='markers+lines')
fig_transport_li.update_xaxes(title_text='Date')
fig_transport_li.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_transport_li)

#### Companies
#st.subheader('Graphische Darstellung von Nitratwerten im Wirtschaft')

# Create the line plot
fig_companies_li = px.line(companies_feature, x='Date', y='Nitrat level2', title='Graphische Darstellung von Nitratwerten im Wirtschaft')

# Customize the plot (optional)
fig_companies_li.update_traces(line=dict(color='#288BA8'), mode='markers+lines')
fig_companies_li.update_xaxes(title_text='Date')
fig_companies_li.update_yaxes(title_text='Value')

# Display the plot
st.plotly_chart(fig_companies_li)









st.header("Korrelation Analysis")
# land = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spolied_agriculture_extra_column_2.csv").groupby('Date')[
#     'Nitrat level'].sum().reset_index()
# companies = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spolied_companies_extra_column_2.csv").groupby('Date')[
#     'Nitrat level'].sum().reset_index()
# transport = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\spoiled_transport_extra_column_2.csv").groupby('Date')[
#     'Nitrat level'].sum().reset_index()
# water = pd.read_csv("C:\\Users\\4momina\\Desktop\\gameplan\\fake_water_2.csv")

data_for_y_axis = land_feature['Nitrat level2']
columns = ("land", "companies", "transport")
dict_for_df = {"land": land_feature,
               "companies": companies_feature,
               "transport": transport_feature
               }
axis_y = st.selectbox(
    'choose value for axis x', columns)
data_for_y_axis = dict_for_df[axis_y]
corr_coef = np.corrcoef(water_feature['Nitrat level'], data_for_y_axis['Nitrat level2'])[0, 1]


fig = px.scatter(x=data_for_y_axis['Nitrat level2'],
                 y=water_feature['Nitrat level'],
                 title='Correlation Analysis',
                 labels={'x': "Nitratwerten von ausgewählen Feature", 'y': 'Wasser  Nitratwerten'},
                 trendline='ols',
                 color_discrete_sequence=['#288BA8']  # Color for markers
                 )

text = f"Correlation Coefficient: {corr_coef:.2f}"


st.plotly_chart(fig)
st.write(text)
