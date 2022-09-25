### Importing Packages###
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu

### Loading our Dataset and launching streamlit ###
df= pd.read_csv("world_population.csv")
df.head()

#### Creating Navigation Bar ####
Menu = option_menu(None, ["Home","Dataset","Dashboard"],icons=['house',"cloud","bar-chart-line"],menu_icon="cast", default_index=0, orientation="horizontal", styles={"container": {"padding": "0!important", "background-color": "#B0C4DE"},"icon": {"color": "black", "font-size": "25px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},"nav-link-selected": {"background-color": "#4F6272"},})

### Setting Conditions ###
if Menu == "Home": st.title('World Population')
Image= Image.open("C:/Users/ranab/Desktop/project/map.jpg")
if Menu == "Home": st.image(Image,caption='')
if Menu == "Home": st.write("In the following Dashboard, we are going to observe the world population changes throughout the years. The purpose behind our study is to find what are some intereting factors that might cause the changes.")
if Menu== "Dataset": st.header("A Glimpse Over The Data")
if Menu == "Dataset": st.table(df.head())
if Menu == "Dataset": st.write("In this Dataset,we have Historical Population data for every Country/Territory in the world by different parameters like Area Size of the Country/Territory, Name of the Continent, Name of the Capital, Density, Population Growth Rate, Ranking based on Population, World Population Percentage, etc.")
if Menu == "Dataset":st.write("Rank : Ranked particular country by population")
if Menu == "Dataset":st.write("CCA3 : 3 digit country code.")
if Menu == "Dataset":st.write("Country : Country name")
if Menu == "Dataset":st.write("Capital : Capital of Country")
if Menu == "Dataset":st.write("Continent : Name of the Continent where the Country Belongs")
if Menu == "Dataset":st.write("2022 population : The Population of the Country in year 2022.")
if Menu == "Dataset":st.write("2020 population : The Population of the Country in year 2020.")
if Menu == "Dataset":st.write("2015 population : The Population of the Country in year 2015.")
if Menu == "Dataset":st.write("2010 population : The Population of the Country in year 2010.")
if Menu == "Dataset":st.write("2000 population : The Population of the Country in year 2000.")
if Menu == "Dataset":st.write("1990 population : The Population of the Country in year 1990.")
if Menu == "Dataset":st.write("1980 population : The Population of the Country in year 1980.")
if Menu == "Dataset":st.write("1970 population : The Population of the Country in year 1970.")
if Menu == "Dataset":st.write("Area : The land area of the Country (measured in km^2).")
if Menu == "Dataset":st.write("Density : The Population Density of the Country (measured in per km^2).")
if Menu == "Dataset":st.write("Growth Rate : The Population Growth Rate of the Country.")
if Menu == "Dataset":st.write("World Population Percentage : The percentage of the World Population residing in that Country.")
if Menu=="Dashboard" : st.header("Exploratory Data Analysis - Visualizations")


### DASHBOARD ###
col3, col4 = st.columns(2)
### Map ###
pop = df.melt(id_vars=['Country'], value_vars=['2020', '2010', '2000', '1990', '1980', '1970'], var_name='Year', value_name='Population')
pop = pop.sort_values('Year')
pop.head()
fig1 = px.choropleth(pop, 
              locations = 'Country',
              color="Population", 
              animation_frame="Year",
              color_continuous_scale='Turbo',
              locationmode='country names',template='plotly_dark',color_discrete_sequence=px.colors.sequential.PuBuGn,
              height=500, width= 600
             )

if Menu=="Dashboard": col3.subheader("World Map")
if Menu == "Dashboard": col3.write (fig1)
if Menu == "Dashboard": st.write("Most of the countries didn't even change hue. Most noticable countries were just China and India.")

#### Bar ####

country_count = df['Continent'].value_counts()
fig5 = px.bar(y=country_count.values, x=country_count.index, color = country_count.index,color_discrete_sequence=px.colors.sequential.PuBuGn,text=country_count.values,template='plotly_white')
fig5.update_layout(
    xaxis_title="Countries",
    yaxis_title="Count",
    font = dict(size=15,family="Franklin Gothic"))
if Menu =="Dashboard": col4.subheader('Number of Countries By Continent')
if Menu=="Dashboard": col4.write(fig5)
if Menu=="Dashboard": col4.write("We can notice that Africa has the highest number of countries, but Asia ranks #1 in the population Growth")


col5, col6 = st.columns(2)
### Bar Graph 2 ###
top_pop = df.sort_values(by = '2020', ascending = False).head(10)   
colors= ['#778899', '#B0C4DE', '#CAE1FF','#BCD2EE','#A2B5CD','#008B8B','#528B8B', '#009ACD', '#00688B','#68838B']
data = go.Bar(x = top_pop['Country'], y = top_pop['2020'], text = top_pop['2020'],textposition ='outside',textfont = dict(size = 30,color = 'black'), marker = dict(color = colors,opacity = 0.7,line_color = 'black',line_width = 2))
layout = go.Layout(title = {'text': "<b>Top 10 Countries With Highest Popualtion</b>",'x':0.5,'xanchor': 'center'},xaxis = dict(title='Countries' ),yaxis =dict(title='Populations'),width = 600,height = 500,template = 'plotly_white')
fig4=go.Figure(data = data, layout = layout)
fig4.update_xaxes(tickangle=90,tickfont_size = 12)
if Menu== "Dashboard": col5.write(fig4)
if Menu== "Dashboard": col5.write("From above graph, we can see that China is the country with highest poulation of 1.42B in the world & India is the second country with population of 1.41B")

### Bar Graph ###
less_pop = df.sort_values(by = '2020', ascending = True).head(10)
colors= ['#778899', '#B0C4DE', '#CAE1FF','#BCD2EE','#A2B5CD','#008B8B','#528B8B', '#009ACD', '#00688B','#68838B']
data = go.Bar(x = less_pop['Country'], y = less_pop['2020'],text = less_pop['2020'],textposition ='outside',textfont = dict(size = 10,color = 'black'),marker = dict(color = colors, opacity = 0.7, line_color = 'black', line_width = 2))
layout = go.Layout(title = {'text' : '<b>Top 10 Countries With Lowest Popualtion</b>', 'x' : 0.5},xaxis = dict(title = 'Countries'),yaxis = dict(title = 'Population'),width = 600,height = 500,template = 'plotly_white')
fig3 = go.Figure(data = data, layout = layout)
fig3.update_xaxes(tickangle=90,tickfont_size = 12)
if Menu == "Dashboard": col6.write(fig3)
if Menu=="Dashboard": col6.write("Vatican City is the country with lowest population of 510")

col8, col9 = st.columns(2)

### Pie 1 ###
labels= ('Asia', 'Africa', 'Europe', 'North America', 'South America')
sizes = (59,17.8,9.33,7.51,5.48)
explode = (0.01, 0.01, 0.01, 0.01, 0.01)
colors = ['#778899', '#B0C4DE', '#CAE1FF','#BCD2EE','#A2B5CD']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, autopct='%1.1f%%', labels=labels, colors=colors, shadow=True, startangle=90)
ax1.axis('equal') 
if Menu=="Dashboard": col8.subheader("World Population Percentage Distribution")
if Menu=="Dashboard": col8.pyplot(fig1)
if Menu=="Dashboard": col8.write("Asia is the Continent with 59.2% of highest World population percentage and Oceania continent have only 0.55% of lowest world poulation precentage.")


### Line Chart 1 ###
top10 = df.sort_values('2022', ascending=False).head(10)
top10 = top10.melt(id_vars=['Country'], value_vars=['2020', '2010', '2000', '1990', '1980', '1970'], var_name='Year', value_name='Population')
colors= ['#778899', '#B0C4DE', '#CAE1FF','#BCD2EE','#A2B5CD','#008B8B','#528B8B', '#009ACD', '#00688B','#68838B']
fig = px.line(top10, x='Country', y='Population', color='Year',template='plotly_white',color_discrete_sequence=px.colors.sequential.PuBuGn, width=600, height=500, markers=True)
if Menu=="Dashboard": col9.subheader("Top 10 Countries with Highest Population 1970-2020")
if Menu == "Dashboard": col9.write (fig)
if Menu == "Dashboard": col9.write("Here we can see that all countries had a continous growth through out the years except for Russia, Russia's number of population had just stayed at around 140 million through out 1970 and 2020.Then we can observe at the graph that India's population growth is larger than China, by that, its possible that India's population will outnumber China's population in a couple of decades. The slow or minimal growth rate of China is mainly because of their one, two and three-child policy. One child policy is a government-imposed limit of one child allowed per family. In 2015, the government removed all remaining one-child limits, establishing a two-child limit. In May 2021, this was loosened to a three-child limit. Since this law was removed, China will definetly have a bigger growth rate compared to their growth rate then.")
