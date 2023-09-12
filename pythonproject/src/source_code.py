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
    data (pl.DataFrame): The input Polars DataFrame,
    which must contain numeric data.

    Returns:
    pl.DataFrame: A DataFrame containing descriptive statistics.
    """
    return data.describe()

def generating_plot(data,x_variable,y_variable,size=None,title):
    '''
    Parameters:
        data: Polar DataFrame
        x_variable: String of the variable in axis X from data
        y_variable: String of the variable in axis Y from data
        size: String if a variable is required to 
        title: String for the plot title
    '''
    
    x=data[x_variable]
    y=data[y_variable]
    if size is None:
        area=1
    else:
        area = data[size]*10/data[size].mean()
    #Labeling
    plt.scatter(x, y, s=area, alpha=0.5)
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.title("")
    plt.show()
    plt.savefig(title+'.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":

    data_pl=pl.read_csv("pythonproject/src/data/spotify-2023.csv", encoding="ISO-8859-1")

    descriptive_statistics(data_pl)

    generating_plot(data_pl,x_variable="gdpPerCapitaPPP",
                    y_variable="meanIncome",
                    size="pop2023",
                    title="GDP per Capita vs Avg income (size proportional Population)")
