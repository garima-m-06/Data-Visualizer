import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#set page configuration
st.set_page_config(page_title="Data Visualizer",
                   layout="centered",
                   page_icon='📊')
#wide layout - content is fitted in the entire screen
#centered layout - content is in the center

#title
st.title("📊 Data Visualizer . Web App")

#setting a background image
def set_bg_from_url(url):
    style = f"""
    <style>
    .stApp {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

set_bg_from_url("https://images.stockcake.com/public/9/1/5/9158a5d0-8630-4c6a-b04b-e9fc34551f57/vibrant-data-visual-stockcake.jpg")

#working directory - we need to access the datasets in this directory
#When working with streamlit, this won't be our default working directory, so
#when working with datasets we need to give their full path. So we are not hardcoding this path
#but giving the absolute path (the absolute path of main.py's directory)
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data" #join the data folder

#list the files present in data folder
#we have a for loop and os.listdir - will return all the files in that directory ending with .csv
files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#dropdown for all the files
#index = None - no files selected by default initially
selected_file = st.selectbox("Select a File", files, index=None) #give the label and list of files

if selected_file is not None:
    #get the complete path of the file
    file_path = os.path.join(folder_path, selected_file)

    #reading the csv file as pandas dataframe
    df = pd.read_csv(file_path)
    #display the sample of dataframe
    col1, col2 = st.columns(2) #2 columns - 1 for data display, 1 for axis selection

    columns = df.columns.tolist() #create a list of all the columns in the dataframe

    with col1:
        st.write(" ")
        st.write(df.head())

    with col2:
        #user selection
       x_axis = st.selectbox("Select X Axis", options = columns + ["None"], index=None)
       y_axis = st.selectbox("Select Y Axis", options = columns + ["None"], index=None)

       plot_list = ['Line Plot','Bar Chart', 'Scattered Plot', 'Distributed Plot', 'Count Plot']

       selected_plot = st.selectbox("Select Plot", options = plot_list, index=None)

       st.write(x_axis)
       st.write(y_axis)
       st.write(selected_plot)

    #button tp generate plots
    if  st.button("Generate Plot"):

        fig, ax = plt.subplots(figsize=(6,4)) #will create a figure and base axis

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == "Scattered Plot":
            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)

        elif selected_plot == ("Distributed Plot"):
            sns.histplot(x=df[x_axis], kde=True, ax=ax)
            #smoothens the curve on the histogram

        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], kde=True, ax=ax)

        #adjust label sizes
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        #title axes labels
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(f"{x_axis}", fontsize=12)
        plt.ylabel(f"{y_axis}", fontsize=12)

        st.pyplot(fig)













