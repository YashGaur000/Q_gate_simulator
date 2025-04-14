import streamlit as st
import matplotlib.pyplot as plt
from quantum_simulator import QuantumGateSimulator
import io

st.set_page_config(
    page_title="Quantum Gate Simulator",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for better styling
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main > div {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Quantum Gate Simulator")
st.write("Explore quantum gates and their effects on qubits interactively!")

# Initialize simulator in session state if not exists
if 'simulator' not in st.session_state:
    st.session_state.simulator = QuantumGateSimulator()
    st.session_state.history = []

# Sidebar for gate selection with improved styling
with st.sidebar:
    st.header("🎛️ Gate Controls")
    gate_type = st.selectbox(
        "Select Quantum Gate",
        ["X Gate (NOT)", "H Gate (Hadamard)", "CNOT Gate"],
        help="Choose which quantum gate to apply"
    )

# Main content area split into two columns
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("⚙️ Gate Parameters")
    if gate_type in ["X Gate (NOT)", "H Gate (Hadamard)"]:
        qubit = st.number_input(
            "Select target qubit",
            min_value=0,
            max_value=1,
            value=0,
            help="Choose which qubit to apply the gate to (0 or 1)"
        )
        if st.button("Apply Gate", type="primary"):
            if "X" in gate_type:
                st.session_state.simulator.apply_X(qubit)
                st.session_state.history.append(f"🔄 Applied X gate to qubit {qubit}")
            else:
                st.session_state.simulator.apply_H(qubit)
                st.session_state.history.append(f"🔄 Applied H gate to qubit {qubit}")
    else:  # CNOT Gate
        st.write("CNOT Gate Parameters:")
        control = st.number_input(
            "Control qubit",
            min_value=0,
            max_value=1,
            value=0,
            help="The control qubit determines whether to flip the target qubit"
        )
        target = st.number_input(
            "Target qubit",
            min_value=0,
            max_value=1,
            value=1,
            help="The target qubit is flipped if the control qubit is |1⟩"
        )
        if st.button("Apply CNOT Gate", type="primary"):
            st.session_state.simulator.apply_CNOT(control, target)
            st.session_state.history.append(f"🔄 Applied CNOT gate with control={control}, target={target}")

    if st.button("Reset Circuit", type="secondary"):
        st.session_state.simulator.reset()
        st.session_state.history = []
        st.session_state.history.append("🔄 Circuit reset to initial state")

with col2:
    st.subheader("📊 Quantum State Visualization")
    # Get and display state vector with LaTeX formatting
    state = st.session_state.simulator.get_statevector()
    st.write("Current State Vector:")
    st.latex(f"|\\psi\\rangle = {state}")
    
    # Create and display Bloch sphere visualization
    fig = plt.figure(figsize=(8, 8))
    st.session_state.simulator.visualize_state()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    plt.close()
    st.image(buf, use_column_width=True)

# Display operation history with improved styling
st.subheader("📝 Operation History")
history_container = st.container()
with history_container:
    for operation in reversed(st.session_state.history):  # Show most recent first
        st.info(operation)
