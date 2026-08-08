# hadamard.py
# Date:08/08/2026
# Testing: one qubit in superposition, measured 1000 times.
# Expected: roughly half 0 and half 1.
# Result: {'0': 496, '1': 504}

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

result = AerSimulator().run(qc, shots=1000).result()
print(result.get_counts())
