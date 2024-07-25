
import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Hardcoded OAuth 2.0 credentials
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_SECRET")
REDIRECT_URI = "https://nottodo.streamlit.app"  # Make sure this matches the registered URI

# Configure the OAuth 2.0 flow
flow = Flow.from_client_config(
    client_config={
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [REDIRECT_URI]
        }
    },
    scopes=['https://www.googleapis.com/auth/calendar.readonly']
)

# Streamlit UI
st.title("Google Calendar Integration")

# Button to start the OAuth 2.0 flow
if st.button("Authorize with Google"):
    auth_url, _ = flow.authorization_url(prompt='consent')
    st.markdown(f"[Click here to authorize]({auth_url})")

# Input field for the authorization code
code = st.text_input("Enter the authorization code:")

if code:
    flow.fetch_token(code=code)
    credentials = flow.credentials

    # Display the access token (for demonstration purposes)
    st.write(f"Access Token: {credentials.token}")

    # Use the credentials to build the Google Calendar service
    service = build('calendar', 'v3', credentials=credentials)

    # Fetch and display events
    events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        st.write("No upcoming events found.")
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            st.write(f"{start}: {event['summary']}")
