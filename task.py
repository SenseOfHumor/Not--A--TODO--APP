from streamlit_extras.stodo import to_do

import streamlit as st

st.title("To Do List")


def TODO(task, emoji, key):
    to_do(
        [(st.write,f":{emoji}: {task}")],  ## The main heading 
        f"{key}",                              ## The emoji
    )


## implementation
    
'''
TODO("Write a blog post", "pencil", "1")
TODO("Create a new project", "rocket", "2")
'''