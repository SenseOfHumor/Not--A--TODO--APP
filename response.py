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
history = '''User Query: Hi.
Response: Hello!'''


def askGemini(prompt):
    global history
    # template AKA system prompt
    template = '''
    You are a freindly chatbot.
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
    



