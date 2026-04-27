# Lab 5: Building a Headline Analysis Toolkit with Functions

## Objective
In this lab, you'll practice writing functions to create a reusable, organized toolkit. You'll refactor your previous headline analysis script into functions that are easy to call and test.

## Scenario: Headline Toolkit with Functions
You're building a small “headline analysis toolkit” by splitting the work into functions:

- Set up the script with a headlines list
- Write a function to count words in one headline
- Write a function to search headlines by keyword
- Write a main function that uses your helpers and prints results

---

## Task 1: Getting Started

**Your task:** Set up your workspace and prepare the headline data.

**What to do:**
1. Create a new Python file called `headline_analyzer.py`
2. Copy the headlines list below into your file
3. Make sure the file runs without errors

**Headlines data (copy this into your file):**
```python
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]
```

**Expected outcome:**
- You should have a Python file with the headlines list
- The file should run without errors
- You're ready to start writing functions

**Check your work:**
- Does your file contain the headlines list?
- Can you run the file without errors?
- Are you ready to add functions?

<details>
<summary>Possible Solution for Task 1</summary>

```python
# headline_analyzer.py
# Copy/paste the headlines list so it's available for the functions below.
```

</details>

---

## Task 2: A Function to Get Word Count

**Your task:** Create a function that counts words in a single headline.

**What to do:**
1. Write a function called `get_word_count(headline_text)`
2. The function should take a single headline string as an argument
3. It should return the number of words in that headline

**Hints:**
- Start with `def get_word_count(headline_text):`
- Use the `.split()` method to break the headline into words
- Use `len()` to count the words
- Remember to use the `return` keyword

**Expected outcome:**
- A function that can count words in any headline
- The function should work when called with different headlines

**Check your work:**
- Does your function definition start with `def`?
- Does it take a parameter?
- Does it return a number?
- Can you test it with `print(get_word_count("This is a test headline"))`?

<details>
<summary>Possible Solution for Task 2</summary>

```python
def get_word_count(headline_text):
    return len(headline_text.split())
```

</details>

---

## Task 3: A Function to Find Headlines with a Keyword

**Your task:** Create a function that searches for headlines containing a specific keyword.

**What to do:**
1. Write a function called `find_headlines_with_keyword(list_of_headlines, keyword)`
2. The function should take the full list of headlines and a search term
3. It should return a new list containing only matching headlines

**Hints:**
- Start with `def find_headlines_with_keyword(list_of_headlines, keyword):`
- Create an empty list to store matching headlines
- Loop through each headline in the list
- Check if the keyword (in lowercase) is in the headline (also in lowercase)
- Add matching headlines to your list
- Return the list of matches

**Expected outcome:**
- A function that can search through any list of headlines
- It should return only the headlines that contain the keyword
- The search should be case-insensitive

**Check your work:**
- Does your function take two parameters?
- Does it create a new list for results?
- Does it loop through the headlines?
- Does it return the matching headlines?

<details>
<summary>Possible Solution for Task 3</summary>

```python
def find_headlines_with_keyword(list_of_headlines, keyword):
    keyword = keyword.lower()
    matches = []
    for h in list_of_headlines:
        if keyword in h.lower():
            matches.append(h)
    return matches
```

</details>

---

## Task 4: A Main Analysis Function

**Your task:** Create a main function that orchestrates the analysis and prints results.

**What to do:**
1. Write a function called `analyse_all_headlines(list_of_headlines)`
2. The function should calculate and display the average headline length
3. Use your `get_word_count()` function from Step 2

**Hints:**
- Start with `def analyse_all_headlines(list_of_headlines):`
- Create a counter for total words
- Loop through each headline
- Call your `get_word_count()` function for each headline
- Calculate the average and print it

**Expected outcome:**
- A function that analyzes all headlines
- It should display the average word count
- The output should be user-friendly

**Check your work:**
- Does your function call `get_word_count()`?
- Does it calculate the average correctly?
- Does it print the results clearly?

<details>
<summary>Possible Solution for Task 4</summary>

```python
def analyse_all_headlines(list_of_headlines):
    total_words = 0
    for headline in list_of_headlines:
        total_words += get_word_count(headline)

    avg = total_words / len(list_of_headlines)
    print(f"Average headline word count: {avg:.1f}")
```

</details>

---

## Tying It All Together

**Your task:** Call your functions to produce the final output.

**What to do:**
1. After defining all your functions, add code to call them
2. Test your `analyse_all_headlines()` function
3. Test your search function with different keywords
4. Display the results in a clear format

**Hints:**
- Call `analyse_all_headlines(headlines)` to see the analysis
- Test searching for different keywords like "new", "tax", "NHS"
- Use loops to display search results clearly
- Make your output organized and readable

**Expected outcome:**
- A complete program that demonstrates all your functions
- Clear output showing the analysis results
- Search results displayed in an organized way

**Check your work:**
- Does your program run without errors?
- Does it show the average headline length?
- Can you search for different keywords?
- Are the results displayed clearly?

---

## Example Interaction

```
Average headline word count: 7.7
Searching for keyword: new
Found 3 matches:
- New David Hockney exhibition opens in London
- Science discovers new way to tackle plastic waste
- Debate rages over future of Artificial Intelligence
```

---

**You're done when** your program can (1) compute the average word count across headlines using functions, and (2) search for a keyword and print the matching headlines.

---

## Key Concepts Demonstrated

- Defining functions: `def ...`
- Parameters and arguments: passing data into functions
- Return values: using `return` to produce a result
- Reuse: calling helper functions inside a main orchestration function
- Case-insensitive searching with `.lower()`

---

## Check your work

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:
- [ ] Can you explain what a function is and why we use them?
- [ ] Do you understand the difference between parameters and arguments?
- [ ] Can you explain what the `return` keyword does?
- [ ] Do you know how to call a function?

### Practical Skills:
- [ ] Can you write a function that takes parameters?
- [ ] Can you write a function that returns a value?
- [ ] Can you call functions from within other functions?
- [ ] Can you organize code into logical functions?

### If you answered "No" to any questions:
- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues

### Problem: "NameError: name 'get_word_count' is not defined"
**Fix:** Make sure you've defined your function before trying to call it.

### Problem: Function doesn't return anything
**Fix:** Check that you're using the `return` keyword in your function.

### Problem: Function parameters don't work
**Fix:** Make sure your function definition matches how you're calling it.

### Problem: Search function returns empty results
**Fix:** Check that you're converting both the keyword and headline to lowercase.

---

## Extension Ideas (Optional)
If you finish early, extend your functions while staying focused on the lab’s toolkit:

1. Add a helper like `get_average_word_count(list_of_headlines)` that returns a value instead of printing it.
2. Update your keyword search to return both matches and the match count (and then print them cleanly).
3. Add a small formatting helper so your printed output looks consistent and readable.

---

## Next Steps

In the next lab, you'll learn about:
- More advanced function features
- Working with different data types
- Building larger, more complex programs

Move on to Lab 6: Advanced Functions!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/lab-05` folder.**

- `solutions/headline_analyzer.py` - Complete solution with all functions
- `solutions/step_by_step/` - Individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:
1. Check the error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace! 