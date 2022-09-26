# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('Salary.csv')
#df=pd.DataFrame(df)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

fig=px.data.gapminder().query("country=='Canada'")
fig= px.line(df,x='YearsExperience',y='Salary',title='Salary in Canada')
st.plotly_chart(fig)
fig=px.scatter(df,x='YearsExperience',y='Salary',title='Salary in Canada')
st.plotly_chart(fig)

MentalHealth=pd.read_csv('Student Mental health copy.csv')
if st.checkbox('Show data'):
    st.subheader('Raw data')
    st.write(MentalHealth)

fig=px.pie(MentalHealth,values='Age',names='What is your course?',title='Student Major and Age',color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside',
                  textinfo='percent+label')
st.plotly_chart(fig)
fig=px.bar(MentalHealth,x='Do you have Depression?',y='Age',color='Choose your gender',title= 'Depression, Gender and Age',barmode='group',
             height=500)
st.plotly_chart(fig)
option=st.selectbox(
    "Do you have depression?",
    ('Yes','No'))
st.write('Your answer:',option)
fig = px.histogram(MentalHealth, x="What is your course?",color='Choose your gender',histfunc="count",text_auto=True,title='Course number of each gender',color_discrete_sequence=['indianred'])
st.plotly_chart(fig)
