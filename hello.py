import streamlit as st
import datetime
from zoneinfo import ZoneInfo

# Create streamlit app
st.title("World Clock")
st.write("This app shows the current time in different time zones.")

# Get date and current time
Seattle_current_time = datetime.datetime.now(ZoneInfo("America/Los_Angeles"))
Indonesia_current_time = datetime.datetime.now(ZoneInfo("Asia/Jakarta"))
New_York_current_time = datetime.datetime.now(ZoneInfo("America/New_York"))


# Visualize the time in different time zones
st.write("Seattle")
st.write("Indonesia")
st.write("New York")

# Create a clock for each time zone
st.write(Seattle_current_time.strftime("%H:%M:%S"))
st.write(Indonesia_current_time.strftime("%H:%M:%S"))
st.write(New_York_current_time.strftime("%H:%M:%S"))

# Add images
st.image("https://www.pngkey.com/png/full/114-1149878_seattle-skyline-seattle-skyline-silhouette-png.png", width=300)
st.image("https://www.pngkey.com/png/full/114-1149878_seattle-skyline-seattle-skyline-silhouette-png.png", width=300)
st.image("https://www.pngkey.com/png/full/114-1149878_seattle-skyline-seattle-skyline-silhouette-png.png", width=300)

