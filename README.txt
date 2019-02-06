DSCI 524 Milestone 1 README
===========================

============== =================
Contributors   GitHub Handle
============== =================
Carrie Cheung  `carrieklc`_
Evan Yathon    `EvanYathon`_
Mike Yuan      `mikeymice`_
Shayne Andrews `shayne-andrews`_
============== =================

Project Summary
---------------

``distrrr`` and ``pydistrrr`` are R and Python packages respectively
that calculate distance metrics between vectors. Users can find closest
distances based either on a threshold distance or specified number of
outputs to find vectors that are similar to their input. These functions
are designed to be similar to `Scikit Learn’s Nearest Neighbors`_
functionality.

Functions
---------

+-------------------------+---------+-----------+---------------------+
| Function Name           | Input   | Output    | Description         |
+=========================+=========+===========+=====================+
| get_distance            | 3       | Single    | Given 2             |
|                         | paramet | float     | observations each   |
|                         | ers:    |           | represented by a    |
|                         | 2 lists |           | list of numeric     |
|                         | of      |           | values, compute and |
|                         | numeric |           | return the distance |
|                         | values, |           | between the 2       |
|                         | a       |           | points based on the |
|                         | string  |           | specified distance  |
|                         | specify |           | metric              |
|                         | ing     |           | (e.g. ``metric="euc |
|                         | type of |           | lidean"``)          |
|                         | distanc |           |                     |
|                         | e       |           |                     |
|                         | metric  |           |                     |
+-------------------------+---------+-----------+---------------------+
| get_all_distances       | 3       | List of   | Given a dataframe   |
|                         | paramet | floats of | and an observation  |
|                         | ers:    | length n  | represented by a    |
|                         | a       |           | single list of      |
|                         | datafra |           | numeric values,     |
|                         | me,     |           | compute and return  |
|                         | a list  |           | the distances       |
|                         | of      |           | between the single  |
|                         | numeric |           | observation and     |
|                         | values, |           | each observation in |
|                         | a       |           | the dataframe based |
|                         | string  |           | on the specified    |
|                         | specify |           | distance metric.    |
|                         | ing     |           | Will output a list  |
|                         | type of |           | of distances (as    |
|                         | distanc |           | numeric values)     |
|                         | e       |           | with size equal to  |
|                         | metric  |           | the number of rows  |
|                         |         |           | in the dataframe,   |
|                         |         |           | ``n``.              |
+-------------------------+---------+-----------+---------------------+
| filter_distances        | 3       | List of   | Similiar to         |
|                         | paramet | int (row  | ``get_all_distances |
|                         | ers:    | indices)  | ``                  |
|                         | a       |           | except indices of   |
|                         | datafra |           | rows/observations   |
|                         | me,     |           | with distances less |
|                         | a list  |           | than the threshold  |
|                         | of      |           | distance will be    |
|                         | numeric |           | returned.           |
|                         | values, |           |                     |
|                         | a       |           |                     |
|                         | numeric |           |                     |
|                         | (float  |           |                     |
|                         | or int) |           |                     |
|                         | value   |           |                     |
|                         | represe |           |                     |
|                         | nting   |           |                     |
|                         | a       |           |                     |
|                         | thresho |           |                     |
|                         | ld      |           |                     |
|                         | distanc |           |                     |
|                         | e       |           |                     |
+-------------------------+---------+-----------+---------------------+
| get_closest             | 4       | List of   | Similiar to         |
|                         | paramet | int (row  | ``get_all_distances |
|                         | ers:    | indices)  | ``                  |
|                         | a       | of length | except indices of   |
|                         | datafra | k         | the top ``k``       |
|                         | me,     |           | rows/observations   |
|                         | a list  |           | with the smallest   |
|                         | of      |           | distances are       |
|                         | numeric |           | returned.           |
|                         | values  |           |                     |
|                         | k, int  |           |                     |
|                         | for     |           |                     |
|                         | number  |           |                     |
|                         | of      |           |                     |
|                         | neighbo |           |                     |
|                         | urs,    |           |                     |
|                         | a       |           |                     |
|                         | string  |           |                     |
|                         | specify |           |                     |
|                         | ing     |           |                     |
|                         | type of |           |                     |
|                         | distanc |           |                     |
|                         | e       |           |                     |
|                         | metric  |           |                     |
+-------------------------+---------+-----------+---------------------+

Alignment with Python / R Ecosystems
------------------------------------

There are existing packages that implement the same proposed
functionality in both Python and R (listed below). Most of these
packages provide functions to calculate different distance metrics
between observations and/or also extend the functionality to compute the
k closest neighbors (KNN) of a given point based on a selected distance
metric.

===============================
Existing Packages/Functions
===============================
Sklearn's NearestNeighbors
Scipy's Spatial Distance Functions
R Distance Computations
R K Nearest Neighbors
===============================
