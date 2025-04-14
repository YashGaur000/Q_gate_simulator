from quantum_simulator import QuantumGateSimulator
import matplotlib.pyplot as plt

def main():
    # Create a simulator instance
    sim = QuantumGateSimulator()
    
    # Example 1: X Gate (NOT gate)
    print("Example 1: X Gate")
    sim.apply_X(0)  # Apply X gate to first qubit
    state = sim.get_statevector()
    print("State after X gate:", state)
    sim.visualize_state()
    plt.show()
    sim.reset()
    
    # Example 2: Hadamard Gate
    print("\nExample 2: Hadamard Gate")
    sim.apply_H(0)  # Apply H gate to first qubit
    state = sim.get_statevector()
    print("State after H gate:", state)
    sim.visualize_state()
    plt.show()
    sim.reset()
    
    # Example 3: CNOT Gate
    print("\nExample 3: CNOT Gate")
    sim.apply_X(0)  # Set control qubit to |1⟩
    sim.apply_CNOT(0, 1)  # Apply CNOT with first qubit as control
    state = sim.get_statevector()
    print("State after CNOT gate:", state)
    sim.visualize_state()
    plt.show()

if __name__ == "__main__":
    main()
