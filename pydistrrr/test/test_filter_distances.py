"""
Created on February 8, 2019

@author: Shayne Andrews

This script tests the filter_distances function of the pydistrrr package.

The filter_distances function returns indices of rows in a dataframe that are
within a given threshold distance from a given observation based on a specified
distance metric..

"""
import pytest
import pandas as pd
from pydistrrr.filter_distances import filter_distances

# Sample input
x = [1, 1]
df = pd.DataFrame([[1, 1], [1, 2], [1, 3]])
threshold = 0.9

def test_output_type():
    """
    Test that output is of type list
    """
    assert(type(filter_distances(point=x, data=df, threshold=threshold)) == list)


def test_output_ints():
    """
    Test that output contains ints only
    """
    output = filter_distances(point=x, data=df, threshold=threshold)

    assert(all(isinstance(x, int) for x in output))

def test_output_positive():
    """
    Test that output contains non-negative ints
    (since they are indices, they cannot be negative)
    """
    output = filter_distances(point=x, data=df, threshold=threshold)

    assert(all(x >= 0 for x in output))

def test_input_threshold_single():
    """
    Test for error if input threshold is not a single value
    """
    try:
        filter_distances(point=x, data=df, threshold=[1,2,3])
    except:
        assert True

def test_input_threshold_numeric():
    """
    Test for error if input threshold is not a single value
    """
    try:
        filter_distances(point=x, data=df, threshold="five")
    except:
        assert True

def test_input_threshold_positive():
    """
    Test for error if threshold is negative
    """
    try:
        filter_distances(point=x, data=df, threshold=-5.5)
    except:
        assert True
