import pytest
from sciware_testing_python import sum_numbers, add_vectors

def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum1 = sum_numbers([1,2,3])
    assert sum1 == 6

def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    sum2 = sum_numbers([2, 4, 6])
    assert sum2 == 12

def test_sum_numbers_empty():
    # what's the sum of an empty list?
    sum3 = sum_numbers([])
    assert sum3 == 0

#@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    #assert sciware_testing_python.sum_numbers(["1","2","3"]) == "123"
    pass

# Write a test for the add_vectors function

# Write a test for sum_numbers on a list of booleans
