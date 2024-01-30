import streamlit as st
import datetime
from zoneinfo import ZoneInfo
import time

# Create streamlit app
st.title("World Clock")
st.write("This app shows the current time and date in different time zones.")

# Get Current Time
def get_current_time_and_date(timezone):
    current_time = datetime.datetime.now(ZoneInfo(timezone))
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


Seattle_current_time = get_current_time_and_date("America/Los_Angeles")
Indonesia_current_time = get_current_time_and_date("Asia/Jakarta")
New_York_current_time = get_current_time_and_date("America/New_York")

# Visualize
st.subheader("Seattle")
st.image("Seattle.jpg", width=200)
seattle_time_display = st.text(Seattle_current_time)

st.subheader("Indonesia")
st.image("Jakarta.jpeg", width=200)
indonesia_time_display = st.text(Indonesia_current_time)

st.subheader("New York")
st.image("new york.jpg", width=200)
new_york_time_display = st.text(New_York_current_time)

# set refresh interval
refresh_interval = 30  # 30 minutes

while True:
    time.sleep(refresh_interval * 60)  # Sleep for 30 minutes
    # Update the time and date displays with the current time and date
    Seattle_current_time = get_current_time_and_date("America/Los_Angeles")
    Indonesia_current_time = get_current_time_and_date("Asia/Jakarta")
    New_York_current_time = get_current_time_and_date("America/New_York")
    
    seattle_time_display.text(Seattle_current_time)
    indonesia_time_display.text(Indonesia_current_time)
    new_york_time_display.text(New_York_current_time)
