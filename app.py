import streamlit as st
from google.cloud import aiplatform
from google.protobuf.json_format import ParseDict
from google.cloud.aiplatform_v1.types import PredictRequest
import json
import pandas as pd

# Initialize the AI Platform client
def get_prediction_client():
    return aiplatform.gapic.PredictionServiceClient()

# Function to get predictions from the deployed model
def get_model_prediction(instance, project_id, region, endpoint_id):
    client = get_prediction_client()
    endpoint = client.endpoint_path(project=project_id, location=region, endpoint=endpoint_id)

    # Ensure the instance is in the correct format
    instance_dict = json.loads(json.dumps(instance))  # Convert instance to dict if necessary
    instances = [instance_dict]

    request = PredictRequest(endpoint=endpoint, instances=instances)
    response = client.predict(request=request)

    return response.predictions

# Streamlit app
st.title("TruPrognostics Predictive Maintenance System")

# Input fields for user to enter data
st.header("Enter Machine Data")
temperature = st.number_input("Temperature (°C)", value=25.0)
vibration = st.number_input("Vibration Level", value=0.1)
pressure = st.number_input("Pressure (Pa)", value=101325.00)
operational_hours = st.number_input("Operational Hours", value=100.00)

# Collect the input data
input_data = [{
    "temperature": temperature,
    "vibration": vibration,
    "pressure": pressure,
    "operational_hours": operational_hours
}]


# Display input data
st.subheader("Input Data")
st.json(input_data)

# Predict button
if st.button("Predict Failure"):
    project_id = "elliptical-city-426011-t7"
    region = "europe-west4"
    endpoint_id = "3892002881489862656"

    try:
        prediction = get_model_prediction(input_data, project_id, region, endpoint_id)
        st.subheader("Prediction")
        st.write(prediction)

        # Further process the prediction if needed
        if prediction[0]["label"] == 1:
            st.error("Warning: Potential Failure Detected!")
        else:
            st.success("Machine is operating normally.")
    except Exception as e:
        st.error(f"Error: {e}")

# Google Cloud AI Platform initialization
if __name__ == "__main__":
    # Ensure the user has configured the Google Cloud environment properly
    st.write("Ensure you have authenticated with Google Cloud and set the project ID and endpoint ID correctly.")
