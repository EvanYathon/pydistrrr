"""
Created on February 8, 2019

@author: Shayne Andrews

Implementation of filter_distances function in the pydistrrr package.
"""

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

    indices = []
    return indices
