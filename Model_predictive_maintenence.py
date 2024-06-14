# To create a model for the Additive Manufacturing Shift Calculator in the context
# of IoT Python predictive maintenance software, you'll need to define the
# specific requirements and inputs for your calculator. Here’s a basic outline to
# get you started:
# ### Step 1: Define the Problem
# The Additive Manufacturing Shift Calculator should help predict maintenance
# needs based on various parameters. This could include usage patterns, machine
# data, environmental conditions, and historical maintenance records.
# ### Step 2: Collect Data
# Gather the relevant data needed for your model:
# - Machine usage data (e.g., operating hours, print counts)
# - Environmental data (e.g., temperature, humidity)
# - Historical maintenance records (e.g., failure times, types of maintenance
# performed)
# - Sensor data (e.g., vibration, sound levels)
# ### Step 3: Preprocess Data
# Ensure your data is clean and preprocessed correctly. This might involve
# handling missing values, normalizing data, and encoding categorical variables.
# ### Step 4: Develop the Model
# Here's a basic Python code outline to build a predictive maintenance model using
# a machine learning approach (e.g., Random Forest):
# ```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
# Load your dataset
data = pd.read_csv('Dataset/maintenance.csv')



# for i in data["Product ID"]:
#     print(i.replace('#',''))
# Preprocess the data
# Handle missing values, encode categorical variables, etc.
#data.fillna(method='ffill', inplace=True)
# Feature selection

def remove_prefix_and_convert(value, prefix='L'):
    if value.startswith(prefix):
        value = value[len(prefix):]
    try:
        return float(value)
    except ValueError:
        return None

data['Type'] = [remove_prefix_and_convert(v) for v in data['Type']]
print(data['Type'])


import re

def extract_numeric(value):
    numeric_str = re.sub('[^0-9.]', '', value)
    return float(numeric_str) if numeric_str else None


data['Product ID'] = [extract_numeric(v) for v in data['Product ID']]
print(data['Product ID'])
features = data.drop('Machine failure', axis=1)  # Assuming'failure' is the target variable
print(features)
target = data['Machine failure']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target,
test_size=0.2, random_state=42)
# Build the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
import pandas as pd

# Assuming you have a DataFrame df and a column that 
# needs conversion

print(X_train)
print("========")
print(y_train)

model.fit(X_train, y_train)
# Make predictions
predictions = model.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')
print(classification_report(y_test, predictions))
# Save the model
import joblib
joblib.dump(model, 'Machine_failure_model.pkl')

# Function to predict maintenance need
def predict_maintenance(data):
    model = joblib.load('Machine_failure_model.pkl')
    prediction = model.predict(data)
    return prediction
#```
### Step 5: Integrate with IoT System
# Integrate the predictive model with your IoT system to get real-time data and
# make predictions on the fly.
# ```python
# Example of integrating with IoT data stream
def process_iot_data(iot_data):
    # Preprocess IoT data
    iot_data_processed = preprocess_iot_data(iot_data)
    # Predict maintenance needs
    maintenance_prediction = predict_maintenance(iot_data_processed)
    # Take action based on prediction
    if maintenance_prediction == 1:
        print("Maintenance needed!")
        # Trigger maintenance workflow
    else:
        print("No maintenance needed.")
# Function to preprocess IoT data
def preprocess_iot_data(iot_data):
    # Example preprocessing steps
    iot_data = pd.DataFrame(iot_data, index=[0])
    iot_data.fillna(method='ffill', inplace=True)
    return iot_data
#```
### Step 6: Deploy and Monitor
# Deploy the model within your IoT system and continuously monitor its
# performance. Collect feedback and retrain the model periodically to ensure its
# accuracy.
# ### Additional Considerations
# - **Real-time Processing**: Ensure your system can handle real-time data
# processing.
# - **Model Update**: Implement a mechanism to update the model as new data
# becomes available.
# - **User Interface**: Provide a user-friendly interface for maintenance
# personnel to interact with the system.
# This is a simplified outline to get you started. Depending on the complexity of
# your system and the specific requirements, you may need to adjust the approach.
