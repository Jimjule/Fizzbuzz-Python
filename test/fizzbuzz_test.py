import pytest
import sys
import os

sys.path.insert(0,'/Users/James/Projects/Python_Playground/fizzbuzz_python/lib')
print(sys.path)

from fizzbuzz import Fizzbuzz as fb

def test_one():
    assert fb.go(1) == 1

def test_three_is_fizz():
    assert fb.go(3) == "Fizz"
