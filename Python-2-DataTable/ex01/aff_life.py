import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def aff_life(country: str, dataset: pd.DataFrame) -> None:
    """
    Show life expectancy over time for a given country
    """
    filtered_data = dataset[dataset['country'] == country].iloc[0, 1:]
    
    if filtered_data.empty:
        print(f"Country '{country}' not found in the dataset.")
        return

    row_df = filtered_data.reset_index()
    row_df.columns = ['Year', 'Life Expectancy']
    row_df['Year'] = row_df['Year'].astype(int)

    sns.set(style="white")
    sns.lineplot(data=row_df, x='Year', y='Life Expectancy')

    plt.xticks(ticks=row_df['Year'][::40], labels=row_df['Year'][::40])

    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    plt.show()

