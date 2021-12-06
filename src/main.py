'''---------------------------------------------
Maria Harrison
CSC535-Data Mining
Dr. Saquer
Final Group Project

Maria's deliverables:
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