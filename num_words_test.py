import pytest
from tryexcept import num_words 

def test_num_words_regular_cases():
    """Test normal cases where text contains words."""
    assert num_words("Hello world") == 2
    assert num_words("This is a test sentence") == 5
    assert num_words("Python is awesome!") == 3
    assert num_words("One") == 1  # Single word case

def test_num_words_edge_cases():
    """Test edge cases such as empty strings and multiple spaces."""
    assert num_words("") == 0  # Empty string
    assert num_words("   ") == 0  # Only spaces
    assert num_words("Hello   world") == 2  # Multiple spaces between words
    assert num_words("  Leading and trailing spaces  ") == 4  # Spaces at start & end

def test_num_words_non_string_input():
    """Test cases where input is not a string."""
    assert num_words(123) == "text argument must be a string"  # Integer
    assert num_words(None) == "text argument must be a string"  # NoneType
    assert num_words(["this", "is", "a", "list"]) == "text argument must be a string"  # List
