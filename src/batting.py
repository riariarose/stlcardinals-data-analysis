'''---------------------------------------------
CSC535-FA2021
Data Mining
Final Group Project

Column names in the "team_batting.csv" file
Rank,Position,Name,Age,Games,PA,AB,Runs,Hits,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB
------------------------------------------------'''

import pandas as pd
import numpy as np

def get_data(fileName):
    df = pd.read_csv(fileName)
    return df

# preprocessing the team_batting.csv file
def preprocess_batting(df):
    # batting = df.drop(['Country', 'Ht', 'Wt', 'DoB', 'Yrs', 'WAR', 'Status'], axis=1)
    ranks = pd.DataFrame(df.iloc[:, 0:4])
    data = pd.DataFrame(df.iloc[:, 2:])

    return 0

def main():

    batting_file = "team_batting.csv"
    batting_df = get_data(batting_file)
    preprocess_batting(batting_df)

main()
