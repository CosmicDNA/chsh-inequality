import qiskit
from qiskit import IBMQ
import os

IBMQ.save_account(os.environ['TOKEN'])