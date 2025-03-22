from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def main():
	secret = "a"
	s_to_search = "a"
	full_bits = string_to_binary(secret)
	s = string_to_binary(s_to_search)
	n = len(s)

	print(f"Secret: {secret}, Bits: {full_bits}")
	print(f"Pattern: {s_to_search}, Bits: {s}, n: {n}")

	qc = bernstein_vazirani(n, s)
	print(qc)
	backend = Aer.get_backend('qasm_simulator')
	new_circuit = transpile(qc, backend)
	job = backend.run(new_circuit, shots=1, memory=True)
	result = job.result()
	measurements = result.get_memory()[0]
	measurements = measurements[::-1]
	print(f'The Hidden Bit String was {full_bits}.')
	print(f'The prediction was {measurements}.')
	if full_bits == measurements:
		print('Correct!')

	plt.show()

def bernstein_vazirani(n, s):
	qc = QuantumCircuit(n + 1, n)
	qc.h(n)
	qc.z(n)
	qc.h(range(n))
	qc.barrier()
	for i in range(n):
		if s[i] == '1':
			qc.cx(i, n)
	qc.barrier()
	qc.h(range(n))
	qc.measure(range(n), range(n))
	return qc

def string_to_binary(s):
	res = ''.join(format(ord(i), '08b') for i in s)
	return res



if __name__ == "__main__":
	main()