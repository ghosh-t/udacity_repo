import pytest
from tryexcept import num_words  # Replace 'your_module' with the actual filename

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world", 2),                   # Regular case
        ("This is a test sentence", 5),       # Sentence with multiple words
        ("Python", 1),                         # Single word
        ("", 0),                               # Empty string
        ("   ", 0),                            # Only spaces
        ("Hello   world", 2),                  # Multiple spaces between words
        ("  Leading and trailing spaces  ", 4) # Spaces at start & end
    ]
)
def test_num_words_valid_cases(text, expected):
    """Test different valid input cases."""
    assert num_words(text) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [123, None, ["this", "is", "a", "list"], {"key": "value"}]  # Non-string inputs
)
def test_num_words_invalid_inputs(invalid_input):
    """Test non-string inputs, ensuring they return the expected error message."""
    assert num_words(invalid_input) == "text argument must be a string"
