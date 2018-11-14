import sys
# import pytest

# Those imports fails in vscode-python 2018.10.1, but works in 2018.9.0
import asdfasdf
from asdfasdf.some_file import SomeFile

def test_function():
    a = SomeFile()
    print(a.some_function())

if __name__ == '__main__':
    # pytest.main(sys.argv)
    test_function()
