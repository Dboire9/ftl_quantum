from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

load_dotenv()
 
# Save an IBM Quantum account and set it as your default account.
service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("TOKEN"))

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(qc)

backend = service.least_busy(operational=True, simulator=False)

transpiled_qc = transpile(qc, backend=backend)

sampler = Sampler(backend)

job = sampler.run([transpiled_qc], shots=500)
result = job.result()
meas_data = result[0].data.meas

counts = meas_data.get_counts()

print("Counts:", counts)
plot_histogram(counts)
plt.show()