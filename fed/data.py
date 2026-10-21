from pathlib import Path

import pandas as pd


def load_gdp_data():
    data_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "API_NY.GDP.MKTP.KD_DS2_en_csv_v2_64.csv"
    )

    df = pd.read_csv(data_path, skiprows=4)

    return df



def clean_gdp_data(df):
    countries = [
        "United Kingdom",
        "United States",
        "Brazil",
        "Japan",
        "China",
        "Germany",
        "Switzerland",
    ]

    df = df[df["Country Name"].isin(countries)]

    years = [str(year) for year in range(2000, 2023)]
    df = df[["Country Name", "Country Code"] + years]

    df = df.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=years,
        var_name="Year",
        value_name="GDP",
    )

    df["Year"] = df["Year"].astype(int)

    return df

