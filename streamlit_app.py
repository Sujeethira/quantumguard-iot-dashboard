import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="QuantumGuard Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ QuantumGuard")
st.subheader("AI-Based IoT Security and Quantum Optimization")
st.caption("Artificial sensor data | Simulation dashboard")

# Sensor data
data = {
    "Sensor": [f"S{i}" for i in range(1, 11)],
    "Temperature": [28, 30, 65, 29, 31, 27, 30, 28, 29, 31],
    "Packet Rate": [50, 55, 120, 48, 52, 49, 51, 47, 53, 50],
    "Response Time": [100, 110, 350, 95, 105, 98, 102, 97, 108, 101],
    "Trust Score": [100, 100, 0, 100, 100, 100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Section",
    ["Overview", "Sensor Monitoring", "Network Performance", "Quantum Results"]
)

if page == "Overview":

    st.header("System Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Sensors", "10")
    c2.metric("Anomalies Detected", "1")
    c3.metric("After Isolation", "96.26%")
    c4.metric("After Recovery", "99.24%")

    st.markdown("### Network Security Status")
    st.success("Network Operational")

    st.markdown("### Project Workflow")
    st.write(
        "Sensor Monitoring → Anomaly Detection → "
        "Trust Evaluation → Sensor Isolation → "
        "Quantum Optimization → Recovery"
    )

elif page == "Sensor Monitoring":

    st.header("IoT Sensor Monitoring")

    st.dataframe(df, use_container_width=True)

    st.markdown("### Sensor Trust Scores")

    fig = px.bar(
        df,
        x="Sensor",
        y="Trust Score",
        color="Trust Score",
        title="Trust Score of Each Sensor",
        range_y=[0, 100]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.warning("S3 is identified as an anomalous sensor in this simulation.")

elif page == "Network Performance":

    st.header("Network Performance Analysis")

    results = pd.DataFrame({
        "Stage": ["Before Isolation", "After Isolation", "After Recovery"],
        "Coverage": [99.24, 96.26, 99.24],
        "Active Sensors": [10, 9, 10]
    })

    fig = px.bar(
        results,
        x="Stage",
        y="Coverage",
        color="Stage",
        title="Network Coverage Comparison",
        text="Coverage"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(results, use_container_width=True)

    st.success("Network connectivity was maintained throughout the simulation.")

elif page == "Quantum Results":

    st.header("Quantum Optimization – Grover's Algorithm")

    c1, c2, c3 = st.columns(3)

    c1.metric("Valid Configurations", "19")
    c2.metric("Initial Probability", "1.86%")
    c3.metric("After Grover", "15.88%")

    st.write("**Grover Iterations:** 1")
    st.write("**Probability Improvement:** 8.56×")

    st.info(
        "These are results from a Qiskit quantum simulation. "
        "They demonstrate probability amplification of valid configurations."
    )

st.divider()
st.caption("QuantumGuard | IoT Security Simulation Project")
