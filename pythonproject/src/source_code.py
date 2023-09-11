"""
This module takes a csv and returns statistics about it
"""

import pandas
import seaborn
import matplotlib.pyplot as plt
import polars as pl

def descriptive_statistics(data):
    """
    Calculate descriptive statistics for a DataFrame.

    Parameters:
    data (pd.DataFrame): The input DataFrame containing numeric data.

    Returns:
    pd.DataFrame: A DataFrame containing descriptive statistics.
    """
    return data.describe()

def generating_plot(data):
    '''
    This function generates a scatter plot from X and Y
    '''
    seaborn.pairplot(data)
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":

    # Read the CSV file
    data_pd = pandas.read_csv("pythonproject/src/data/spotify-2023.csv", encoding="ISO-8859-1")

    data_pl=pl.read_csv("pythonproject/src/data/spotify-2023.csv", encoding="ISO-8859-1")

    # Print descriptive statistics
    print(descriptive_statistics(data_sample))

    generating_plot(data_sample[['energy_%','instrumentalness_%']])
