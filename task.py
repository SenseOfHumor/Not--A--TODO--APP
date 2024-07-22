from streamlit_extras.stodo import to_do

import streamlit as st

st.title("To Do List")


def TODO(task, emoji, key):
    to_do(
        [(st.write,f":{emoji}: {task}")],  ## The main heading 
        f"{key}",                              ## The emoji
    )


TODO("have a milkshake", "🥛", 42) 

#TODO have to make overloaded fucntions for different use cases like no date, no time, or crazier -> no task