import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def convert_to_number(value: str) -> float:
    """
    Converts a string with 'K', 'M', or 'B' suffix into a number.
    - K = Thousand (1,000)
    - M = Million (1,000,000)
    - B = Billion (1,000,000,000)

    Args:
        value (str): The string to convert.

    Returns:
        float: The numerical value.
    """
    if isinstance(value, str):
        value = value.strip().upper()
        if value.endswith('K'):
            return float(value[:-1]) * 1_000
        elif value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('B'):
            return float(value[:-1]) * 1_000_000_000
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def format_with_suffixes(x, _):
        """
        Format the y-axis ticks with suffixes.
        """
        if x >= 1_000_000_000:
            return f'{x / 1_000_000_000:.1f}B'
        elif x >= 1_000_000:
            return f'{x / 1_000_000:.1f}M'
        elif x >= 1_000:
            return f'{x / 1_000:.1f}K'
        return str(int(x))

def aff_pop(country1: str, country2: str, dataset: pd.DataFrame) -> None:
    """
    Show life expectancy over time for two given countries.
    """

    filtered_data1 = dataset[dataset['country'] == country1].iloc[0, 1:]
    if filtered_data1.empty:
        print(f"Country '{country1}' not found in the dataset.")
        return

    filtered_data2 = dataset[dataset['country'] == country2].iloc[0, 1:]
    if filtered_data2.empty:
        print(f"Country '{country2}' not found in the dataset.")
        return

    row_df1 = filtered_data1.reset_index()
    row_df1.columns = ['Year', 'Population']
    row_df1['Year'] = row_df1['Year'].astype(int)
    row_df1['Population'] = row_df1['Population'].apply(convert_to_number)
    row_df1['Country'] = country1

    row_df2 = filtered_data2.reset_index()
    row_df2.columns = ['Year', 'Population']
    row_df2['Year'] = row_df2['Year'].astype(int)
    row_df2['Population'] = row_df2['Population'].apply(convert_to_number)
    row_df2['Country'] = country2

    combined_df = pd.concat([row_df1, row_df2], ignore_index=True)

    combined_df = combined_df[combined_df['Year'] <= 2050]

    print(combined_df)

    sns.set(style="white")
    plt.figure(figsize=(8, 8))

    sns.lineplot(data=combined_df, x='Year', y='Population', hue='Country')

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_with_suffixes))

    years = combined_df['Year'].unique()
    plt.xticks(ticks=years[::40], labels=years[::40])

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title='Country', loc='lower right')

    plt.show()
