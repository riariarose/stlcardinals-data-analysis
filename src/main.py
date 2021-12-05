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

# find the top 12 players overall by combining the two dataframes and adding the total runs they have and games they have played
def computation_of_players(batting, roster):
    """
    Finds the top 12 players overall by combining the two dataframes and adding the total runs they have and games they have played
    """
    # combine the two dataframes
    df = pd.merge(batting, roster, left_index=True, right_on='playerID')
    # add the total runs and games they have played
    df['total_runs'] = df['R'] + df['H']
    df['total_games'] = df['G']
    # sort the dataframe by the total runs and games they have played
    df = df.sort_values(by=['total_runs', 'total_games'], ascending=False)
    # return the top 12 players overall
    return df


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
    Checks each top players of roster with war score to computed's top 12 players
    """
    # get the top 12 players of the roster
    top_players_roster = roster.sort_values(by=['war'], ascending=False)
    # get the top 12 players of the computed dataframe
    top_players_computed = computed.sort_values(
        by=['total_runs', 'total_games'], ascending=False)
    # check each top player of the roster with the war score
    for i in range(1, 13):
        print("Top Player of Roster: ", top_players_roster.iloc[i-1]['playerID'], " ", top_players_roster.iloc[i-1]['nameFirst'], " ",
              top_players_roster.iloc[i-1]['nameLast'], " ", top_players_roster.iloc[i-1]['total_runs'], " ", top_players_roster.iloc[i-1]['total_games'])
        print("Top Player of Computed: ", top_players_computed.iloc[i-1]['playerID'], " ", top_players_computed.iloc[i-1]['nameFirst'], " ",
              top_players_computed.iloc[i-1]['nameLast'], " ", top_players_computed.iloc[i-1]['total_runs'], " ", top_players_computed.iloc[i-1]['total_games'])
        print("")


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
