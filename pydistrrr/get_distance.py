#
# Created on Feb  8  2019
#
# @author: Mike Yuan
#
# Implementation of get_closest function in the pydistrrr package.


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


DISTANCE_FUNCTIONS = {
    "euclidean": get_euclidean,
    "cosine": get_cosine,
    "manhanttan": get_manhattan

}


def get_distance(point1, point2, metric="euclidean"):
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

    if(len(point1) == 0 or len(point2) == 0):
        raise ValueError("point cannot be empty list")

    if(len(point1) != len(point2)):
        raise AssertionError("points have unequal length")

    return DISTANCE_FUNCTIONS[metric](point1, point2)
