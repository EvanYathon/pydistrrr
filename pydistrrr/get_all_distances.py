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

    #define distance metric function
    #placeholder, as the function will use get_distance
    def get_distance(point1, point2, metric = "euclidean"):
        if metric == "euclidean":
            ph = 0
            for i in range(0,len(point1)):
                ph += (point1[i]-point2[i])**2

            return ph**(1/2)

        elif metric == "cosine":
            dp = 0
            amag = 0
            bmag = 0

            for i in range(0,len(point1)):
                dp += point1[i]*point2[i]
                amag += point1[i]**2
                bmag += point2[i]**2

            amag = amag**(1/2)
            bmag = bmag**(1/2)

            return dp/(amag*bmag)

        elif metric == "man":
            ph = 0
            for i in range(0,len(point1)):
                ph += abs(point1[i]-point2[i])

            return ph

    distances = [] #empty vector to be filled with distances

    for obs in range(0,n):
        distances.append(get_distance(point, data.iloc[obs,], metric = dist))

    return distances
