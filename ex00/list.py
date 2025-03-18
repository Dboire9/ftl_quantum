from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService
import os

load_dotenv()
 
# Save an IBM Quantum account and set it as your default account.
QiskitRuntimeService.save_account(channel="ibm_quantum", token=os.getenv("TOKEN"), set_as_default=True, overwrite=True)
 
# Load saved credentials
service = QiskitRuntimeService()

backends = service.backends(simulator=True)

for backends in backends:
	print(f"Simulator: {backends.name}")
	status = backends.status()
	print(f"Status: {status.status_msg}")
	print(f"Pending Jobs: {status.pending_jobs}")
	print("---")

backends = service.backends()

for backends in backends:
	print(f"Simulator: {backends.name}")
	print(f"Num qubits: {backends.num_qubits}")
	status = backends.status()
	print(f"Status: {status.status_msg}")
	print(f"Pending Jobs: {status.pending_jobs}")
	print("---")