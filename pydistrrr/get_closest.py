"""
Created on Fri Feb  8 10:07:35 2019

@author: Carrie Cheung

Implementation of get_closest function in the pydistrrr package.

The get_closest function returns indices of the top k rows in a dataframe that
are closest to a given observation (point) based on a specified distance metric.
"""

# Import dependencies
import pandas as pd
import numpy as np
import warnings
from pydistrrr.get_all_distances import get_all_distances

def get_closest(point, data, top_k, metric="euclidean"):
    
    """
    Returns indices of the top k rows in a dataframe
    that are closest to a given observation based on
    a specified distance metric.

    Parameters
    ----------
    point : list
        Values defining a single observation
        to compute distances for.
        
    data : dataframe
        Dataframe containing values of all
        observations to calculate distances
        from point.
        
    top_k : int
        The number of closest observations to
        return indices for.
        
    metric: string
        Type of distance metric to use in distance
        calculations.
    
    Returns
    -------
    list
        Indices of the closest k observations
        from data.
    """
    # Check inputs are valid and as expected
    if not isinstance(data, pd.DataFrame):
        raise Exception("The data argument should be a pandas dataframe")
    
    if not isinstance(metric, str):
        raise Exception("The 'metric' argument should be a string")
    
    if top_k < 0 or not isinstance(top_k, int):
        raise Exception("The top_k argument should be a non-negative integer")

    if not isinstance(point, list):
        raise Exception("The point argument should be a list")
        
    if not all((isinstance(x, int)|isinstance(x, float)) for x in point):
        raise Exception("The point argument should contain only numerics")
        
    supported_dist = ["euclidean", "cosine", "manhattan"]
    if metric not in supported_dist:
        raise Exception("The 'metric' argument is not a supported distance metric")
    
    if top_k > len(data):
        warnings.warn("Warning: Note that since top_k is larger than the number of points in the dataframe, fewer than top_k indices will be returned.")
    
    # Call helper function to compute distances 
    distances = get_all_distances(point, data, metric)
    
    # Sort distances in ascending order (smallest distances first) 
    # and return indices in that order
    dist_index_sorted = list(np.argsort(distances))
    
    if len(distances) >= top_k:
        return dist_index_sorted[:top_k] # Returns first k rows
    else:
        return dist_index_sorted # Returns all rows