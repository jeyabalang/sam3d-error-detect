# # import requests

# # # Fetch data from an external source (e.g., IoT device or web API)
# # def get_data():
# #     response = requests.get('http://your_api_endpoint')
# #     data = response.json()
# #     return pd.DataFrame({
# #         'timestamp': [pd.Timestamp.now()],
# #         'temperature': [data['temperature']],
# #         'humidity': [data['humidity']],
# #         'vibration': [data['vibration']],
# #         'pressure': [data['pressure']]
# #     })
# # #```

# # ### Adding More Features

# # #You can add more features to your app, such as alerts for abnormal values, historical data analysis, or more detailed visualizations.

# # #### Adding Alerts

# # #For instance, if you want to add alerts when certain thresholds are crossed:

# # #```python
# # # Real-time data update loop
# # while True:
# #     # Get new data
# #     new_data = get_data()
# #     
# #     # Append new data to the existing dataframe
# #     data = pd.concat([data, new_data])
# #     
# #     # Display the updated dataframe
# #     data_placeholder.dataframe(data)
# #     
# #     # Check for alerts
# #     if new_data['temperature'].values[0] > 240:
# #         st.error('Temperature is too high!')
# #     
# #     if new_data['humidity'].values[0] > 45:
# #         st.error('Humidity is too high!')
# #     
# #     if new_data['vibration'].values[0] > 0.8:
# #         st.error('Vibration levels are too high!')
# #     
# #     if new_data['pressure'].values[0] > 9:
# #         st.error('Pressure is too high!')
# #     
# #     # Display line charts of the data
# #     st.subheader('Temperature Over Time')
# #     chart_placeholder.line_chart(data.set_index('timestamp')['temperature'])
# #     
# #     st.subheader('Humidity Over Time')
# #     chart_placeholder.line_chart(data.set_index('timestamp')['humidity'])
# #     
# #     st.subheader('Vibration Over Time')
# #     chart_placeholder.line_chart(data.set_index('timestamp')['vibration'])
# #     
# #     st.subheader('Pressure Over Time')
# #     chart_placeholder.line_chart(data.set_index('timestamp')['pressure'])
# #     
# #     # Add a small delay to simulate real-time data streaming
# #     time.sleep(1)


# # First, ensure you have Streamlit and any other necessary libraries installed. If not, you can install them using pip:
# # ```bash
# # pip install streamlit pandas numpy ```
# # ### 2. Create the Streamlit App
# # Create a new Python file, `app.py`, for your Streamlit app. Here’s an example of a real-time monitoring app for an additive manufacturing process:
# # ```python
# import streamlit as st 
# import pandas as pd
# import numpy as np 
# import time
# # Title of the Streamlit app
# st.title('Real-Time Monitoring Dashboard for Additive Manufacturing')
# # Simulated data function def get_data():
# # Simulate data from the additive manufacturing process return pd.DataFrame({
# 'timestamp': [pd.Timestamp.now()],
# 'temperature': [np.random.uniform(150, 250)], # example temperature range in Celsius
# 'humidity': [np.random.uniform(20, 50)], 'vibration': [np.random.uniform(0, 1)], 'pressure': [np.random.uniform(1, 10)]
# # example humidity range in percentage # example vibration level
# # example pressure range in bar
# # Placeholder for the dataframe data_placeholder = st.empty() chart_placeholder = st.empty()
# # Initialize an empty dataframe
# data = pd.DataFrame(columns=['timestamp', 'temperature', 'humidity', 'vibration', 'pressure'])
# # Real-time data update loop while True:
# # Get new data new_data = get_data()
# # Append new data to the existing dataframe data = pd.concat([data, new_data])
# # Display the updated dataframe data_placeholder.dataframe(data)
# # Display line charts of the data
# st.subheader('Temperature Over Time') chart_placeholder.line_chart(data.set_index('timestamp')['temperature'])
# st.subheader('Humidity Over Time') chart_placeholder.line_chart(data.set_index('timestamp')['humidity'])
# st.subheader('Vibration Over Time') chart_placeholder.line_chart(data.set_index('timestamp')['vibration'])
# st.subheader('Pressure Over Time') chart_placeholder.line_chart(data.set_index('timestamp')['pressure'])
# # Add a small delay to simulate real-time data streaming
# time.sleep(1) ```


#### 1. Set Up GCP IoT Core#
#1. **Create IoT Core Registry**: This will manage your devices. 2. **Register Devices**: Add your IoT devices to the registry.
#### 2. Publish Data from IoT Devices to Pub/Sub
#Use the Google Cloud IoT Device SDK to send data from your IoT devices to Google Cloud Pub/Sub.
#```python
from google.cloud import pubsub_v1
def publish_message(project_id, topic_id, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, message.encode('utf-8')) 
    future.result()
    # Example usage
    project_id = 'your-project-id'
    topic_id = 'your-topic-id'
    message = 'Hello, IoT!'
    publish_message(project_id, topic_id, message) 
#### 3. Store Data in Firestore
#Set up Firestore to store and query the data collected from your IoT devices.
#```python
from google.cloud import firestore
def store_data(collection_name, data):
    db = firestore.Client()
    doc_ref = db.collection(collection_name).document() 
    doc_ref.set(data)
# Example usage 
data = {
'temperature': 22.5,
'humidity': 55,
'timestamp': firestore.SERVER_TIMESTAMP
}
store_data('iot-data', data) 
#### 4. Create Streamlit Dashboard
#Create a Streamlit application to visualize and interact with the IoT data.
#```python
import streamlit as st
import pandas as pd
from google.cloud import firestore
def get_data(collection_name):
    db = firestore.Client()
    docs = db.collection(collection_name).stream() 
    data = [doc.to_dict() for doc in docs]
    return pd.DataFrame(data)
st.title('IoT-Based ERP Dashboard')

# Fetch data from Firestore
data = get_data('iot-data')
if not data.empty: 
    st.write('Real-time IoT Data') 
    st.dataframe(data)
else:
    st.write('No data available.')
# Customizable alerts example
threshold = st.slider('Temperature Threshold', 0, 100, 25)
if any(data['temperature'] > threshold):
    st.warning('Temperature threshold exceeded!') 
# Load the logo image
logo_path = "photo_2024-06-22 12.10.05.jpeg"  # Adjust the path to your logo file
logo = Image.open(logo_path)

# Display the logo
st.image(logo, width=150)  # Adjust width as needed

# CSS for additional formatting (optional)
st.markdown(
    """
    <style>
    .main {
        background-color: orange;
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
