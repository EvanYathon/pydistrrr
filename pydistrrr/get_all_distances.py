"""
Created on 2019-02-08

@author: Evan Yathon

Implementation of get_all_distances function in the pydistrrr package.
"""
# import pandas and get_all_distances
from pydistrrr.get_distance import get_distance
import pandas as pd
import numpy as np

def get_all_distances(point, data, metric = "euclidean"):
    """
    Return distance metric for each row in a dataframe as compared to an input list

    Compares an input reference vector to all rows of an input data frame, calculating the specified distance/similarity metric for each row.

    Parameters
    ----------
    point: list
    list of length k to compare to data, containing only int or float types

    data : pandas dataframe
    dataframe of size n by k to compare to point

    metric: string
    string indicating type of distance metric

    Returns
    -------
    list
    numeric list of length n containing distances for each row of data

    Example
    -------
    df = pd.DataFrame({"A" : [1,2,3], "B" : [8,2,4]})
    point = [-2,4]
    get_all_distances(point, df, metric = "euclidean")
    >>> [5, 4.47, 5]
    """

    # raise error if dataframe isn't the correct type of object
    if not isinstance(data, pd.DataFrame):
        raise Exception("the data argument should be a pandas dataframe")

    # raise error if first argument isn't a list
    if not isinstance(point, list):
        raise Exception("the point argument should be type list")

    # raise error if point isn't all numeric
    for obs in point:
        if not isinstance(obs, int) and not isinstance(obs, float):
            raise Exception("point argument should be a list containing only type float or int")

    #raise error if df isn't all numeric
    for row in range(0,n):
        for col in range(0,k):
            if not isinstance(df.iloc[row,col],(int,np.integer)) and not isinstance(df.iloc[row,col],float):
                raise Exception("data argument should be a pandas dataframe containing only floats or integers")

    # number of observations in data frame
    n = data.shape[0]
    k = data.shape[1]

    # raise error if point isn't length k
    if len(point) != k:
        raise Exception("point vector length and number of columns in data should match")

    # raise error if metric isn't correctly defined
    if not metric in ["euclidean","cosine","manhattan"]:
        raise Exception("metric should be one of 'euclidean','cosine' or 'manhattan'")

    # empty vector to be filled with distances
    distances = []

    for obs in range(0,n):
        distances.append(get_distance(point, data.iloc[obs,], metric = dist))

    return distances
