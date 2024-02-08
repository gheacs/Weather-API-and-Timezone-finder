import streamlit as st
import datetime
from zoneinfo import ZoneInfo
import time
from hello import get_weather_data

# Create streamlit app
st.title("World Clock")
st.write("This app shows the current date, time and weather in different time zones.")

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
        #define the weather data
        weather_data = get_weather_data(timezone.split("/")[1] )
        
elif timezone == "Asia/Jakarta":
        current_time = get_current_time_and_date("Asia/Jakarta")
        st.subheader("Indonesia")
        st.image("Jakarta.jpeg", width=200)
        weather_data = get_weather_data(timezone.split("/")[1] )
        
elif timezone == "America/New_York":
        current_time = get_current_time_and_date("America/New_York")
        st.subheader("New York")
        st.image("new york.jpg", width=200)
        weather_data = get_weather_data(timezone.split("/")[1] )

time_display = st.empty() # create a container for the time
weather_display = st.empty() # create a container for the weather
time_display.text(f"The current time in {timezone} is {current_time}")        
time.sleep(1) # updated every 1 second
if weather_data:
        weather_display.text(f"Temperature: {weather_data['temperature']}°C, "
                             f"Humidity: {weather_data['humidity']}%, "
                             f"Description: {weather_data['description']}")
else: # if there was an error in fetching the weather data
        weather_display.text("Failed to fetch weather data")
