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

#create dropdown
timezone = st.selectbox("Select Timezone", ["America/Los_Angeles", "Asia/Jakarta", "America/New_York"])

# filter the timezones based on the selected timezone
if timezone == "America/Los_Angeles":
        current_time = get_current_time_and_date("America/Los_Angeles")
        st.subheader("Seattle / Los Angeles")
        st.image("Seattle.jpg", width=200)
        seattle_time_display = st.text(Seattle_current_time)
elif timezone == "Asia/Jakarta":
        current_time = get_current_time_and_date("Asia/Jakarta")
        st.subheader("Indonesia")
        st.image("Jakarta.jpeg", width=200)
        indonesia_time_display = st.text(Indonesia_current_time)    
elif timezone == "America/New_York":
        current_time = get_current_time_and_date("America/New_York")
        st.subheader("New York")
        st.image("new york.jpg", width=200)
        new_york_time_display = st.text(New_York_current_time)  

