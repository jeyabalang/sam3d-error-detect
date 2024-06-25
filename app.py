import streamlit as st
from google.cloud import aiplatform
from google.auth import credentials

# Function to make predictions using the AI Platform
def predict_with_model(project_id, endpoint_id, machine_data):
    client = aiplatform.gapic.PredictionServiceClient()

    # The AI Platform endpoint path
    endpoint = client.endpoint_path(
        project=project_id,
        location='europe-west4',
        endpoint=endpoint_id
    )

    # Input data in the format expected by the model
    instance = {"data": machine_data}
    instances = [instance]
    
    # Call the AI Platform model for prediction
    response = client.predict(
        endpoint=endpoint,
        instances=instances,
    )
    
    return response.predictions

# Streamlit UI components
st.title("TruPrognostics Predictive Maintenance System")

project_id = st.text_input("Google Cloud Project ID")
endpoint_id = st.text_input("AI Platform Endpoint ID")
google_id = st.text_input("Google ID")

machine_data = {}
machine_data['temperature'] = st.number_input("Temperature", step=0.1)
machine_data['pressure'] = st.number_input("Pressure", step=0.1)
machine_data['vibration'] = st.number_input("Vibration", step=0.01)

if st.button("Submit"):
    if not project_id or not endpoint_id or not google_id:
        st.error("Please provide all required inputs.")
    else:
        try:
            # Make prediction
            prediction = predict_with_model(project_id, endpoint_id, machine_data)
            st.write("Prediction:", prediction)
        except Exception as e:
            st.error(f"Error: {e}")
