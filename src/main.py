'''---------------------------------------------
CSC535-FA2021
Data Mining
Final Group Project

Column names in the "full_roster.csv" file
Name,Age,Country,B,T,Ht,Wt,DoB,Yrs,G,GS,Batting,Defense,P,C,1B,2B,3B,SS,LF,CF,RF,OF,DH,PH,PR,WAR,Status
Column names in the "team_batting.csv" file
Rank,Position,Name,Age,Games,PA,AB,Runs,Hits,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB
------------------------------------------------'''

import pandas as pd
import numpy as np

def get_data(fileName):
    df = pd.read_csv(fileName)
    return df

def main():
    batting_file = "team_batting.csv"
    roster_file = "full_roster.csv"

    batting_data = get_data(batting_file)
    roster_data = get_data(roster_file)
