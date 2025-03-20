# Imports from Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from math import sqrt


def main():
	n = 3
	qc = Grover_init(n)
	for _ in range(int(sqrt(n))):
		qc = Oracle(qc)
		qc = Diffusion(qc, n)
	qc.measure_all()
	print(qc)
	backend = Aer.get_backend('qasm_simulator')
	new_circuit = transpile(qc, backend)
	job = backend.run(new_circuit, shots=100)
	result = job.result()
	counts = result.get_counts()
	print(counts)
	plot_histogram(counts)
	plt.show()

def Grover_init(n):
	qc = QuantumCircuit(n)
	qc.h(range(n))

	return qc

def Oracle(qc):
	qc.h(2)
	qc.mcx([0, 1], 2)
	qc.h(2)
	return qc

def Diffusion(qc, n):
	qc.h(range(n))
	qc.x(range(n))
	qc.h(n-1)
	qc.mcx(list(range(n-1)), n-1)
	qc.h(n-1)
	qc.x(range(n))
	qc.h(range(n))
	return qc


if __name__ == "__main__":
	main()