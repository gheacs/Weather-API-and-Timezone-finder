import streamlit as st
import datetime
from zoneinfo import ZoneInfo

# Create streamlit app
st.title("World Clock")
st.write("This app shows the current time in different time zones.")

# Get current time
Seattle_current_time = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))
Indonesia_current_time = datetime.datetime.now(ZoneInfo("Asia/Jakarta"))
New_York_current_time = datetime.datetime.now(ZoneInfo("America/New_York"))

# Show time in different time zones in the app
st.write("Current time in Seattle:", Seattle_current_time.strftime("%H:%M:%S"))
st.write("Current time in Indonesia:", Indonesia_current_time.strftime("%H:%M:%S"))
st.write("Current time in New York:", New_York_current_time.strftime("%H:%M:%S"))

