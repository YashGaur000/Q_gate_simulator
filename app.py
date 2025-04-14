import streamlit as st
import matplotlib.pyplot as plt
from quantum_simulator import QuantumGateSimulator
import io

st.set_page_config(page_title="Quantum Gate Simulator", layout="wide")

st.title("Quantum Gate Simulator")
st.write("Explore quantum gates and their effects on qubits")

# Initialize simulator in session state if not exists
if 'simulator' not in st.session_state:
    st.session_state.simulator = QuantumGateSimulator()
    st.session_state.history = []

# Sidebar for gate selection
st.sidebar.header("Gate Controls")
gate_type = st.sidebar.selectbox(
    "Select Gate",
    ["X Gate", "H Gate", "CNOT Gate"]
)

# Main content area split into two columns
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("Gate Parameters")
    if gate_type in ["X Gate", "H Gate"]:
        qubit = st.number_input("Select qubit", min_value=0, max_value=1, value=0)
        if st.button("Apply Gate"):
            if gate_type == "X Gate":
                st.session_state.simulator.apply_X(qubit)
                st.session_state.history.append(f"Applied X gate to qubit {qubit}")
            else:
                st.session_state.simulator.apply_H(qubit)
                st.session_state.history.append(f"Applied H gate to qubit {qubit}")
    else:  # CNOT Gate
        control = st.number_input("Control qubit", min_value=0, max_value=1, value=0)
        target = st.number_input("Target qubit", min_value=0, max_value=1, value=1)
        if st.button("Apply Gate"):
            st.session_state.simulator.apply_CNOT(control, target)
            st.session_state.history.append(f"Applied CNOT gate with control={control}, target={target}")

    if st.button("Reset Circuit"):
        st.session_state.simulator.reset()
        st.session_state.history = []
        st.session_state.history.append("Circuit reset")

with col2:
    st.subheader("Quantum State Visualization")
    # Get state vector
    state = st.session_state.simulator.get_statevector()
    st.write("Current State Vector:", state)
    
    # Create and display Bloch sphere visualization
    fig = plt.figure(figsize=(8, 8))
    st.session_state.simulator.visualize_state()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    st.image(buf, use_column_width=True)

# Display operation history
st.subheader("Operation History")
for operation in st.session_state.history:
    st.text(operation)
