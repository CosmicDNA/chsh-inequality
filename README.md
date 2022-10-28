# Local Reality and the CHSH inequality
This project runs the real experiment that demonstrates the reason why Einsten was wrong in the Einstein-Podolsky-Rosen article in quantum theory. It runs the code detailed in https://qiskit.org/textbook/ch-demos/chsh.html.

# Installation
```bash
# Clone the repository
git clone git@github.com:CosmicDNA/chsh-inequality.git
# Enter cloned folder
cd chsh-inequality
# Create virtual environment for pip packages
python -m venv .venv
# Install requirements
pip install -r requirements.txt
```

# Setup IBM quantum computing token

Edit .envrc.sample file name to .envrc and paste the token retrieved from https://quantum-computing.ibm.com/

Once the environment variable is set, run the following to save your account details:

```bash
python src/save_account.py
```