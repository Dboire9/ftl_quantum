from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt
import numpy as np
from qiskit.visualization import plot_histogram


def main():
	n = 3
	dj_circuit = QuantumCircuit(n+1, n)
	for qubit in range(n):
		dj_circuit.h(qubit)
	dj_circuit.x(n)
	dj_circuit.h(n)
	dj_circuit.barrier()


	balanced_oracle = example_oracle(n + 1)
	const_oracle = oracle_c(n+1)
	
	
	dj_circuit = dj_circuit.compose(balanced_oracle)
	for qubit in range(n):
		dj_circuit.h(qubit)
	dj_circuit.barrier()
	for i in range(n):
		dj_circuit.measure(i, i)

	print(dj_circuit)
	backend = Aer.get_backend('qasm_simulator')
	job = backend.run(dj_circuit, shots=100)
	result = job.result()
	counts = result.get_counts()
	print(counts)
	plot_histogram(counts)
	plt.show()
	for key, value in counts.items():
		if '1' in key:
			return print("balanced")
	return print("constant")

def oracle_b(nb_qubits):
	balanced_oracle = QuantumCircuit(nb_qubits)
	for i in range(3):
		balanced_oracle.cx(i,3)
	balanced_oracle.barrier()
	# print(balanced_oracle)
	return balanced_oracle

def oracle_c(nb_qubits):
	const_oracle = QuantumCircuit(nb_qubits)
	const_oracle.x(3)
	const_oracle.barrier()
	print(const_oracle)
	return const_oracle

if __name__ == "__main__":
	main()