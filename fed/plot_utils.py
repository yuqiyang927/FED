import matplotlib.pyplot as plt

def plot_gdp_data(df):
    """Plot GDP by country from 2000 to 2022."""
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