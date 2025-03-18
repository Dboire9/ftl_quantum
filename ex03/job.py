from dotenv import load_dotenv
import os
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

load_dotenv()

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token=os.getenv("TOKEN")
)

job = service.job('czc34tbr3jrg008p737g')
job_result = job.result()

meas_data = job_result[0].data.meas

counts = meas_data.get_counts()

print("Counts:", counts)
plot_histogram(counts)
plt.show()