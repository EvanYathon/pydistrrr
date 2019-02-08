"""
Created on Fri Feb  8 10:07:35 2019

@author: Carrie Cheung

Implementation of get_closest function in the pydistrrr package.
"""

def get_closest(point, data, top_k, dist="euclidean"):
    
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
        
    dist: string
        Type of distance metric to use in distance
        calculations.
    
    Returns
    -------
    list
        Indices of the closest k observations
        from data.
    """
    
    indices = []
    return indices