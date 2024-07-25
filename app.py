import streamlit as st
#from NLP import *
#from task import *
from CRUD import *
from streamlit_extras.stodo import to_do


def TODO(task, emoji, key):
    to_do(
        [(st.write,f":{emoji}: {task}")],  
        f"{key}",                              
    )

st.title("Not a To Do List")
st.write("Just type in what you want to do and I'll create a task for you")
st.write("______________________________________________________________________")

st.sidebar.title("How can i help you today?")
st.sidebar.write("ask me to optimize your day")
st.sidebar.write("______________________________________________________________________")
side_task = st.sidebar.chat_input("What do you want to do?",key = "2")
main_task = st.chat_input("What do you want to do?", key = "1")

count = 0
MAX = 15
## Pop up a message to the user
if main_task:
    st.toast("Task created succesfully")
    response = askGemini(main_task)
    st.write(response)

