"""
Created on 2019-02-08

@author: Evan Yathon

This script tests the get_all_distances function of the pydistrrr package.

get_all_distances compares an input reference vector to all rows of an input data
frame, calculating the specified distance/similarity metric for each row.
"""
import pytest
import pandas as pd
from pydistrrr.get_closest import get_closest
