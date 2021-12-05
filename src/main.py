"""
Final Project: Cardinals
Author: Zach Grasso
Task 1: The top 12 players overall, and how they compare to the 12 players    listed on the dataset website (found by using a WAR score)

"""

###### Imports ######
import pandas as pd
import numpy as np
import sklearn


###### Functions ######

# find the top 12 players overall by combining the two dataframes and adding the total runs they have along with runs divided by games they have played
def computation_of_players(batting, roster):
    """
    Finds the top 12 players overall by combining the two dataframes and adding the total runs they have and games they have played
    """
    # combine the two dataframes on playerID
    df = pd.merge(batting, roster, on='Name')
    # append a new column called calculated
    df['calculated'] = 0

    # for each player in dataframe, add the Runs and Hits they have and divide by the games they have played
    for i in range(len(df)):
        num = df.iloc[i]['Runs'] + \
            df.iloc[i]['Hits'] / df.iloc[i]['Games']
        print(num)
        df.iloc[i]['calculated'] = num

    # create a dataframe with the name and calculated value for top 12 players of calculated
    print(df.head(12))
    computed = df.sort_values(by=['calculated'], ascending=False)
    computed = computed[['Name', 'calculated', 'WAR']]
    print(computed.head(12))

    return computed


# Read CSV files
def get_data(filename):
    """
    Reads in the data from the CSV file and returns a dataframe
    """
    df = pd.read_csv(filename)
    return df

# check each top players of roster with war score to computed's top 12 players


def check_top_players(roster, computed):
    """
    Checks each top players of roster with war score to computed's top 12 players (war score is calculated through a complicated equation but only measures the players during a winning game)
    """
    # get the top 12 players of the roster
    top_players_roster = roster.sort_values(by=['WAR'], ascending=False)
    # get the top 12 players of the computed dataframe
    top_players_computed = computed.sort_values(
        by=['calculated'], ascending=False)
    # check each top player of the roster with the war score
    for i in range(1, 13):
        print(top_players_roster.iloc[i]['Name']
              == top_players_computed.iloc[i]['Name'])
        print(top_players_roster.iloc[i]['Name'],
              top_players_computed.iloc[i]['Name'])


def main():
    """
    Main function
    """
    # maria added the following 4 lines
    # you have to set the file name to the string. python doesn't work the way you originally had it
    team_batting_file = "team_batting.csv"
    roster_file = "full_roster.csv"
    batting = get_data(team_batting_file)
    roster = get_data(roster_file)

    computed = computation_of_players(batting, roster)
    check_top_players(roster, computed)


main()
