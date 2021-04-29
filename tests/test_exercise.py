import pytest
from sciware_testing_python import sum_numbers, add_vectors

def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum1 = sum_numbers([1,2,3])
    assert sum1 == 6

def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    sum2 = sum_numbers([2, 1.5, 6])
    assert sum2 == 9.5

def test_sum_numbers_empty():
    # what's the sum of an empty list?
    sum3 = sum_numbers([])
    assert sum3 == 0

@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    assert sum_numbers(["1","2","3"]) == "123"

# Write a test for the add_vectors function
def test_add_vectors():
    a = [ 1, 2, 3]
    b = [ 3, 2, 1]
    c = add_vectors(a, b)
    assert c == [4, 4, 4]

# Write a test for sum_numbers on a list of booleans
