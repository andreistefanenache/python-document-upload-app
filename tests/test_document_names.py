import pytest
from documents import generate_stored_filename

def test_generate_stored_filename_starts_with_prefix():
    filename = "example.txt"
    result = generate_stored_filename(filename)
    assert result.startswith("DYNAMIC_DOCUMENT_UPLOAD_")

def test_generate_stored_filename_contains_original_filename():
    filename = "example.txt"
    result = generate_stored_filename(filename)
    assert "example" in result

def test_generate_stored_filename_ends_with_correct_extension():
    filename = "example.txt"
    result = generate_stored_filename(filename)
    _, extension = filename.split('.')
    assert result.endswith("." + extension)

def test_generate_stored_filename_has_different_suffix():
    filename = "example.txt"
    result = generate_stored_filename(filename)
    new_result = generate_stored_filename(filename)
    assert result != new_result

if __name__ == "__main__":
    pytest.main()
