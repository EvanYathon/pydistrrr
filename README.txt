Pydistrrr
=========

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

``pydistrrr`` is a Python package that calculates distances between
numeric-based data points or observations. The currently supported
distance metrics are:

-  `Euclidean Distance`_
-  `Manhattan Distance`_
-  `Cosine Similarity`_

In addition to computing distances, ``pydistrrr`` can identify the
closest data points to a given point based on a distance threshold, or
based on a user-specified number of points. These functions are designed
to be similar to `Scikit Learn’s Nearest Neighbors`_ functionality.

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
|                         | ers:    | length    | represented by a    |
|                         | a       | ``n``     | list of numeric     |
|                         | datafra |           | values, compute and |
|                         | me,     |           | return the          |
|                         | a list  |           | distances between   |
|                         | of      |           | the single          |
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
| filter_distances        | 4       | List of   | Similiar to         |
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
|                         | e,      |           |                     |
|                         | a       |           |                     |
|                         | string  |           |                     |
|                         | specify |           |                     |
|                         | ing     |           |                     |
|                         | type of |           |                     |
|                         | distanc |           |                     |
|                         | e       |           |                     |
|                         | metric  |           |                     |
+-------------------------+---------+-----------+---------------------+
| get_closest             | 4       | List of   | Similiar to         |
|                         | paramet | int (row  | ``get_all_distances |
|                         | ers:    | indices)  | ``                  |
|                         | a       | of length | except indices of   |
|                         | datafra | ``k``     | the top ``k``       |
|                         | me      |           | rows/observations   |
|                         | of data |           | with the smallest   |
|                         | points, |           | distances are       |
|                         | a list  |           | returned. In the    |
|                         | specify |           | case where there is |
|                         | ing     |           | a tie in distances  |
|                         | values  |           | between two or more |
|                         | for a   |           | points, the point   |
|                         | target  |           | with larger index   |
|                         | point,  |           | in the dataframe    |
|                         | an int  |           | will be selected.   |
|                         | for     |           |                     |
|                         | number  |           |                     |
|                         | of      |           |                     |
|                         | neighbo |           |                     |
|                         | urs     |           |                     |
|                         | k, a    |           |                     |
|                         | string  |           |                     |
|                         | specify |           |                     |
|                         | ing     |           |                     |
|                         | type of |           |                     |
|                         | distanc |           |                     |
|                         | e       |           |                     |
|                         | metric  |           |                     |
|                         | to      |           |                     |
|                         | calcula |           |                     |
|                         | te      |           |                     |
+-------------------------+---------+-----------+---------------------+

Alignment with Python / R Ecosystems
------------------------------------

There are existing packages that implement the same proposed
functionality in both Python and R (listed bel

.. _carrieklc: https://github.com/carrieklc
.. _EvanYathon: https://github.com/EvanYathon
.. _mikeymice: https://github.com/mikeymice
.. _shayne-andrews: https://github.com/shayne-andrews
.. _Euclidean Distance: https://en.wikipedia.org/wiki/Euclidean_distance
.. _Manhattan Distance: https://en.wikipedia.org/wiki/Taxicab_geometry
.. _Cosine Similarity: https://en.wikipedia.org/wiki/Cosine_similarity
.. _Scikit Learn’s Nearest Neighbors: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors
