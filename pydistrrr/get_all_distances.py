"""
Created on 2019-02-08

@author: Evan Yathon

Implementation of get_all_distances function in the pydistrrr package.
"""

def get_all_distances(point, data, dist = "euclidean"):
    """
    Return distance/similarity metric for each row in a dataframe

    Compares an input reference vector to all rows of an input data frame, calculating the specified distance/similarity metric for each row.

    Parameters
    ----------
    data : pandas dataframe
    dataframe of size n by k to compare to ref_vec

    point: list
    list of length k to compare to the data frame

    dist: string
    string indicating type of distance metric

    Returns
    -------
    list
    numeric vector of length n containing distances for each row of data
    """

    n = data.shape[0]
    k = data.shape[1]
    


    distances = []
    return distances
