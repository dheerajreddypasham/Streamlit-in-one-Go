import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

## 1. Altair Scatter plot 

# Add a header
st.header("1. Altair scatter plot")

# Generate some random data
chart_data = pd.DataFrame(np.random.randn(500, 5), columns=['a', 'b', 'c', 'd', 'e'])

# Create an Altair scatter plot
chart = alt.Chart(chart_data).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    tooltip=['a', 'b', 'c', 'd', 'e']  # Corrected 'toollip' to 'tooltip'
)

# Display the chart in Streamlit
st.altair_chart(chart)


## 2. Interactive Charts
import os

# Add a header
st.header("2. Interactive Charts")

# Define the file path
file_path = '/Users/dheerajreddypasham/Documents/GfG/lang_data.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Get the list of columns (languages)
    lang_list = df.columns.tolist()
    
    # Create a multiselect widget for language choices
    lang_choices = st.multiselect('Choose your language', lang_list)
    
    # Check if any language is selected
    if lang_choices:
        # Filter the DataFrame based on selected languages
        new_df = df[lang_choices]
        
        # Display the filtered data as a line chart
        st.subheader("2.1. Line chart")
        st.line_chart(new_df)
        # Display the filtered data as a area chart
        st.subheader("2.2. Area chart")
        st.area_chart(new_df)
    else:
        st.write("Please select at least one language.")
else:
    st.write("File does not exist. Please check the file path.")


## 3. Data visualization with Plotly


# Add a header
st.header("3. Data visualization with Plotly")

# Define the file path
file_path = '/Users/dheerajreddypasham/Documents/GfG/tips.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Display the first few rows of the DataFrame
    st.subheader("3.1. Displaying the dataset")
    st.dataframe(df.head())

    # Add interactivity for plot selection
    plot_type = st.selectbox("Choose plot type", ["Scatter Plot", "Pie Chart"])

    # Create and display plot based on user selection
    if plot_type == "Scatter Plot":
        st.subheader("3.2. Scatter Plot")
        fig_scatter = px.scatter(df, x='total_bill', y='tip', color='sex', title='Total Bill vs Tip by Sex')
        st.plotly_chart(fig_scatter)
    elif plot_type == "Pie Chart":
        st.subheader("3.3. Pie Chart")
        fig_pie = px.pie(df, values='total_bill', names='day', title='Total Bill Distribution by Day')
        st.plotly_chart(fig_pie)
        
    # Pie chart with multiple parameters
    st.subheader("3.4. Pie chart with multiple parameters")   
    fig_pie = px.pie(df, values='total_bill', names='day', title='Total Bill Distribution by Day',opacity = 0.7,
                     color_discrete_sequence = px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie) 
else:
    st.write("File does not exist. Please check the file path.")
    
    
#3.4.histogram
st.subheader("3.4. Histogram")
x1 = np.random.randn(200)    
x2 = np.random.randn(200)    
x3 = np.random.randn(200)        

hist_data = [x1,x2,x3]
group_labels = ["Group-1","Group-2","Group-3"]  
fig = ff.create_distplot(hist_data,group_labels,bin_size =[.1,.25,.5])  
st.plotly_chart(fig)

