"""
Final Project: Cardinals

Task 2: The top 6 best performing players per position based on game statistics

"""

###### Imports ######
import pandas as pd
import numpy as np
import sklearn


###### Functions ######
def get_top_performers(df, position):
    """
    Returns the top 6 players in the given position based on their game statistics using kmeans clustering from sklearn
    """
    # Select the data for the given position
    df_pos = df[df['Position'] == position]
    # Drop the position column
    df_pos = df_pos.drop(['Position'], axis=1)
    # Convert the dataframe to a numpy array
    data = df_pos.values
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        data, data[:, 0], test_size=0.2, random_state=0)
    # Create a kmeans model
    model = sklearn.cluster.KMeans(n_clusters=6)
    # Fit the model to the training data
    model.fit(X_train)
    # Predict the clusters for the test data
    y_pred = model.predict(X_test)
    # Create a dataframe from the predictions
    df_pred = pd.DataFrame(y_pred, columns=['Cluster'])
    # Join the predictions to the test data
    df_pred = pd.concat([df_test, df_pred], axis=1)
    # Create a list of the top 6 players in the given position
    top_performers = []
    for i in range(6):
        top_performers.append(df_pred.loc[df_pred['Cluster'] == i].iloc[0, 0])
    return top_performers


def get_data():
    """
    Reads in the data from the CSV file and returns a dataframe
    """
    df = pd.read_csv('data/Zach_Data.csv')
    return df


def main():
    """
    Main function
    """
    df = get_data()
    print(df.head())
    print(get_top_performers(df, 'PG'))


main()
