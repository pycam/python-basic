# An introduction to solving biological problems with Python

Materials for the "Introduction to Solving Biological Problems with Python" course run by the Graduate School of Life Sciences, University of Cambridge.

## Clone this github project

```bash
git clone https://github.com/pycam/python-intro.git
cd python-intro
```

## Dependencies

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install jupyter
pip install rise
jupyter-nbextension install rise --py --sys-prefix
jupyter nbextension enable rise --py --sys-prefix
```

## Usage

```bash
jupyter notebook
```
