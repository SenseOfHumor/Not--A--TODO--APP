import os
from dotenv import load_dotenv
import google.generativeai as genai
#from task import *

load_dotenv()

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.0-pro')

## creating a history of the tasks, user query, and the response
history = '''User Query: help me out with my tasks please.
Response: Sure, On it.'''


def askGemini(prompt):
    global history
    # template AKA system prompt
    template = '''
    You will analyze what the user is saying, extract the information to create a ToDo list item.
    you will extract the key information from the user input and create tasks in the following way
    a list of list, there are 3 operations, create, update, delete. This should be the first key for 
    every list inside the main list. The list will also have a unique identification number (UID) which
    will start from 1 for the first task, and increment each time a new task is created, updated, or deleted.
    each operation will vary a little bit, for example, create will have 
    the following structure -> [create, task, time, UID]
    update will have the following structure -> [update, UID (of the task to be updated), task, time, UID(old UID of the task)]
    delete will have the following structure -> [delete, UID (of the task to be deleted)]
    The user may give multiple tasks at once, so you will have to extract the information and create the tasks accordingly.
    The user may also give some tasks that are already present in the list, in that case, you will have to update the task.
    You will do your best to understand and extract the information, if there is no similar task to update, only then 
    you will create a new task.
    The user may sometime make error while giving you information, in that case, you will follow the following steps ->
    1. if no command is given (ex. something to create, update, or delete), then you will create a task with 'empty' in the other sections.
    2. if the user gives you a task that is not present in the list, then you will create a new task.
    3. if no task is given, then you will create a task with 'empty' in the task section.
    4. if not task and time is given, then you will create a task with 'empty' in the task and time section.
    5. if no time is given, then you will create a task with 'No Time allocated' in the time section.
    6. if only update is given, then you will create a task with 'empty' in all the sections with a new UID.

    a case -> lets say the user asks you to create a task about brushing their teeh at a certain time
    but late, says they dont wanna do it anymore, so you should not create a new task but delete the old one. and nothing to update.
    You will only respond with the list of lists in plain text, and nothing else.
    Good Luck!
    Here is the user prompt: {prompt}
    Here is the history of the tasks, user query, and the response: {history}
    '''

    complete_prompt = f"{template.format(prompt = prompt, history = history)}"
    response = model.generate_content(complete_prompt)

    res = response.text

    ## updating the history
    history += f"User Query: {prompt}\nResponse: {res}\n"
    

    return res

while True:
    print(askGemini(input("what do you want to do?: ")))
    



