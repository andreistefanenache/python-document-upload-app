import pytest
from documents import allowed_file

def test_allowed_file_with_allowed_extension():
    filename = "example.pdf"
    assert allowed_file(filename)

def test_allowed_file_with_allowed_extension_uppercase():
    filename = "example.MD"
    assert allowed_file(filename)

def test_allowed_file_with_not_allowed_extension():
    filename = "example.exe"
    assert not allowed_file(filename)

def test_allowed_file_with_multiple_dots():
    filename = "example.txt.pdf"
    assert not allowed_file(filename)

def test_allowed_file_with_allowed_extension_and_path():
    filename = "path/to/example.md"
    assert allowed_file(filename)

if __name__ == "__main__":
    pytest.main()
