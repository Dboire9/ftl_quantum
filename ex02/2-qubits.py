from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(qc)

backend = Aer.get_backend('qasm_simulator')
new_circuit = transpile(qc, backend)
job = backend.run(new_circuit, shots=500)
result = job.result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.show()