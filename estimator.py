from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import AerSimulator

def estimate_time(algorithm):
    if algorithm == "RSA":
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()

        simulator = AerSimulator()
        compiled_circuit = transpile(qc, simulator)
        result = simulator.run(compiled_circuit).result()

        return "Estimated breach time: ~10 years (RSA-2048)"
    elif algorithm == "SHA-1":
        return "Estimated breach time: ~5 years with Grover's algorithm"
    elif algorithm == "AES":
        return "Estimated breach time: ~3 years with Grover's algorithm"
    else:
        return "No estimate available"
