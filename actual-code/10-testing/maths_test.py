from maths import add
import pytest

def test_pytest_is_running():
  assert True == True

# Happy Path
def test_two_whole_numbers_add_together_correctly():
  # Arrange
  number1 = 10
  number2 = 20
  expected = 30
  # Act
  result = add(number1, number2)
  # Assert
  assert result == expected


# Edge cases
# Big numbers, negative numbers, decimals
def test_two_large_numbers_give_correct_result():
  assert 2_000_000 == add(1_000_000, 1_000_000)


# Decorator -> enhance/add functionality to another function or method or class
@pytest.mark.parametrize("expected, number1, number2", (
  (-200, -100, -100),
  (3_000_010, 3_000_000, 10),
  (2, -5, 7),
))
def test_pairs_of_numbers_add_together_correctly(expected, number1, number2):
  assert expected == add(number1, number2)


def test_two_decimals_add_correctly():
  assert pytest.approx(0.3) == add(0.1, 0.2)

# Errors
def test_add_fails_when_adding_strings():
  with pytest.raises(TypeError):
    add("1", "2")  # "12"

@pytest.mark.parametrize("number1, number2", (
  ([], []),
  ("", []),
  ((), ""),
  (None, None),
  (True, True)
))
def test_add_fails_when_adding_non_numbers(number1, number2):
  with pytest.raises(TypeError):
    add(number1, number2)  # "12"