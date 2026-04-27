# Manual Test Plan — Headline Analyser

## Objective

Verify that the headline program:

- reads data from a file
- creates `Headline` objects correctly
- computes word counts accurately
- handles errors gracefully

---

## Test Environment

- Python installed
- Project structure:

```
headline.py
main.py
headlines.txt
```

---

## Test Data

**headlines.txt**

```
General election: Labour and Tories clash over tax
England crowned T20 world champions
Summer travel chaos feared as airline strikes loom
```

---

# Test Cases

## 1. Basic File Load

**Purpose**
Check the program reads headlines from a file.

**Steps**

1. Ensure `headlines.txt` exists with valid content
2. Run the program

**Expected Result**

- Program runs without errors
- Headlines are printed or processed

---

## 2. Object Creation

**Purpose**
Verify each line becomes a `Headline` object

**Steps**

1. Add debug print or output:
   - print(type(headline))

2. Run the program

**Expected Result**

- Each item is `<class 'Headline'>`

---

## 3. Word Count Accuracy

**Purpose**
Ensure `get_word_count()` works correctly

**Steps**

1. Run program
2. Observe output

**Expected Result**

| Headline                                           | Expected Word Count |
| -------------------------------------------------- | ------------------- |
| General election: Labour and Tories clash over tax | 8                   |
| England crowned T20 world champions                | 6                   |
| Summer travel chaos feared as airline strikes loom | 9                   |

---

## 4. Empty Line Handling

**Purpose**
Check behaviour with blank input

**Steps**

1. Add an empty line to `headlines.txt`
2. Run program

**Expected Result (choose your behaviour)**

- Either:
  - empty line is ignored

- Or:
  - handled without crashing

---

## 5. Missing File

**Purpose**
Verify error handling

**Steps**

1. Rename `headlines.txt` → `missing.txt`
2. Run program

**Expected Result**

- Program does not crash
- Displays message like:

  ```
  File not found
  ```

---

## 6. Malformed Data

**Purpose**
Check robustness of input handling

**Steps**

1. Add unusual lines:

   ```
   !!!

   123 456
   ```

2. Run program

**Expected Result**

- Program still runs
- Word count still works (or handled safely)

---

## 7. Large Input

**Purpose**
Basic performance sanity check

**Steps**

1. Duplicate headlines many times (e.g. 100+ lines)
2. Run program

**Expected Result**

- Program completes quickly
- No noticeable slowdown

---

# Optional Checks

## String Representation

**Steps**

1. Print a `Headline` object

**Expected Result**

```
General election... (BBC News)
```

---

## Method Behaviour

**Steps**

1. Call `get_word_count()` manually

**Expected Result**

- Returns integer
- Matches manual count

---

# What This Teaches (explicitly call this out)

- You can test software **without frameworks**
- A test is:
  - setup → action → expected result

- Manual testing is about:
  - **confidence**, not perfection

---

# Nice closing line for your session

> “What we just did manually… is exactly what automated tests do for us later.”
