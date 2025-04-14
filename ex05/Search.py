# Imports from Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from math import sqrt


def main():
	n = 4
	qc = Grover_init(n)
	for _ in range(int(sqrt(n))):
		qc = Oracle(qc, n)
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

# Searching for a 111 pattern

def Oracle(qc, n):
	qc.ch(0,2)
	qc.ccx(1,3,2)
	qc.ch(0,2)
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