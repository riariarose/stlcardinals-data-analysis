'''---------------------------------------------
CSC535-FA2021
Data Mining
Final Group Project

Maria's deliverables: 
The top 6 best performing players per position based on game statistics 
Positions: Pitcher, Catcher, 1B, 2B, 3B, Short stop, Right fielder, Left fielder, Center fielder and Designated Hitter

Column names in the "full_roster.csv" file
Name,Age,Country,B,T,Ht,Wt,DoB,Yrs,G,GS,Batting,Defense,P,C,1B,2B,3B,SS,LF,CF,RF,OF,DH,PH,PR,WAR,Status

Column names in the "team_batting.csv" file
Rank,Position,Name,Age,Games,PA,AB,Runs,Hits,2B,3B,HR,RBI,SB,CS,BB,SO,BA,OBP,SLG,OPS,OPS+,TB,GDP,HBP,SH,SF,IBB
------------------------------------------------'''

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import datasets


def get_data(fileName):
    df = pd.read_csv(fileName)
    return df

#creating a knn model and training it on the iris data
def train_knn_model():
    # Load data
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    # Create standardizer
    standardizer = StandardScaler()

    # Standardize features
    X_std = standardizer.fit_transform(X)
    # Train a KNN classifier with 5 neighbors
    knn = KNeighborsClassifier(n_neighbors=13, n_jobs=-1).fit(X_std, y)
    return(knn)

#preprocessing the full_roster.csv file
def preprocess_roster(df):
    roster = df.drop(['Age', 'B', 'T', 'Country', 'Ht', 'Wt', 'DoB', 'Yrs', 'Batting', 'WAR', 'Status'], axis=1)
    print(roster)
   
    data=list(zip(roster))
    print(data)
    # data = np.array(roster)
    # Create standardizer
    standardizer = StandardScaler()
    # Standardize features
    X = standardizer.fit_transform(data)
   

    # pitchers = roster.drop(['C','1B','2B','3B','SS','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # catchers = roster.drop(['P','1B','2B','3B','SS','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # firstB = roster.drop(['P','C','2B','3B','SS','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # secondB = roster.drop(['P','C','1B','3B','SS','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # thirdB = roster.drop(['P','C','1B','2B','SS','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # shortstop = roster.drop(['P','C','1B','2B','3B','LF','CF','RF','OF','DH','PH','PR'], axis=1)
    # leftfield = roster.drop(['P','C','1B','2B','3B','SS','CF','RF','OF','DH','PH','PR'], axis=1)
    # centerfield = roster.drop(['P','C','1B','2B','3B','SS','LF','RF','OF', 'DH','PH','PR'], axis=1)
    # rightfield = roster.drop(['P','C','1B','2B','3B','SS','LF','CF','OF','DH','PH','PR'], axis=1)
    # outerfield = roster.drop(['P','C','1B','2B','3B','SS','LF','CF','RF','DH','PH', 'PR'], axis=1)
    # desighit = roster.drop(['P','C','1B','2B','3B','SS','LF','CF','RF','OF', 'PR', 'PH'], axis=1)
    # pinchhit = roster.drop(['P','C','1B','2B','3B','SS','LF','CF','RF','OF','DH', 'PR'], axis=1)
    # pinchrun = roster.drop(['P','C','1B','2B','3B','SS','LF','CF','RF','OF','DH','PH'], axis=1)
    # return (pitchers, catchers, firstB, secondB, thirdB, shortstop, leftfield, centerfield, rightfield, outerfield, desighit, pinchhit, pinchrun)
    return X
'''    
def find_pitchers(df):
    # Name  Age  B  T    G   GS  Defense   P
    games = df.drop(['Name', 'Age', 'B', 'T'], axis=1)
    X = np.array(games)
    # Create standardizer
    standardizer = StandardScaler()

    # Standardize features
    X_std = standardizer.fit_transform(X)
    # Train a KNN classifier with 5 neighbors
    knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(X_std, y)

    return 0

def find_catchers(df):
    print(df)
    return 0


def find_firstB(df):
    print(df)
    return 0


def find_secondB(df):
    print(df)
    return 0


def find_thirdB(df):
    print(df)
    return 0


def find_shortstop(df):
    print(df)
    return 0


def find_leftfield(df):
    print(df)
    return 0


def find_centerfield(df):
    print(df)
    return 0


def find_rightfield(df):
    print(df)
    return 0


def find_outerfield(df):
    print(df)
    return 0


def find_desighit(df):
    print(df)
    return 0


def find_pinchhit(df):
    print(df)
    return 0  


def find_pinchrun(df):
    print(df)
    return 0
'''
def main():
    roster_file = "full_roster.csv"
    roster_df = get_data(roster_file)
    knn = train_knn_model()
    X = preprocess_roster(roster_df)
    # Predict the class of two observations
    knn.predict(X)
    # find_pitchers(pitchers)
    '''
    pitchers, catchers, firstB, secondB, thirdB, shortstop, leftfield, centerfield, rightfield, outerfield, desighit, pinchhit, pinchrun = preprocess_roster(roster_df)
    find_pitchers(catchers)
    find_pitchers(firstB)
    find_pitchers(secondB)
    find_pitchers(thirdB)
    find_pitchers(shortstop)
    find_pitchers(leftfield)
    find_pitchers(centerfield)
    find_pitchers(rightfield)
    find_pitchers(outerfield)
    find_pitchers(desighit)
    find_pitchers(pinchhit)
    find_pitchers(pinchrun)
    '''
main()