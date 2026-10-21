# FED: GDP Analysis

A collaborative project to load, clean, analyse and visualise GDP data for the UK, USA, Brazil, Japan, China, Germany and Switzerland from 2000 to 2022.

## Project Structure

- `data/`: Raw GDP data
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

## Data Source

- Source: [World Bank, World Development Indicators (WDI)](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD)
- Indicator: GDP (constant 2015 US$), `NY.GDP.MKTP.KD`
- Frequency: Annual
- Raw data: `data/API_NY.GDP.MKTP.KD_DS2_en_csv_v2_64.csv`

## Data Processing

The functions in `fed/data.py` handle data loading and cleaning:

- `load_gdp_data()`: Reads the raw GDP data from the CSV file
- `clean_gdp_data(df)`: Filters seven countries, selects years 2000–2022, reshapes the data from wide to long format, and converts `Year` to an integer

### Usage

```python
from fed.data import load_gdp_data, clean_gdp_data

raw_gdp = load_gdp_data()
gdp = clean_gdp_data(raw_gdp)
```