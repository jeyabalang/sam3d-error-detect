# import requests

# # Fetch data from an external source (e.g., IoT device or web API)
# def get_data():
#     response = requests.get('http://your_api_endpoint')
#     data = response.json()
#     return pd.DataFrame({
#         'timestamp': [pd.Timestamp.now()],
#         'temperature': [data['temperature']],
#         'humidity': [data['humidity']],
#         'vibration': [data['vibration']],
#         'pressure': [data['pressure']]
#     })
# #```

# ### Adding More Features

# #You can add more features to your app, such as alerts for abnormal values, historical data analysis, or more detailed visualizations.

# #### Adding Alerts

# #For instance, if you want to add alerts when certain thresholds are crossed:

# #```python
# # Real-time data update loop
# while True:
#     # Get new data
#     new_data = get_data()
#     
#     # Append new data to the existing dataframe
#     data = pd.concat([data, new_data])
#     
#     # Display the updated dataframe
#     data_placeholder.dataframe(data)
#     
#     # Check for alerts
#     if new_data['temperature'].values[0] > 240:
#         st.error('Temperature is too high!')
#     
#     if new_data['humidity'].values[0] > 45:
#         st.error('Humidity is too high!')
#     
#     if new_data['vibration'].values[0] > 0.8:
#         st.error('Vibration levels are too high!')
#     
#     if new_data['pressure'].values[0] > 9:
#         st.error('Pressure is too high!')
#     
#     # Display line charts of the data
#     st.subheader('Temperature Over Time')
#     chart_placeholder.line_chart(data.set_index('timestamp')['temperature'])
#     
#     st.subheader('Humidity Over Time')
#     chart_placeholder.line_chart(data.set_index('timestamp')['humidity'])
#     
#     st.subheader('Vibration Over Time')
#     chart_placeholder.line_chart(data.set_index('timestamp')['vibration'])
#     
#     st.subheader('Pressure Over Time')
#     chart_placeholder.line_chart(data.set_index('timestamp')['pressure'])
#     
#     # Add a small delay to simulate real-time data streaming
#     time.sleep(1)


# First, ensure you have Streamlit and any other necessary libraries installed. If not, you can install them using pip:
# ```bash
# pip install streamlit pandas numpy ```
# ### 2. Create the Streamlit App
# Create a new Python file, `app.py`, for your Streamlit app. Here’s an example of a real-time monitoring app for an additive manufacturing process:
# ```python
import streamlit as st 
import pandas as pd
import numpy as np 
import time
from PIL import Image
# Load the logo image
logo_path = "photo_2024-06-22 12.10.05.jpeg"  # Adjust the path to your logo file
logo = Image.open(logo_path)

# Display the logo
st.image(logo, caption='Licensed by Sam3dp.tech', width=150)   # Adjust width as needed

# CSS for additional formatting (optional)
st.markdown(
    """
    <style>
    .main {
        background-color: purple;
        font-family: Arial, sans-serif;
    }
    .title {
        font-size: 2em;
        color: #333;
        text-align: center;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the Streamlit app
st.title('Real-Time Monitoring Dashboard for Additive Manufacturing')
# Adding Bootstrap CSS
st.markdown(
    """
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Simulated data function 
def get_data():
# Simulate data from the additive manufacturing process 
  return pd.DataFrame({
    'timestamp': [pd.Timestamp.now()],
    'temperature': [np.random.uniform(150, 250)], # example temperature range in Celsius
    'humidity': [np.random.uniform(20, 50)], 
    'vibration': [np.random.uniform(0, 1)], 
    'pressure': [np.random.uniform(1, 10)]
   })
# example humidity range in percentage # example vibration level
# example pressure range in bar
# Placeholder for the dataframe
data_placeholder = st.empty() 
chart_placeholder = st.empty()
# Initialize an empty dataframe
data = pd.DataFrame(columns=['timestamp', 'temperature', 'humidity', 'vibration', 'pressure'])
st.subheader('Temperature, Humidity, and Vibration for Additive Manufacturing Using a Line Chart Over Time')

# Real-time data update loop 
while True:
# Get new data 
  new_data = get_data()
# Append new data to the existing dataframe 
  data = pd.concat([data, new_data])
# Display the updated dataframe 
  data_placeholder.dataframe(data)  

# Display line charts of the data
 
  chart_placeholder.line_chart(data.set_index('timestamp')['temperature'])
  
  chart_placeholder.line_chart(data.set_index('timestamp')['humidity'])

  chart_placeholder.line_chart(data.set_index('timestamp')['vibration'])
  
  chart_placeholder.line_chart(data.set_index('timestamp')['pressure'])
  # Add a small delay to simulate real-time data streaming
  time.sleep(1) 

# Check for alerts
  if new_data['temperature'].values[0] > 240:
     st.error('At over 240!, the Temperature is extremely high')
  if new_data['humidity'].values[0] > 45: 
     st.error('At over 45!, the Humidity is extremely high')
  if new_data['vibration'].values[0] > 0.8: 
     st.error('At over 0.8!, the Vibration is extremely high')
  if new_data['pressure'].values[0] > 9: 
    st.error('At over 9!, the Pressure is extremely high')
    # Display line charts of the data
    chart_placeholder.line_chart(data.set_index('timestamp')['temperature'])
    chart_placeholder.line_chart(data.set_index('timestamp')['humidity'])
    chart_placeholder.line_chart(data.set_index('timestamp')['vibration'])
    chart_placeholder.line_chart(data.set_index('timestamp')['pressure'])

# Add a small delay to simulate real-time data streaming
    time.sleep(1) 
### Conclusion
# This example provides a foundation for building a real-time monitoring dashboard for an additive manufacturing process using Streamlit. Customize the data fetching logic, visualizations, and additional features to match your specific needs. If you need further customization or encounter any issues, feel free to ask for additional help!
# created by,
# Jeyabalan Ganesh Nadar
