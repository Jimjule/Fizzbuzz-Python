import pytest
import sys
import os

sys.path.insert(0,'/Users/James/Projects/Python_Playground/fizzbuzz_python/lib')

from fizzbuzz import Fizzbuzz as fb

def test_normal_numbers():
    count = 0
    if fb.go(1) == 1:
        count += 1
    if fb.go(100000003) == 100000003:
        count += 1
    if fb.go(8) == 8:
        count += 1
    assert count == 3

def test_multiple_of_three_is_fizz():
    count = 0
    if fb.go(3) == "Fizz":
        count += 1
    if fb.go(6) == "Fizz":
        count += 1
    if fb.go(18000003) == "Fizz":
        count += 1
    assert count == 3

def test_multiple_of_five_is_buzz():
    count = 0
    if fb.go(5) == "Buzz":
        count += 1
    if fb.go(10) == "Buzz":
        count += 1
    if fb.go(50000000) == "Buzz":
        count += 1
    assert count == 3

def test_multiple_of_fifteen_is_fizzbuzz():
    count = 0
    if fb.go(15) == "Fizzbuzz":
        count += 1
    if fb.go(45) == "Fizzbuzz":
        count += 1
    if fb.go(30000015) == "Fizzbuzz":
        count += 1
    assert count == 3
