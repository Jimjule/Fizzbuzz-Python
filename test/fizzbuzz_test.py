import pytest
import sys
import os

sys.path.insert(0,'/Users/James/Projects/Python_Playground/fizzbuzz_python/lib')
print(sys.path)

from fizzbuzz import Fizzbuzz as fb

def test_one():
    assert fb.go(1) == 1

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
