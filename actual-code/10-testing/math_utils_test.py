from math_utils import add
import pytest

def test_that_pytest_finds_this():
  pass

def test_two_numbers_add_together_properly():
  # Arrange
  num1 = 3
  num2 = 4
  expected = 7

  # Act
  result = add(num1, num2)

  # Assert
  assert result == expected

def test_two_negative_numbers_add_together_properly():
  assert add(-2, -2) == -4

# parameterize my test

@pytest.mark.parametrize("num1, num2, expected", [
  (-1, 1, 0),
  (1_000_000, 1_000_000, 2_000_000),
  (-10, 1_000_000, 999_990),
  (1_000_000, 10, 1_000_010),
  (0.1, 0.2, pytest.approx(0.3))
])
def test_a_variety_of_numbers_add_to_the_correct_value(num1, num2, expected):
  assert add(num1, num2) == expected


def test_floating_point_numbers_add_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3, 9)

@pytest.mark.parametrize("num1, num2, expected", [
  (-1.1, 1.1, 0),
  (0.123, 0.123, 0.246),
])
def test_a_variety_of_floating_point_numbers_add_to_the_correct_value(num1, num2, expected):
  assert add(num1, num2) == pytest.approx(expected)


# Test Driven Development
# - write a failing test (red)
# - write code to make it pass (green)
# - improve the test/code  (refactor)

def test_add_raises_error_when_passed_two_strings():
  with pytest.raises(TypeError):
    add("1", "2")

@pytest.mark.parametrize("val1, val2", [
  ("", ""),
  ("", 3),
  ([], []),
  ({}, [])
  ])
def test_add_raises_typeerror_when_trying_to_add_non_numbers(val1, val2):
  with pytest.raises(TypeError):  # assert that this throws this error
    add(val1, val2)
