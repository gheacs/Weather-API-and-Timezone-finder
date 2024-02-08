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
        
elif timezone == "Asia/Jakarta":
        current_time = get_current_time_and_date("Asia/Jakarta")
        st.subheader("Indonesia")
        st.image("Jakarta.jpeg", width=200)
        
elif timezone == "America/New_York":
        current_time = get_current_time_and_date("America/New_York")
        st.subheader("New York")
        st.image("new york.jpg", width=200)

time_display = st.empty() # create a placeholder for the time
time_display.text(f"The current time in {timezone} is {current_time}")        
time.sleep(1) # updated every 1 second
