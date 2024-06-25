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
import streamlit as st





# Input fields in the left column

project_id = st.sidebar.text_input("Google Cloud Project ID")
endpoint_id = st.sidebar.text_input("AI Platform Endpoint ID")
google_id = st.sidebar.text_input("Google ID")

machine_data = {}
machine_data['temperature'] = st.number_input("Temperature", step=0.1)
machine_data['pressure'] = st.number_input("Pressure", step=0.1)
machine_data['vibration'] = st.number_input("Vibration", step=0.01)
# Footer
st.write("")
st.write("")
st.write("")
st.write("Follow Us On:LinkedIn information Solutions Vision Imprint Blog About Company +49 (0)1622443256 ,Info@sam3dp.tech Gubener Strasse 3B 10243 Berlin ")
st.write('This Streamlit app demonstrates predictive maintenance for additive manufacturing using Google Cloud AI Platform.')
st.write('Learn more about this project at https://www.sam3dp.tech')  # Replace with your project URL

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
