"""
Created on 2019-02-08

@author: Evan Yathon

This script tests the get_all_distances function of the pydistrrr package.

get_all_distances compares an input reference vector to all rows of an input data
frame, calculating the specified distance/similarity metric for each row.
"""
import pytest
import pandas as pd
import sys
from pydistrrr.get_all_distances import get_all_distances

#initialize a sample dataframe and reference vector
df = pd.DataFrame({"A" : [1,2,3], "B" : [8,2,4]})
ref_vec = [-2,4]

def test_pandas_loaded():
    """
    Test that pandas package is loaded
    """
    assert('pandas' in sys.modules)

def test_output_length():
    """
    Test that the output vector length is the same as the
    number of rows in the input dataframe
    """
    assert(len(get_all_distances(ref_vec, df)) == df.shape[0])

def test_output_type():
    """
    Test that output is of type list
    """
    assert(type(get_all_distances(ref_vec, df)) == list)

def test_euclidean():
    """
    Test that the euclidean output works correctly
    """
    output = get_all_distances(ref_vec, df, metric = "euclidean")
    output_rounded = [round(dist,2) for dist in output]

    assert(output_rounded == [5,4.47,5])

def test_cosine():
    """
    Test that the cosine output works correctly
    """
    output = get_all_distances(ref_vec, df, metric = "cosine")
    output_rounded = [round(dist,2) for dist in output]

    assert(output_rounded == [0.83,0.32,0.45])

def test_manhattan():
    """
    Test that the manhattan output works correctly
    """
    output = get_all_distances(ref_vec, df, metric = "manhattan")
    output_rounded = [round(dist,2) for dist in output]

    assert(output_rounded == [7,6,5])

def test_second_arg_df():
    """
    Test that if the second argument isn't a data frame, an exception should be thrown
    """
    try:
        get_all_distances(ref_vec,[1,2,3])
    except:
        assert True

def test_second_arg_list():
    """
    Test that if the first argument isn't a list, an exception should be thrown
    """
    try:
        get_all_distances(df, df)
    except:
        assert True

def test_point_correct_length():
    """
    Point vector should be length k, the number of columns of the input dataframe
    """
    try:
        get_all_distances([1,2,3,4],df)
    except:
        assert True

def test_metric_input():
    """
    dist should be a string and one of 'cosine', 'euclidean' or 'manhattan'
    """
    try:
        get_all_distances(ref_vec,df, metric = "cityblock")
    except:
        assert True
