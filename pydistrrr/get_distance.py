#
# Created on Feb  8  2019
#
# @author: Mike Yuan
#
# Implementation of get_closest function in the pydistrrr package.


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

    distanace = -1  # dummy result
    return distanace
