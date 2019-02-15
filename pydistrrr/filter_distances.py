"""
Created on February 8, 2019

@author: Shayne Andrews

Implementation of filter_distances function in the pydistrrr package.
"""

from pydistrrr.get_all_distances import get_all_distances
import pandas as pd

def filter_distances(point, data, threshold, dist="euclidean"):

    """
    Returns indices of rows in a dataframe that are
    within a given threshold distance from a given
    observation based on a specified distance metric.

    Parameters
    ----------
    point : list
        Values defining a single observation
        to compute distances for.

    data : dataframe
        Dataframe containing values of all
        observations to calculate distances
        from point.

    threshold : float
        The maximum distance of observations to
        return indices for.

    dist: string
        Type of distance metric to use in distance
        calculations.

    Returns
    -------
    list
        Indices of the observations with distance less
        than `threshold` from `point`
    """

    # Check inputs are valid and as expected
    if not isinstance(data, pd.DataFrame):
        raise Exception("The data argument should be a pandas dataframe")

    if not isinstance(dist, str):
        raise Exception("The dist argument should be a string")

    if threshold < 0 or not isinstance(threshold, float):
        raise Exception("The threshold argument should be a non-negative float")

    if not isinstance(point, list):
        raise Exception("The point argument should be a list")

    if not all((isinstance(x, int)|isinstance(x, float)) for x in point):
        raise Exception("The point argument should contain only numerics")

    supported_dist = ["euclidean", "cosine", "manhattan"]
    if dist not in supported_dist:
        raise Exception("The dist argument is not a supported distance metric")

    # Call helper function to compute distances
    distances = get_all_distances(point, data, dist)

    indices = []
    for i, d in enumerate(distances):
        if d <= threshold:
            indices.append(i)
    
    return indices
