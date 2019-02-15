Pydistrrr
=========

  Contributors     GitHub Handle
  ---------------- -----------------------------------------------------
  Carrie Cheung    [carrieklc](https://github.com/carrieklc)
  Evan Yathon      [EvanYathon](https://github.com/EvanYathon)
  Mike Yuan        [mikeymice](https://github.com/mikeymice)
  Shayne Andrews   [shayne-andrews](https://github.com/shayne-andrews)

Project Summary
---------------

`pydistrrr` is a Python package that calculates distances between
numeric-based data points or observations. The currently supported
distance metrics are:

-   [Euclidean
    Distance](https://en.wikipedia.org/wiki/Euclidean_distance)
-   [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry)
-   [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)

In addition to computing distances, `pydistrrr` can identify the closest
data points to a given point based on a distance threshold, or based on
a user-specified number of points. These functions are designed to be
similar to [Scikit Learn's Nearest
Neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors)
functionality.

Functions
---------

  -------------------------------------------------------------------------------------------------------------------------------------------------------
  Function Name                                         Input                   Output                     Description
  ----------------------------------------------------- ----------------------- -------------------------- ----------------------------------------------
  get\_distance                                         3 parameters: 2 lists   Single float               Given 2 observations each represented by a
                                                        of numeric values, a                               list of numeric values, compute and return the
                                                        string specifying type                             distance between the 2 points based on the
                                                        of distance metric                                 specified distance metric (e.g.
                                                                                                           `metric="euclidean"`)

  get\_all\_distances                                   3 parameters: a         List of floats of length   Given a dataframe and an observation
                                                        dataframe, a list of    `n`                        represented by a list of numeric values,
                                                        numeric values, a                                  compute and return the distances between the
                                                        string specifying type                             single observation and each observation in the
                                                        of distance metric                                 dataframe based on the specified distance
                                                                                                           metric. Will output a list of distances (as
                                                                                                           numeric values) with size equal to the number
                                                                                                           of rows in the dataframe, `n`.

  filter\_distances                                     4 parameters: a         List of int (row indices)  Similiar to `get_all_distances` except indices
                                                        dataframe, a list of                               of rows/observations with distances less than
                                                        numeric values, a                                  the threshold distance will be returned.
                                                        numeric (float or int)                             
                                                        value representing a                               
                                                        threshold distance, a                              
                                                        string specifying type                             
                                                        of distance metric                                 

  get\_closest                                          4 parameters: a         List of int (row indices)  Similiar to `get_all_distances` except indices
                                                        dataframe of data       of length `k`              of the top `k` rows/observations with the
                                                        points, a list                                     smallest distances are returned. In the case
                                                        specifying values for a                            where there is a tie in distances between two
                                                        target point, an int                               or more points, the point with larger index in
                                                        for number of                                      the dataframe will be selected.
                                                        neighbours k, a string                             
                                                        specifying type of                                 
                                                        distance metric to                                 
                                                        calculate                                          
  -------------------------------------------------------------------------------------------------------------------------------------------------------

Alignment with Python / R Ecosystems
------------------------------------

There are existing packages that implement the same proposed
functionality in both Python and R (listed below). Most of these
packages provide functions to calculate different distance metrics
between observations and/or also extend the functionality to compute the
k closest neighbours (KNN) of a given point based on a selected distance
metric.

In our package, we will be implementing the distance metric calculations
manually rather than simply creating wrappers around existing functions.

  Existing Packages/Functions
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Sklearn's NearestNeighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors)
  [Scipy's Spatial Distance Functions](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
  [R Distance Computations](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/dist.html)
  [R K Nearest Neighbours](https://cran.r-project.org/web/packages/FNN/index.html)

Installation and Usage
----------------------

To install the package, simply run the below in your terminal:

`pip install git+https://github.com/UBC-MDS/pydistrrr.git`

Then simply import `pydistrrr` in your own development.

    # Example Usage
    >>> from pydistrrr import *
    >>> get_distance([1,2],[2,1])
    1.4142135623730951
