from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
from qiskit_aer import Aer
import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram


def main():
	n = 3
	dj_circuit = QuantumCircuit(n+1, n)
	for qubit in range(n):
		dj_circuit.h(qubit)
	dj_circuit.x(n)
	dj_circuit.h(n)
	dj_circuit.barrier()


	balanced_oracle = oracle_b(n + 1)
	# const_oracle = oracle_c(n)
	
	
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

def oracle_b(nb_qubits):
	balanced_oracle = QuantumCircuit(nb_qubits)
	for i in range(1):
		balanced_oracle.cx(i,3)
	balanced_oracle.barrier()
	# print(balanced_oracle)
	return balanced_oracle

def oracle_c(nb_qubits):
	const_oracle = QuantumCircuit(nb_qubits)
	const_oracle.x(4)
	const_oracle.barrier()
	print(const_oracle)
	return const_oracle

if __name__ == "__main__":
	main()