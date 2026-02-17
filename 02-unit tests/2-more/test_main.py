from main import add , divide
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0)==0
def test_divide():
    assert divide(1,0)=="cannot divide by Zero"