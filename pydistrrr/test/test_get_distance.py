# Created on Feb  2019
#
# @author: Mike Yuan
#
# This script tests the get_distnace function of the pydistrrr package.
#

import pytest
import numpy as np
from scipy.spatial import distance
from pydistrrr.get_distance import get_distance
from typing import List

# dummy input
point1 = [1, 1]
point2 = [1, 2]
point3 = [1, 2, 3, 4, 5]
point4 = [5, 4, 3, 2, 1]

empty_point: List[int] = []
bad_point = ["2", "hello"]

# helper function


def get_manhattan_dist(point1, point2):
    """
    Helper function to verfiy manhhantan distance
    """
    a1 = np.asarray(point1)
    a2 = np.asarray(point2)
    return np.sum(abs(a1 - a2))

# test cases


def test_correct_eclidean():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="euclidean") == distance.euclidean(point1, point2)


def test_correct_cosine():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="cosine") == (1 - distance.cosine(point1, point2))


def test_correct_manhattan():
    """
    Test if the correct distance is return based on the metric
    """

    assert get_distance(
        point1, point2, metric="manhattan") == get_manhattan_dist(point1, point2)


def test_null_list_input():
    """
    Test if the Value error will be raised if one of the parameter is empty list
    """
    with pytest.raises(ValueError, match=r'.*empty list.*'):
        get_distance(point1, empty_point)
        #get_distance(empty_point, point1)


def test_unequal_length_in_list():
    """
    Test if assertion error will be thrown if the lists have different length
    """
    with pytest.raises(ValueError, match=r'.*unequal length.*'):
        get_distance(point1, point3)
        #get_distance(point3, point1)


def test_non_numeric_element_input():
    """
    Test if the Value error will be raised if one of the parameter has non-numeric
    """
    with pytest.raises(ValueError, match=r'.*non-numeric element.*'):
        get_distance(point1, bad_point)
        #get_distance(bad_point, point1)


def test_non_numeric_element_output():
    """
    Test if the Value error will be raised if one of the parameter is empty list
    """
    with pytest.raises(ValueError, match=r'.*non-numeric value.*'):
        get_distance(point1, point2, testing='output')


def test_incorrect_metric():
    """
    Test if the metric provided is correct
    """
    with pytest.raises(KeyError, match=r'.*metric has to be one of'):
        get_distance(point1, point2, metric="error test")
