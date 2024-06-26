import streamlit as st
from PIL import Image


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
        
        'Component': ['Component-1', 'Component-2', 'Component-3'],
        'Failure_Probability': [0.1, 0.05, 0.2]
    })
    #datas = pd.concat([data, pd.date_range(start=start_date, end=end_date, freq='W')], axis=1) 
    return data

# Sidebar for user inputs
st.sidebar.header('User Inputs')
start_date = st.sidebar.date_input("Select Start Date")
end_date = st.sidebar.date_input("Select End Date", value=pd.to_datetime('today'))

# Simulate ERP data
erp_data = simulate_erp_data(start_date, end_date)

# Simulate IoT sensor data
iot_data = simulate_iot_data(start_date, end_date)

# Title of the app
st.title("Welcome to TruPrognostics")

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
        background-color: grey;
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

# Add some text or other elements below the logo
st.markdown("<div class='title'>Your partner in predictive maintenance for additive manufacturing.</div>", unsafe_allow_html=True)


# Display data in main section
st.title('ERP IoT Automate Workflow in Additive Manufacturing with Predictive Maintenance')
st.subheader('ERP Data')
st.write(erp_data)

st.subheader('IoT Sensor Data')
st.write(iot_data)


# Workflow automation section
st.header('Workflow Automation')

# Example of workflow automation with Streamlit buttons
if st.button('Run Scheduling Workflow'):
    # Replace with your workflow automation logic
    st.write('Scheduling workflow is running...')
    # Add your workflow steps here

    # Example: Simulate a scheduling action
    st.write('Scheduling complete.')

st.header('Additional Features')

# Add more features as neended
# Example: Data visualization
st.subheader('Visualization of IoT Data')
st.line_chart(iot_data.set_index('Date')['Temperature'])

# Example: User control for workflow
selected_order = st.selectbox('Select an Order', erp_data['Order'].unique())
if selected_order:
    st.write(f'Selected Order: {selected_order}')

# Example: Interactive plot based on user input
if st.checkbox('Show Pressure Data'):
    st.line_chart(iot_data.set_index('Date')['Pressure'])

# Simulate predictive maintenance data
maintenance_data = simulate_maintenance_data(start_date, end_date)

st.subheader('Predictive Maintenance Data')
st.write(maintenance_data)
