import sys
import pytest

# Those imports fails, but used to work
import aqp
from aqp.some_file import SomeFile


def test_function():
    a = SomeFile()
    print(a)

if __name__ == '__main__':
    # pytest.main(sys.argv)
    test_function()
