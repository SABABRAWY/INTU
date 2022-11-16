#imports
from ast import Try
from email import header
from email.policy import HTTP
from tkinter.messagebox import QUESTION
from PIL import Image
import requests as rq
import streamlit as st
import datetime
st.title(""" H X H """)
st.header("WELCOME FRIENDS,")
col1,col2 = st.columns(2)
with col1: 
    st.header("please, we need some informations to help you in your search:")  
#user input (keyword):
    keyword = st.text_input("write the word u need to search: ")
    try:
        intkeyword = int(keyword)
        st.write('Please enter an alphabetical keyword.')
    except:
       pass

#user input (category):
    category = st.selectbox(
    'please, select your category',
    ["business", "entertainment","general","health","science","sports","technology","policy" ])

#user input (country):
    country = st.radio("select your country,please",
    ["eg","gb","jp","ru","us"])
    

#user input(date):
    Date = st.date_input(
    "enter datepublish u need: ")
    current_date = datetime.date.today()
    if Date > current_date:
       st.write("plz entre date <= current date")
   
with col2:
#user input(language):
    language = st.selectbox(
    "please, select your language",
    ['Arabic','English']
)
    langdict = {"Arabic":"ar", "English":"en"}
    urlLang = langdict[language]

#user input(articals):
    myRange = st.number_input("enter the number of articals to show: " ,value=80 )
    if myRange > 80:
       st.write("plz enter numbers < 80")
    if myRange <= 0:
       st.write("plz enter articals =>1")

    url = f"https://newsapi.org/v2/top-headlines?q={keyword}&country={country}&category{category}&apiKey=044cf6b279f6414daf14570e1c3c7b60"
    myRequest = rq.get(url)
    print(url)
  
#update on butten click:
    if st.button("click here"):
       url = f"https://newsapi.org/v2/top-headlines?q={keyword}&country={country}&category{category}&apiKey=044cf6b279f6414daf14570e1c3c7b60"
       myRequest = rq.get(url)
       st.write(url)
       for i in range (myRange):
          st.header(myRequest.json()["articles"][i]["title"])
          st.write("Author:....", myRequest.json()["articles"][i]["author"])
          st.write(myRequest.json()["articles"][i]["description"])    
    st.header("Now, you will find Top headliens in the field you are tooking for.")
    st.write("Thanks for your request.")