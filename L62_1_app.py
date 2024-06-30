import streamlit as st

#Title
st.title('Title  : Hello Friends, this is dheeraj reddy pasham')
#Header
st.header('Header : Hello Friends, this is dheeraj reddy pasham')
#Subheader
st.subheader('Subheader : Hello Friends, this is dheeraj reddy pasham')
#Text
st.text('Text : Hello Friends, this is dheeraj reddy pasham')

#Markdown
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

#succeded
st.success('Data is Submitted!')

#Information
st.info("Information!")

#Warning
st.warning("Warning!")

#Error
st.error("Error!")

#Exception
exp = ZeroDivisionError('Division is not possible ')
st.exception(exp)

#Help
st.help(ZeroDivisionError)

#Write
st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

#Code
st.code('x=10\n'
        'for i in range(x):\n'
        '        print(i)')

#Checkbox
st.checkbox('Male')
st.checkbox('female')

#Checkbox with validation
if(st.checkbox("Adult")):
    st.write("You are an adult")
    
#Radio
radioButton = st.radio('Select your gender :', ("Male","Female","Other"))   
if(radioButton == 'Male'):
    st.write("You are a male")
elif(radioButton == 'Female'):
    st.write("You are female")
else:
    st.write("You are an other gender")      
    
    
#Selectbox
st.subheader('Select Box:')
selectbox = st.selectbox("Data Science: ", ['Data Analysis','Web scraping','Machine Learning','Deep Learning','Natural language processing','Computer Vision','Image processing'])      
st.write('You have selected:' , selectbox) 

#Multiselect box
st.subheader('Multiselect box:')
mulSelBox = st.multiselect("Data Science: ", ['Data Analysis','Web scraping','Machine Learning','Deep Learning','Natural language processing','Computer Vision','Image processing'])      

st.write("You have selected:" ,len(mulSelBox), "courses")

#Button
st.subheader("Button:")
if(st.button("click me")):
    st.write("Thanks for Clicking me!")

#Slider
st.subheader("Slider:")
vol = st.slider("Select the volume",1,100,step = 1)
st.write("The volume is :", vol)

#Text Input
st.subheader("Text Input:")
username = st.text_input("Enter your name :")
password = st.text_input("Password :", type = 'password')
if (username):
    st.write("Hi", username)

#Text area
st.subheader("Text Area:")    
textArea = st.text_area("Write something about yourself in 20 words :")

# Count words in the text area
words_entered = textArea.split()
word_count = len(words_entered)

# Display current word count to the user
st.write("Current Word Count: ", word_count)

if word_count > 20:
    st.warning("You have exceeded the word limit (20 words). Please shorten your text.")

# Input-Number
st.subheader("Input Number:") 
st.number_input("Select your age",18,110)

# Input-Date
st.subheader("Input Date:") 
st.date_input("Select the date:")

#Input-Time
st.subheader("Input Time:")     
st.time_input("Time:")    





