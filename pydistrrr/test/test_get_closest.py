"""
Created on Fri Feb  8 10:05:13 2019

@author: Carrie Cheung

This script tests the get_closest function of the pydistrrr package.

The get_closest function returns indices of the top k rows in a dataframe that
are closest to a given observation based on a specified distance metric.

"""
import pytest
import pandas as pd
import numpy as np
from pydistrrr.get_closest import get_closest

# Sample input
x = [1, 1]
df = pd.DataFrame([[1, 1], [1, 2], [1, 3]])
k = 2


#### Test Outputs
def test_output_type():
    """
    Test that output is of type list
    """
    assert(type(get_closest(point=x, data=df, top_k=k)) == list)


def test_output_size():
    """
    Test that output has a length = k, or smaller if
    the size of input df is smaller than k
    """
    k_tests = [2,10]
    
    for k in k_tests:
        if len(df) >= k:
            assert(len(get_closest(point=x, data=df, top_k=k)) == k)
        else:  # k is larger than size of input dataframe
            assert(len(get_closest(point=x, data=df, top_k=k)) == len(df))


def test_output_ints():
    """
    Test that output contains ints only (also can be numpy ints)
    """
    output = get_closest(point=x, data=df, top_k=k)

    assert(all((isinstance(x, int)|isinstance(x,np.int64)) for x in output))


def test_output_positive():
    """
    Test that output contains non-negative ints
    (since they are indices, they cannot be negative)
    """
    output = get_closest(point=x, data=df, top_k=k)

    assert(all(x >= 0 for x in output))

#### Test Inputs
def test_input_data_type():
    """
    Test for error if data input is not a DataFrame
    """
    try:
        get_closest(point=x, data=[1, 2, 3], top_k=k)
    except TypeError:
        assert True


def test_input_point_all_numeric():
    """
    Test for error if input 'point' contains items other than numerics
    """
    non_num = [1,"two"]
    try:
        get_closest(point=non_num, data=df, top_k=k)
    except ValueError:
        assert True

def test_input_k_int():
    """
    Test for error if k is a non-neg int
    """
    try:
        get_closest(point=x, data=df, top_k=-2)
    except ValueError:
        assert True


def test_input_point_list():
    """
    Test for error if point is not a list
    """
    try:
        get_closest(point=1, data=df, top_k=k)
    except TypeError:
        assert True


def test_input_dist_string():
    """
    Test for error if metric is not a string
    """
    try:
        get_closest(x, data=df, top_k=k, metric=2)
    except TypeError:
        assert True

def test_input_dist_supported():
    """
    Test for error if metric is not a supported distance metric
    """
    try:
        get_closest(x, data=df, top_k=k, metric="mahalanobis")
    except ValueError:
        assert True
