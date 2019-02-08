"""
Created on Fri Feb  8 10:05:13 2019

@author: Carrie Cheung

This script tests the get_closest function of the pydistrrr package.

The get_closest function returns indices of the top k rows in a dataframe that
are closest to a given observation based on a specified distance metric.

"""
import pytest
import pandas as pd
from pydistrrr.get_closest import get_closest

# Sample input
x = [1, 1]
df = pd.DataFrame([[1, 1], [1, 2], [1, 3]])
k = 2


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
    if len(df) >= k:
        assert(len(get_closest(point=x, data=df, top_k=k)) == k)
    else:  # k is larger than size of input dataframe
        assert(len(get_closest(point=x, data=df, top_k=k)) == len(df))


def test_output_ints():
    """
    Test that output contains ints only
    """
    output = get_closest(point=x, data=df, top_k=k)

    assert(all(isinstance(x, int) for x in output))


def test_output_positive():
    """
    Test that output contains non-negative ints
    (since they are indices, they cannot be negative)
    """
    output = get_closest(point=x, data=df, top_k=k)

    assert(all(x >= 0 for x in output))


def test_input_data_type():
    """
    Test for error if data input is not a DataFrame
    """
    try:
        get_closest(point=x, data=[1, 2, 3], top_k=k)
    except:
        assert True
    else:
        assert False


def test_input_k_int():
    """
    Test for error if k is a non-neg int
    """
    try:
        get_closest(point=x, data=df, top_k=-2)
    except:
        assert True
    else:
        assert False


def test_input_point_list():
    """
    Test for error if point is not a list
    """
    try:
        get_closest(point=1, data=df, top_k=k)
    except:
        assert True
    else:
        assert False
