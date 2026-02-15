# FIRST : import the functions you need to test from modules
from main import get_weather 
# then : write test finctions starting with "test_"
def test_get_weather ():
    assert get_weather(21) =="hot"