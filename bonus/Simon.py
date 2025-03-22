from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import Aer
import matplotlib.pyplot as plt


def main():
	secret = '110'
	n = len(secret)
	qc = QuantumCircuit(n*2, n)
	qc.h(range(n))
	qc.barrier()
	qc = Simon_algo(qc, n, secret)
	qc.barrier()
	qc.h(range(n))
	qc.measure(range(n), range(n))
	print(qc)
	backend = Aer.get_backend('qasm_simulator')
	new_circuit = transpile(qc, backend)
	job = backend.run(new_circuit, shots=100, memory=True)
	counts = job.result().get_counts()
	print(f"Clues: {counts}")
	plot_histogram(counts)
	for z in counts:
		print('{}.{}={} (mod2)'.format(secret,z,find_it(secret,z)))

	plt.show()

def Simon_algo(qc, n, s):
	s = s[::-1]
	for i in range(n):
		qc.cx(i, n + i)
	if '1' not in s:
		return qc
	index = s.find('1')
	for i in range(n):
		if s[i] == '1':
			qc.cx(index, i+n)
	return qc
	
def find_it(s, z):
	accum = 0
	for i in range(len(s)):
		accum += int(s[i]) * int(z[i])
	return (accum % 2)



if __name__ == "__main__":
	main()