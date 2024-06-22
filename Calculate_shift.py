import streamlit as st

def calculate_shift(machine_id, shift_hours, material_used, job_complexity):
    job_time = shift_hours * (1 + {"Low": 0.1, "Medium": 0.2, "High": 0.3}[job_complexity])
    efficiency = material_used / job_time
    return {
        "Job Time": job_time,
        "Efficiency": efficiency
    }

def predictive_maintenance_analysis(maintenance_status):
    if "critical" in maintenance_status.lower():
        return "Immediate maintenance required"
    elif "warning" in maintenance_status.lower():
        return "Maintenance needed soon"
    else:
        return "All systems operational"

from PIL import Image
# Title
st.title("Additive Manufacturing Shift Calculator")
# Load the logo image
logo_path = "photo_2024-06-22 12.10.05.jpeg"  # Adjust the path to your logo file
logo = Image.open(logo_path)

# Display the logo
st.image(logo, caption='Licensed by Sam3dp.tech')  # Adjust width as needed

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


# Inputs
st.header("Input Parameters")
machine_id = st.text_input("Machine ID")
shift_hours = st.number_input("Shift Hours", min_value=1, max_value=24, value=8)
material_used = st.number_input("Material Used (kg)", min_value=0.0, value=1.0)
job_complexity = st.selectbox("Job Complexity", ["Low", "Medium", "High"])

# Predictive Maintenance Data
st.header("Predictive Maintenance Data")
maintenance_status = st.text_area("Maintenance Status", "Enter maintenance data...")

# Calculate button
if st.button("Calculate"):
    shift_results = calculate_shift(machine_id, shift_hours, material_used, job_complexity)
    maintenance_analysis = predictive_maintenance_analysis(maintenance_status)
    
    st.subheader("Shift Details")
    st.write(f"Job Time: {shift_results['Job Time']} hours")
    st.write(f"Efficiency: {shift_results['Efficiency']} kg/hour")
    
    st.subheader("Maintenance Analysis")
    st.write(maintenance_analysis)
