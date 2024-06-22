# import joblib

# # Load the model from .pkl file
# model = joblib.load('Machine_failure_model.pkl')

# import tensorflow as tf

# # Convert the model to TensorFlow's protobuf format (.pb)
# tf.saved_model.save(model, 'Machine_failure_model.pb')

# # Load the converted model
# loaded_model = tf.saved_model.load('Machine_failure_model.pb')

# # Check the model's signatures
# print(list(loaded_model.signatures.keys()))  # This should show the available signatures or functions

# # Example: Run inference with the loaded model
# result = loaded_model.predict(...)  # Replace with your prediction logic
# print(result)

# import torch
# import torch.nn as nn
# import torch.optim as optim
# from sklearn.metrics import accuracy_score

# # Assuming you have a PyTorch model and a DataLoader
# model = MyPyTorchModel()
# criterion = nn.CrossEntropyLoss()
# optimizer = optim.Adam(model.parameters(), lr=0.001)

# # Evaluation function
# def evaluate(model, dataloader):
#     model.eval()
#     all_preds = []
#     all_targets = []
#     with torch.no_grad():
#         for inputs, targets in dataloader:
#             outputs = model(inputs)
#             _, preds = torch.max(outputs, 1)
#             all_preds.extend(preds.cpu().numpy())
#             all_targets.extend(targets.cpu().numpy())
    
#     accuracy = accuracy_score(all_targets, all_preds)
#     return accuracy

# import warnings
# from sklearn.exceptions import InconsistentVersionWarning

# warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


# # Example usage
# test_accuracy = evaluate(model, test_loader)
# print(f'Test Accuracy: {test_accuracy}')

# Jeyabalan Nadar, [18. Jun 2024 at 16:44:54]:
# Temperature, Humidity,Vibration over time period for the Additive Manufacturing with line_chart

# Temperature, Humidity, and Vibration for Additive Manufacturing Using a Line Chart Over Time

# Jeyabalan Nadar, [19. Jun 2024 at 14:59:21]:
# To create a Streamlit Python code for ERP IoT smart scheduling in additive manufacturing with predictive maintenance, you can implement logical interaction elements for user input or control. Here's an outline of how you might structure it:

import streamlit as st
import pandas as pd

# Function to simulate ERP data
def simulate_erp_data(start_date, end_date):
    # Replace with your ERP data simulation logic
    data = pd.DataFrame({
        'Date': pd.date_range(start=start_date, end=end_date, freq='D'),
        'Order': [f'Order-{i}' for i in range(1, (end_date - start_date).days + 2)],
        'Quantity': [10 * i for i in range(1, (end_date - start_date).days + 2)]
    })
    return data

# Function to simulate IoT sensor data
def simulate_iot_data(start_date, end_date):
    # Replace with your IoT data simulation logic
    data = pd.DataFrame({
        'Date': pd.date_range(start=start_date, end=end_date, freq='H'),
        'Temperature': [25.0 + 10 * (i % 24) / 24 for i in range((end_date - start_date).days * 24 + 1)],
        'Pressure': [1.0 + 0.5 * (i % 24) / 24 for i in range((end_date - start_date).days * 24 + 1)]
    })
    return data

# Function to simulate predictive maintenance data
def simulate_maintenance_data(start_date, end_date):
    # Replace with your predictive maintenance data simulation logic
    data = pd.DataFrame({
        #'Date': pd.date_range(start=start_date, end=end_date, freq='W'),
        'Component': ['Component-1', 'Component-2', 'Component-3'],
        'Failure_Probability': [0.1, 0.05, 0.2]
    })
    return data

# Sidebar for user inputs
st.sidebar.header('User Inputs')
start_date = st.sidebar.date_input("Select Start Date")
end_date = st.sidebar.date_input("Select End Date", value=pd.to_datetime('today'))

# Simulate ERP data
erp_data = simulate_erp_data(start_date, end_date)

# Simulate IoT sensor data
iot_data = simulate_iot_data(start_date, end_date)

# Display data in main section
st.title('ERP IoT Smart Scheduling for Additive Manufacturing with Predictive Maintenance')
st.subheader('ERP Data')
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

st.write(erp_data)

st.subheader('IoT Sensor Data')
st.write(iot_data)

# Simulate predictive maintenance data
maintenance_data = simulate_maintenance_data(start_date, end_date)

st.subheader('Predictive Maintenance Data')
st.write(maintenance_data)
### Logical Interaction Elements:
# 1. Date Inputs: Allow users to select start and end dates for data simulation.
# 2. Sidebar: Use Streamlit's sidebar to place input controls for dates.
# 3. Data Simulation Functions: Simulate ERP, IoT sensor, and predictive maintenance data.
# 4. Display Data: Display the simulated dataframes in the main section using st.write().

# ### Additional Elements to Consider:
# - Data Visualization: Use Streamlit's interactive plotting capabilities (st.line_chart(), st.bar_chart(), etc.) to visualize data trends.
# - User Controls: Implement sliders, dropdowns, and checkboxes to allow users to filter and explore data dynamically.
# - Integration: Integrate with your existing ERP, IoT, and predictive maintenance systems using APIs or data connectors.

# This structure provides a foundation to start building your Streamlit app for ERP IoT smart scheduling in additive manufacturing with predictive maintenance. Adjust the simulation logic and data sources as per your application's requirements.

