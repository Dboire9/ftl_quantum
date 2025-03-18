from qiskit_aer.primitives import Sampler
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
print(qc)

sampler = Sampler()
quasi_dists = sampler.run(qc, shots=500).result().quasi_dists[0]

print(quasi_dists)
plot_histogram(quasi_dists)
plt.show()