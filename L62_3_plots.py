import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['Line_1','Line_2','Line_3'])

#Line chart
st.subheader("1.1. Line chart :")
st.line_chart(chart_data)

#Area chart
st.subheader("1.2. Area chart :")
st.area_chart(chart_data)

#Bar chart
st.subheader("1.3. Bar chart :")
st.bar_chart(chart_data)

#Data visualization
st.subheader("2.Data visualization with Matplotlib and Seaborn:")


st.subheader("2.1. Loading the DataFrame")
df = pd.read_csv("/Users/dheerajreddypasham/Documents/GfG/iris.csv")
st.dataframe(df)


st.subheader("2.2. Bar graph with matplotlib:")
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)


st.subheader("2.3. Distribution plot with seaborn:")
fig = plt.figure(figsize=(15, 8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header("3. Multiple Graphs in one columns :")
col1, col2 = st.columns(2)

with col1:
    st.text('KDE=False')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'], kde=False)
    st.pyplot(fig1)

with col2:
    st.text('hist=False')
    fig2 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig2)   
    

st.header("4. Changing style:")
col1, col2 = st.columns(2)

with col1:
    fig1 = plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig1)

with col2:
    fig2 = plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['petal_length'], hist=False)
    st.pyplot(fig2)    
    
st.header('5. Exploring Different Graphs:')

st.subheader('5.1. Scatter plot:')
fig,ax = plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2. Count plot:')
fig  = plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species')
st.pyplot(fig)

st.subheader('5.3. Box plot:')   
fig  = plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)

st.subheader('5.4. Violin plot:')
fig  = plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='species',y='petal_length')
st.pyplot(fig)



