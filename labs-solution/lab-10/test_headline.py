# test_headline.py
#
# Lab 10 solution (labelled by step)

import pytest
from headline_module import Headline


# Step 2: Test object creation
def test_headline_stores_text_and_source():
    h = Headline("Hello world", "BBC")
    assert h.text == "Hello world"
    assert h.source == "BBC"


# Step 3: Test get_word_count
def test_get_word_count_counts_words():
    h = Headline("One two three", "BBC")
    assert h.get_word_count() == 3


# Step 4: Add one edge case
def test_get_word_count_empty_string_is_zero():
    h = Headline("", "BBC")
    assert h.get_word_count() == 0


# Step 5B: Parametrised test (reduce duplication)
@pytest.mark.parametrize(
    "text, expected",
    [
        ("One", 1),
        ("One two", 2),
        ("One two three", 3),
        ("", 0),
    ],
)
def test_get_word_count_cases(text, expected):
    h = Headline(text, "BBC")
    assert h.get_word_count() == expected


# Extra: @pytest.raises example 
# This test assumes Headline rejects non-string text or source.
# If your Headline currently accepts anything, delete this test, update the class or change the expectation.
def test_headline_rejects_non_string_text():
    with pytest.raises(TypeError):
        Headline(123, "BBC")
