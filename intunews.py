#imports
from ast import Try
from email import header
from email.policy import HTTP
from tkinter.messagebox import QUESTION
import requests as rq
import streamlit as st
import datetime

st.title(""" H X H """)

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
    ["business", "entertainment","general","health","science","sports","technology" ])
#st.write('You selected:', category)

#user input (country):
country = st.radio("select your country,please",
    ["United Kingdom","Japan","Russia"])
#st.write('You selected:', country)
coundict = {"Egypt":"eg","us":"America","United Kingdom":"gb","Japan":"jp","Russia":"ru"}
urlcount = coundict[country]

#user input(date):
Date = st.date_input(
    "enter datepublish u need: ")
current_date = datetime.date.today()
if Date > current_date:
    st.write("plz entre date <= current date")

#user input(language):
#language = st.selectbox(
   # "please, select your language",
  #  ['Arabic','English']
#)
#langdict = {"Arabic":"ar", "English":"en"}
#urlLang = langdict[language]

#user input(articals):
myRange = st.number_input("enter the number of articals to show: " ,value=40 )
if myRange > 40:
    st.write("plz enter numbers < 40")
if myRange <= 0:
    st.write("plz enter articals =>1")
#if  type (myRange) == float(myRange):
    #st.write("plz enter an int numbers")

#user input(sorted by):
#sortBy = st.selectbox("enter the type of sorted data u need,please" ,['relevancy','popularity','publishedAt']  ) 


pagesize = st.text_input("enter number of page u need: ")
try:
    flpagesize = float(pagesize)
    st.write("plz enter an int number")
except:
    pass
  
    
url = f"https://newsapi.org/v2/top-headlines?q={keyword}&country={urlcount}&category{category}&pageSize{pagesize}&apiKey=044cf6b279f6414daf14570e1c3c7b60"
myRequest = rq.get(url)
print(url)
  
#update on butten click:
if st.button("click here"):
    url = f"https://newsapi.org/v2/top-headlines?q={keyword}&country={urlcount}&category{category}&pageSize{pagesize}&apiKey=044cf6b279f6414daf14570e1c3c7b60"
    myRequest = rq.get(url)
    st.write(url)
    for i in range (myRange):
       st.header(myRequest.json()["articles"][i]["title"])
       st.write("Author:....", myRequest.json()["articles"][i]["author"])
       st.write(myRequest.json()["articles"][i]["description"])    
