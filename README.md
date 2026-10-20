# FED: GDP Analysis

A collaborative project to load, clean, analyse and visualise GDP data for the UK, USA, Brazil, Japan, China, Germany and Switzerland from 2000 to 2022.

## Project Structure

- `fed/__init__.py`: Python package initialisation
- `fed/data.py`: Data loading and cleaning
- `fed/plot_utils.py`: Data visualisation
- `gdp_analysis.ipynb`: GDP analysis notebook
- `environment.yml`: Conda environment configuration
- `pyproject.toml`: Python package configuration

## Setup

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate fed-env
```

Install the project package:

```bash
python -m pip install -e .
```

Open `gdp_analysis.ipynb` using the `fed-env` environment.