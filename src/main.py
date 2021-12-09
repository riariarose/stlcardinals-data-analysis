"""
Final Project: Cardinals
Author: Zach Grasso
Task 1: The top 12 players overall, and how they compare to the 12 players    listed on the dataset website (found by using a WAR score)

"""

###### Imports ######
import pandas as pd


###### Functions ######

# Read CSV files
def get_data(filename):
    """
    Reads in the data from the CSV file and returns a dataframe
    """
    df = pd.read_csv(filename)
    return df
