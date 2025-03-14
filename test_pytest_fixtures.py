import pytest
import tryexcept as t 

# test function - num_words
@pytest.fixture
def sample_texts():
    return {
        '2_simple': 'hello world',
        '5_sentence': 'this is a complete sentence.',
        '1_word': 'python',
        '0_empty': '',
        '0_empty_spaces': '  ',
        '2_multiple_spaces': 'hello    world',
        '4_leading_trailing': '   leading and trailing spaces   '
    }

@pytest.fixture
def invalid_inputs():
    return [123, None, ["this", "is", "a", "list"], {"key": "value"}]

def test_num_words_sample_texts(sample_texts):
    assert t.num_words(sample_texts['2_simple']) == 2
    assert t.num_words(sample_texts['5_sentence']) == 5
    assert t.num_words(sample_texts['1_word']) == 1
    assert t.num_words(sample_texts['0_empty']) == 0
    assert t.num_words(sample_texts['0_empty_spaces']) == 0
    assert t.num_words(sample_texts['2_multiple_spaces']) == 2
    assert t.num_words(sample_texts['4_leading_trailing']) == 4

def test_num_words_invalid_inputs(invalid_inputs):
    for invalid in invalid_inputs:
        assert t.num_words(invalid) == "text argument must be a string"
