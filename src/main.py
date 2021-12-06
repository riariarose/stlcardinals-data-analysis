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

# use KNN algorithm to find the best players from sklearn


def knn_algorithm(df):
    """
    Uses KNN algorithm to find the best players from sklearn
    """
    # split the dataframe into two dataframes
    X = df.drop(['Name', 'calculated', 'WAR'], axis=1)
    y = df['calculated']
    # split the data into training and testing data
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, test_size=0.2)
    # create a KNN model
    knn = sklearn.neighbors.KNeighborsClassifier()
    # train the model
    knn.fit(X_train, y_train)
    # predict the model
    predictions = knn.predict(X_test)
    # calculate the accuracy of the model
    accuracy = sklearn.metrics.accuracy_score(y_test, predictions)
    print(accuracy)
