import streamlit as st
from google.cloud import aiplatform
from datetime import datetime

# Initialize Google Cloud AI Platform 
aiplatform.init(project='elliptical-city-426011-t7', location='europe-west4 ')

# Define a function to call the AI model on GCP 
def predict_with_model(start_date, end_date, shift):

    # Create AI Platform prediction client
    endpoint = aiplatform.Endpoint(ptendpoint_name='projects/elliptical-city-426011-t7/locations/europe-west4/endpoints/3892002881489862656')

    # Prepare input data for the model
    instances = [{"start_date": start_date, "end_date": end_date, "shift": shift}]

    # Make predictionx  
    prediction = endpoint.predict(instances=instances) 
    return prediction

# Streamlit UI
st.title("Additive Manufacturing Shift Calculator")

# Date inputs
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Shift input
shift = st.number_input("Shifts per Day", min_value=1, step=1)

# Calculate button
if st.button("Calculate Total Shifts"):

    if start_date and end_date and shift:
        start_date_str = start_date.strftime('%Y-%m-%d') 
        end_date_str = end_date.strftime('%Y-%m-%d') 
        total_days = (end_date - start_date).days + 1 
        total_shifts = total_days * shift

# Display total shifts
        st.write(f'Total Shifts: {total_shifts}')

# Call the AI model for predictions
        prediction = predict_with_model(start_date_str, end_date_str, shift) 
        st.write("Model Prediction:", prediction)

    else:
        st.error("Please enter valid dates and shift values.")

if __name__ == '__main__': 

    st.write("Streamlit app is running!")



