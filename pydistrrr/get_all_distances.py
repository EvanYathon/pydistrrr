"""
Created on 2019-02-08

@author: Evan Yathon

Implementation of get_all_distances function in the pydistrrr package.
"""

def get_all_distances(data, ref_vec, dist_type = "euclidean"):
    """
    Return distance/similarity metric for each row in a dataframe

    Compares an input reference vector to all rows of an input data frame, calculating the specified distance/similarity metric for each row.

    Parameters
    ----------
    data : pandas dataframe
    dataframe of size n by k to compare to ref_vec

    ref_vec: list
    list of length k to compare to the data frame

    dist_type: string
    string indicating type of distance metric

    Returns
    -------
    list
    numeric vector of length n containing distances for each row of data
    """

    distances = []
    return distances
