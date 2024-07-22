import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

#configure the API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-pro')


def askGemini(prompt):
    # template AKA system prompt
    template = '''
    You will analyze what the user is saying, extract the information to create a ToDo list item.
    You will only extract the task from the response and you will assign an appropriate emoji 
    to the task (the emoji should be in a text format) and a key which should be a placeholder (relatd to the task for identification and not an emoji). 
    Do not entertain any other question the user might ask.
    Your output should STRICTLY be in this format: task,emoji,key.    (no spaces before or after the comma)
    Here is the user prompt: {prompt}
    '''

    complete_prompt = f"{template.format(prompt = prompt)}"
    response = model.generate_content(complete_prompt)

    res = response.text
    new_res = res.strip('\n').strip(" ")
    lst = new_res.split(',')

    return lst

# print(askGemini("I want to ask her out for a date"))
