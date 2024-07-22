import os
from dotenv import load_dotenv
from google.generativeai import generativeai

load_dotenv()

# Set the environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")