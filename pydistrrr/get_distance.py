#
# Created on Feb  8  2019
#
# @author: Mike Yuan
#
# Implementation of get_closest function in the pydistrrr package.

# Global variables

import numpy as np

NUMERIC_TYPES = [int, float, complex]

# helper functions for the distances


def get_euclidean(point1, point2):
    ph = 0
    for i in range(0, len(point1)):
        ph += (point1[i] - point2[i])**2

    return ph**(1 / 2)


def get_cosine(point1, point2):
    dp = 0
    amag = 0
    bmag = 0

    for i in range(0, len(point1)):
        dp += point1[i] * point2[i]
        amag += point1[i]**2
        bmag += point2[i]**2

    amag = amag**(1 / 2)
    bmag = bmag**(1 / 2)

    return dp / (amag * bmag)
    # return distance.cosine(point1, point2)


def get_manhattan(point1, point2):
    ph = 0
    for i in range(0, len(point1)):
        ph += abs(point1[i] - point2[i])
    return ph


DISTANCE_FUNCTIONS = {
    "euclidean": get_euclidean,
    "cosine": get_cosine,
    "manhattan": get_manhattan

}


# helper functions for the distances
def get_euclidean(point1, point2):
    ph = 0
    for i in range(0, len(point1)):
        ph += (point1[i] - point2[i])**2

    return ph**(1 / 2)


def get_cosine(point1, point2):
    dp = 0
    amag = 0
    bmag = 0

    for i in range(0, len(point1)):
        dp += point1[i] * point2[i]
        amag += point1[i]**2
        bmag += point2[i]**2

    amag = amag**(1 / 2)
    bmag = bmag**(1 / 2)

    return dp / (amag * bmag)


def get_manhattan(point1, point2):
    ph = 0
    for i in range(0, len(point1)):
        ph += abs(point1[i] - point2[i])
    return ph


def contain_only_numeric_elements(point):
    """
    Return boolean based on whether the list contain any non_numeric contain
    only_numeric_elements

    Parameters
    ----------
    point: list
        Values defining a single observation
        to compute distances for

    Returns
    --------
    result: Boolean

    Example
    -------
    contain_only_numeric_elements([1,1.0,2.4]) return True

    contain_only_numeric_elements(["1", "two", "monday"]) return False
    """

    for p in point:
        if(type(p) not in NUMERIC_TYPES):
            return False
    return True


def get_distance(point1, point2, metric="euclidean", testing=None):
    """
    Returns ditance between point1 and point2 based on dist type that is passed
    from the dist parameter

    Parameters
    ----------
    point1 : list
        Values defining a single observation
        to compute distances for.

    point2 : list
        Dataframe containing values of all
        observations to calculate distances
        from point.

    dist: string
        Type of distance metric to use in distance
        calculations. default is  "euclidean" which return euclidean distance
        "cosine" return cosine similarity
        "man" return manhattan
        ""

    Returns
    -------
    float
        distance calculated based on the metric.
    """
    DISTANCE_FUNCTIONS = {
        "euclidean": get_euclidean,
        "cosine": get_cosine,
        "manhattan": get_manhattan

    }

    # check for empty list
    if(len(point1) == 0 or len(point2) == 0):
        raise ValueError("point cannot be empty list")

    # check for unequal length
    if(len(point1) != len(point2)):
        raise AssertionError("points cannot have unequal length")

    # check for incorrect metric input
    if (metric not in DISTANCE_FUNCTIONS):
        raise(KeyError("metric has to be one of 'euclidean','cosine', or 'manhattan'"))

    # check for non-numeric element in points
    if((not contain_only_numeric_elements(point1)) or
       (not contain_only_numeric_elements(point2))):
        raise ValueError("Points should not contain non-numeric element")

    # check output size and type
    result = DISTANCE_FUNCTIONS[metric](point1, point2)

    if(testing == 'output'):
        result = [1]  # test for non-numeric output

    if ((type(result) not in NUMERIC_TYPES)
            and (not np.isscalar(result) and type(result) is not str)):
        raise(ValueError("get_distance returned non-numeric value"))

    return result
