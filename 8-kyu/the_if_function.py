# 8 kyu - The 'if' Function
# https://www.codewars.com/kata/54147087d5c2ebe4f1000805

from collections.abc import Callable

def _if(bool, func1: Callable, func2: Callable):
    if bool :
        func1()
        
    else :
        func2()

#--------Test --------------------------

from solution import _if
import codewars_test as test

f1_called, f2_called = False, False

def f1():
    global f1_called
    f1_called = True

def f2():
    global f2_called
    f2_called = True

@test.describe("Sample tests")
def _():
    global f1_called, f2_called
    f1_called, f2_called = False, False
    _if(True, f1, f2)
    test.assert_equals(f1_called, True)
    test.assert_equals(f2_called, False)

    f1_called, f2_called = False, False
    _if(False, f1, f2)
    test.assert_equals(f1_called, False)
    test.assert_equals(f2_called, True)
