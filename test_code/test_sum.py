import os, sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, path)

import pytest

from funcs import summ

def  test_sum():
  assert summ(10, 20) == 30, "Test Failed"

def  test_sum_2():
  assert summ(10, 2) == 30, "Test Failed"

def test_all():
  assert True == True, "Failed all tests"