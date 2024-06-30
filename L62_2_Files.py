import streamlit as st 
import pandas as pd


# CSV files

st.subheader("Uploading the CSV file:")

df = st.file_uploader("Upload the CSV file:", type=['csv','xlsx'])
if df is not None:
    st.dataframe(df)
    
st.subheader("Loading the CSV file:")
df = pd.read_csv("/Users/dheerajreddypasham/Documents/GfG/Products.csv")
if df is not None:
    st.table(df.head())

   
# Images

st.subheader("Working with images :")

image_path = "/Users/dheerajreddypasham/Downloads/A1.jpg"

# Displaying the image from the file path
st.image(image_path, caption="Original Image")

# Uploading and displaying the user's image
uploaded_img = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

if uploaded_img is not None:
    st.image(uploaded_img, caption="Uploaded Image")
else:
    st.warning("Please upload an image")


# Videos

st.subheader("Working with videos :")

video_file = st.file_uploader("Upload the video file :", type = ["mkv","mp4"])
if video_file is not None:
    st.video(video_file, start_time = 0)
else:
    st.warning("Please upload an video")    
    
# Working with audio

st.subheader("Working with audios :")

audio_file = st.file_uploader("Upload the audio file :", type = ["wav","mp3"])
if audio_file is not None:
    st.audio(audio_file.read())
else:
    st.warning("Please upload an audio") 
    
    
    