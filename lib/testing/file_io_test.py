# test_file_io.py

import pytest
from file_io import write_file, append_file, read_file

@pytest.fixture
def tmp_file(tmp_path):
    """Fixture to create temporary file path."""
    return tmp_path / "test_file.txt"

def test_write_file(tmp_file):
    """Test write_file()"""
    file_content = "This is a test content."
    write_file(tmp_file, file_content)
    assert read_file(tmp_file) == file_content

def test_append_file(tmp_file):
    """Test append_file()"""
    file_content = "This is a test content."
    append_content = "\nAppended content."
    write_file(tmp_file, file_content)
    append_file(tmp_file, append_content)
    assert read_file(tmp_file) == file_content + append_content

def test_read_file(tmp_file):
    """Test read_file()"""
    file_content = "This is a test content."
    write_file(tmp_file, file_content)
    assert read_file(tmp_file) == file_content
