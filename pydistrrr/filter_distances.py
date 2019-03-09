"""
Created on February 8, 2019

@author: Shayne Andrews

Implementation of filter_distances function in the pydistrrr package.
"""

from pydistrrr.get_all_distances import get_all_distances
import pandas as pd

def filter_distances(point: list, data: pd.DataFrame, threshold: float, metric: str="euclidean") -> list:

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

    metric: string
        Type of distance metric to use in distance
        calculations.

    Returns
    -------
    list
        Indices of the observations with distance less
        than `threshold` from `point`
    """

    if not isinstance(threshold, float):
        raise Exception("The threshold argument should be a single number (float)")

    if threshold < 0:
        raise Exception("The threshold argument should be non-negative")

    # Call helper function to compute distances
    distances = get_all_distances(point, data, metric)

    indices = []
    for i, d in enumerate(distances):
        if d <= threshold:
            indices.append(i)

    return indices
