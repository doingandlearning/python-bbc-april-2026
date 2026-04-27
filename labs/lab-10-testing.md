# Lab 10: Testing a Small Class with pytest

## Objective

In this lab, you'll write a few automated tests for the `Headline` class using `pytest`.

You are **not** changing the `Headline` code — only writing tests.

## Scenario: Locking in Behavior with pytest
You have a `Headline` class that should behave consistently (store text/source correctly and compute word counts). Tests help you catch regressions if the implementation changes later.

---

## Task 1: Create your test file

**Your task:**

- Create a new file called `test_headline.py`
- Place it next to `headline_module.py`
- Import the `Headline` class

**Check**

- Running `pytest` should find the file (even if there are no tests yet)

<details>
<summary>Possible Solution for Task 1</summary>

```python
# test_headline.py
from headline_module import Headline
```

</details>

---

## Task 2: Test object creation

**Your task:**

- Write a test that:
  - creates a `Headline`
  - checks that the text is stored correctly
  - checks that the source is stored correctly

**Hints**

- Test function names must start with `test_`
- Use `assert`
- Use very simple text (e.g. two words)

**Check**

- The test fails if you change the expected value
- The test passes when values are correct

<details>
<summary>Possible Solution for Task 2</summary>

```python
def test_headline_object_creation():
    h = Headline("hello world", "BBC News")
    assert h.text == "hello world"
    assert h.source == "BBC News"
```

</details>

---

## Task 3: Test `get_word_count`

**Your task:**

- Write a test for `get_word_count`
- Choose text where the word count is obvious
- Assert that the returned value is correct

**Hints**

- Don’t overthink punctuation yet
- One clear test case is enough

**Check**

- If you change the text, the expected count should change too

<details>
<summary>Possible Solution for Task 3</summary>

```python
def test_get_word_count():
    h = Headline("one two three", "BBC News")
    assert h.get_word_count() == 3
```

</details>

---

## Task 4: Add one edge case

Pick **one** edge case and write a test for it.

Examples (choose one):

- empty string
- single word
- multiple spaces between words

**Your task:**

- Decide what _should_ happen
- Write a test that locks that behaviour in

**Check**

- Your test documents a decision about behaviour

<details>
<summary>Possible Solution for Task 4</summary>

```python
def test_get_word_count_empty_string():
    h = Headline("", "BBC News")
    assert h.get_word_count() == 0
```

</details>

---

## Task 5: Reduce duplication (choose one)

Pick **one** way to tidy your tests.

### Option A: Helper function

- Create a small helper that returns a `Headline`
- Use it in at least two tests

### Option B: Parametrised test

- Use `@pytest.mark.parametrize`
- Test multiple word-count cases with one test function

### Option C: Leave it alone

- If your tests are already clear and short, stop here

<details>
<summary>Possible Solution for Task 5</summary>

```python
# Option A idea (helper function)
def make_headline(text: str) -> Headline:
    return Headline(text, "BBC News")
```

</details>

---

## Example Interaction

```
pytest
==================== 3 passed in 0.01s ====================
```

---

**You're done when** `pytest` finds your test file and your tests all pass (and you can lock in at least one edge-case decision).

---

## Key Concepts Demonstrated

- Tests as small Python functions
- Using `assert` to check expected behavior
- Designing tests to document decisions
- Keeping tests readable and not overly duplicated

---

## Check your work

### Running your tests

Run tests with:

```bash
pytest
```

Optional:

```bash
pytest -v
```

---

## What matters

- Tests are just Python functions
- `assert` is the key idea
- One test = one behaviour
- Tests describe how your code _should_ behave

---

## Common Issues

- `pytest` can’t find your test file: make sure the filename starts with `test_`
- Your assertions never run: double-check that you wrote `test_...` functions
- Tests fail after you change expected output: update the expected values to match the intended behavior

---

## Extension Ideas (Optional)
If you finish early, add more tests while keeping to the behavior already covered in Tasks 1–4:

1. Write a test for `__str__` (what `print(headline)` / `str(headline)` should show).
2. Add one more `get_word_count` edge case (for example: multiple spaces between words).
3. Use parametrization to test several word-count cases in one test function.

---

## Next Steps

In the next lab, you'll read and process data from a CSV file (`lab-11-files`).
