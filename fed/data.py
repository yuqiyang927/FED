from pathlib import Path
import pandas as pd


def load_gdp_data():
    """Load raw GDP data from the World Bank CSV file."""
    
    data_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "API_NY.GDP.MKTP.KD_DS2_en_csv_v2_64.csv"
    )

    df = pd.read_csv(data_path, skiprows=4)

    return df



def clean_gdp_data(df):
    """Filter and reshape GDP data for the selected countries and years."""

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

def plot_gdp_data(df):
    """Plot Yearly GDP by country from 2000 to 2022."""
    fig, ax = plt.subplots(figsize=(12, 6))

    for country, country_data in df.groupby("Country Name"):
        country_data = country_data.sort_values("Year")

        ax.plot(
            country_data["Year"],
            country_data["GDP"],
            label=country,
        )

    ax.set_title("GDP by Country, 2000–2022")
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP (constant US$, trillions)")
    ax.set_xlim(2000, 2022)
    ax.set_xticks(range(2000, 2023, 2))

    # Display GDP values in trillions
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(lambda value, position: f"{value / 1e12:.1f}")
    )

    ax.legend(title="Country")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    plt.show()

    return fig, ax
