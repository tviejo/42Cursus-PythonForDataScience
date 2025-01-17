import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, LogLocator


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


def projection_life(gdpp: pd.DataFrame, life_ex: pd.DataFrame) -> None:
    """
    Show life expectancy over time for a given country
    """
    gdpp_data = gdpp['1900']
    
    if gdpp_data.empty:
        print(f"Country '{country}' not found in the dataset.")
        return

    print(gdpp_data)

    life_ex = life_ex['1900']
    
    if life_ex.empty:
        print(f"Country '{country}' not found in the dataset.")
        return

    print(life_ex)

    gdpp_data = gdpp_data.apply(convert_to_number)
    life_ex = life_ex.apply(convert_to_number)

    combined_df = pd.DataFrame({
        'GDP per Capita': gdpp_data,
        'Life Expectancy': life_ex
    })

    print(combined_df)

    row_df = gdpp_data.reset_index()
    row_df.columns = ['GDP per Capita', 'Life Expectancy']

    sns.scatterplot(data=combined_df, x='GDP per Capita', y='Life Expectancy')

    plt.xscale('log')

    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_with_suffixes))
    plt.grid(False)

    plt.title("1900")
    plt.xlabel('Gross domestic product')
    plt.ylabel("Life Expectancy")

    plt.show()
