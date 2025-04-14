import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

class QuantumGateSimulator:
    def __init__(self):
        """Initialize the quantum gate simulator."""
        self.qreg = QuantumRegister(2)  # Using 2 qubits for basic operations
        self.creg = ClassicalRegister(2)
        self.circuit = QuantumCircuit(self.qreg, self.creg)
        
    def apply_X(self, qubit_idx):
        """Apply X (NOT) gate to the specified qubit."""
        self.circuit.x(self.qreg[qubit_idx])
        return self
        
    def apply_H(self, qubit_idx):
        """Apply Hadamard (H) gate to the specified qubit."""
        self.circuit.h(self.qreg[qubit_idx])
        return self
        
    def apply_CNOT(self, control_idx, target_idx):
        """Apply CNOT gate with specified control and target qubits."""
        self.circuit.cx(self.qreg[control_idx], self.qreg[target_idx])
        return self
    
    def get_statevector(self):
        """Get the quantum state vector of the circuit."""
        return Statevector.from_instruction(self.circuit)
    
    def visualize_state(self):
        """Visualize the quantum state on the Bloch sphere."""
        state = self.get_statevector()
        return plot_bloch_multivector(state)
    
    def measure(self):
        """Measure all qubits in the computational basis."""
        self.circuit.measure(self.qreg, self.creg)
        return self
    
    def reset(self):
        """Reset the circuit to initial state."""
        self.circuit = QuantumCircuit(self.qreg, self.creg)
        return self
