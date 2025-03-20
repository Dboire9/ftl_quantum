from qiskit import QuantumCircuit, transpile, QuantumRegister
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
	qc = dj_query(3)
	print(dj_algo(qc))
	plt.show()

def dj_circuit(function: QuantumCircuit):
	n = function.num_qubits - 1
	djc = QuantumCircuit(n + 1, n)
	djc.x(n)
	djc.h(range(n + 1))
	djc.compose(function, inplace=True)
	djc.h(range(n))
	djc.measure(n, n - 1)
	return djc

def dj_algo(function: QuantumCircuit):
	qc = dj_circuit(function)
	backend = Aer.get_backend('qasm_simulator')
	new_circuit = transpile(qc, backend)
	job = backend.run(new_circuit, shots=1, memory=True)
	result = job.result()
	measurements = result.get_memory()
	print(measurements)
	if "1" in measurements[0]:
		return "balanced"
	return "constant"
	
def balanced_oracle(n: int) -> QuantumCircuit:
	qreg = QuantumRegister(n + 1, 'q')
	qc = QuantumCircuit(qreg)
	for i in range(n):
		qc.cx(i, n)
	print(qc)
	return qc

def constant_oracle(n: int) -> QuantumCircuit:
	qreg = QuantumRegister(n + 1, 'q')
	qc = QuantumCircuit(qreg)
	qc.x(n)
	print(qc)
	return qc

def dj_query(n: int) -> QuantumCircuit:
	oracle_circuit = balanced_oracle(n)
	return dj_circuit(oracle_circuit)

if __name__ == "__main__":
	main()