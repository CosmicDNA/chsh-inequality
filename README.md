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

# Running the [CSH Inequality Jupyter notebook](https://github.com/CosmicDNA/chsh-inequality/blob/main/src/chsh-inequality.ipynb)

Once the token has been saved to your IBM local account, you can run [the Jupyter notebook from src/chsh-inequality.ipynb](https://github.com/CosmicDNA/chsh-inequality/blob/main/src/chsh-inequality.ipynb) by either following the intructions present [here](https://docs.jupyter.org/en/latest/running.html) or running directly from Visual Studio Code following the instructions present [here](https://code.visualstudio.com/docs/datascience/jupyter-notebooks#:~:text=If%20you%20have%20an%20existing%20Jupyter%20Notebook%2C%20you,can%20also%20use%20keyboard%20shortcuts%20to%20run%20code.).