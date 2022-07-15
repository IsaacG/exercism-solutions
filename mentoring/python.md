# Python Mentoring Snippets

## TOC

* [General](#general)
* [Collatz](#collatz)
* [Raindrops](#raindrops)
* [High Scores](#high-scores)
* [Matrix](#matrix)
* [Protein Translation](#protein-translation)
* [Robot Name](#robot-name)
* [Pangram](#pangram)
* [RNA Transcription](#rna-transcription)


General
-------
```text
There's no need to comment just to say you submitted a new iteration; Exercism notifies mentors of new iterations.
Using a data type as part of the variable name is typically considered an anti-pattern. Prefer describing what the variable represents or is used for.
That data dict is a good candidate for a module-level constant. There is not need to have it recreated every time the function is called.
This code uses both double quotes and single quotes. Either is fine, but avoid mixing and matching! Consistent code is good code.
Single character variable names are usually not recommended, especially for any scope larger than one or two lines.
For type annotation, the `list` should be `list[int]` (for Py 3.9+) or `from typing import List; List[int]`
Docstrings should be imperative ("Do something ..." or "Return ...") vs descriptive ("Does sometime ..." or "Returns ...").
Submitting the test file is not necessary ... and makes reviewing your solution more difficult.
`Exception` is a base exception class and is very generic. It conveys the least amount of information of (almost) all the exceptions. Avoid using this directly and always prefer [a more specific exception](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
Exception messages should start with an uppercase letter and end with a period (just like docstrings). When possible, prove as much detail as possible in the message so the user can figure out what went wrong (like, the bad value or the type of the data). That makes acting on the error much easier.
Type checking is best done with the builtin `isinstance()` method.
`[f(a) for a in b]` iterates through `b` to create a list. You are then passing this list to `str.join()` which iterates through that list to build a string and discards that list. You can avoid that extra middle step of building and storing a list by passing a generator to `str.join()` instead and having `str.join()` process the elements of that iterator directly! You can do this either by doing `str.join(f(a) for a in b)` or `generator = (f(a) for a in b); str.join(generator)`
In Python, the `is` operator checks if two objects are the *same object* while `==` checks if two objects have the same *value*. `[1, 2] == [1, 2] -> True` but `[1, 2] is [1, 2] -> False`. You generally want to use `==` and only want `is` in very specific conditions.
In boolean logic (and Python), `var == True` is the same as `var` and `var == False` can be written `not var`.
In languages were strings are immutable (like Python and Go), string concatenations are relatively expensive and should generally not be done in loops. Instead, string building techniques should be used, like collecting string pieces in a list then making use of `str.join()`.
Function definitions should be separated from other expressions by exactly two blank lines.
Regular variables are usually named using `snake_case` and module constants use `ALL_CAPS`.
```

### Extra Credit

```text
If you want to go the extra step, type annotation is worth adding to your code!
Docstrings aren't required here but they are nice to have - both for the module and functions.
```

### Less common

```text
I enjoy helping mentor students on Exercism and occasionally I'll help out on IRC (irc://irc.freenode.net #python,##programming). I don't take email questions, though. I prefer setting the boundaries of where and how I volunteer my skills. If you're looking for programming help, I'd suggest trying out IRC, the Python Discord server or Stack Overflow.
```

Collatz
-------

```text
This code essentially builds a C-style for-loop with an init, condition and increment. In general, it's best to avoid `while` loops when a `for` loop can be used.  Using a `for` in this exercise is a bit tricky... but `itertools.count()` can help make that happen!
```

Raindrops
---------
<details><summary>Notes</summary>

```text
From a scalability perspective, can you solve this in a way that doesn't mean repeating a bunch of code for every sound/factor?
From a scalability perspective, can you avoid the (relatively) costly repeated string-append (which has to copy the entire string every time)?
This solution has two `return` points. Fewer `return` points makes for easier code readability since the code flows from the same start to the same end. Could you refactor the end bit so there is only one `return`?
Lines N-M could be reduced to a single line with a ternary operator or with the `or` keyword.
Python has a `+=` operator which is perfect for `int` incrementing or `str` appending.
The Pythonic way to test for an empty string/sequence is: `if not result: ...`
For a more compact and less repetitive solution you can use tuples or a dictionary for the data and a generator to loop over the data to build the sound.
What sound does `15` produce? What steps did you take in your head to solve that? Do you need to explicitly consider every combination of factors to solve that?
This solution tests all the factors two times. Do you need to test the factors more than once?
f-strings are fabulous for string formatting. If you just want to convert an `int` to a `str`, the builtin `str()` function works quite well.
Is it necessary to handle every single combination of factors to solve this exercise? Try to think how you'd solve what sound "15" makes in your head.
```
</details>

High Scores
-----------
<details><summary>Notes</summary>

```text
For your `top_three function`, would the builtin [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) function make this easier?
For the `personal_top_three`, would some of the optional flags to [`sorted`](https://docs.python.org/3/library/functions.html#sorted) clean up that function?
When taking a list slice `foo[0:3]`, the `0` is the default start so convention is to just omit it and prefer `foo[:3]`
For `personal_best`, do you need to sort the entire list? Or is there a more specific [builtin function](https://docs.python.org/3/library/functions.html) that could be used?
```

```text
What would the following code print out?
\```
scores = [3, 2, 1, 4]
print(latest(scores))
top = personal_top_three(scores)
print(latest(scores))
\```
```
</details>


Matrix
------
<details><summary>Notes</summary>

```text
You might want to use a linter/formatter. Typically, the `[` and `]` are not padded with spaces.
If a Matrix is constructed once then a bunch of rows and columns are read, this would convert the elements to `int()` many times. Moving that conversion to `__init__` allows you to do that just once. Additionally, if there's a non-int value, moving the conversion into `__init__` catches the data the first time it is handled versus maybe catching it lazily later in a more surprising fashion.
Python provides a [`str.splitlines`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) method that you may want to consider using.
Do you need to specify a separator for your per-line [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split) call?
Which of these do you find easier to read? `[int(i) for i in mylist]` or `list(map(int, mylist))`?
This solution maintains two copies of the data. If the data is large, that can be expensive. Can you solve this without maintaining two copies of the data?
Whenever you find yourself reaching for `for i in range(len(thing))`, ask yourself if you can use `for t in thing` instead. Often, that's sufficient. If you absolutely need the index, there is the `enumerate()` function. If you *only* need the index and not the actual value, only then is `range()` the right approach. In this case, you shouldn't actually need the index at all!
This solution combines functions that act on lists (`list(map(..))`) with list comprehensions. Could you solve this with the consistent use of just list comprehensions?
It's good practice to use a variable for just one purpose. It makes static type checking possible and keeps the logic clean since one variable isn't used for unrelated things. `self.matrix` is used to store two distinct data types.
Having single-statement functions is usually a bit of a red flag, especially if that function isn't called from multiple places. Is there any value in splitting out your `__init__()` into a second function other than as a way to name what a block of code is doing? Can a comment accomplish the same thing?
Note your `__init__` loops over the data twice, creating two different sets of data. Constructing the results you need in one loop halves your computational costs.
It's best to create your iterables where you use them, i.e. inside the `for x in iterable`. This keeps the logic local to where it's used and makes the code easier to read.
The data provided to the Matrix class is 2D data. This code flattens that to a 1D list then uses a bunch of logic to later extrapolate a 2D view from the 1D list. Could you simply maintain the 2D structure using, say, a list of lists and simplify the work here?
`column()` transposes the *entire* matrix then selects just one row, discarding the rest of the data. Do you need to actually transpose the matrix?
```

```text
List comprehensions are the Pythonic approach to generating a list from an iterable. Can you find and replace this pattern in your code?
```a
# Instead of doing this:
out = []
for a in b:
    out.append(func(a))
# Prefer this:
out = [func(a) for a in b]
```a
```

### Extra
```text
If you want to go the extra step, type annotation is worth adding to your code!
Fun fact. If someone does: `matrix.row(3)[0] = 5`, this will alter the data stored in the matrix. Conversely, if they did `matrix.column(3)[0] = 5`, this would *not* update the matrix. Making `row()` behave like `column()` is simple. The reverse is a fair bit more tricky. Something to think about :)
What does `Matrix('1\n2').row(0)` return? What *should* it return? Is this worth fixing?
Docstrings aren't required here but they are nice to have - both for the module and functions.

`self.matrix` contains a list of list objects. `row()` returns one of those objects. So `row(3)[0] = 5` is modifying the list that lives inside `self.matrix`. `column()`, on the other hand, copies the values from `self.matrix` into a new list object. The `int`s are copied but the list is a new list. That was, when you run `matrix.column(3)[0] = 5`, you're not actually changing anything about `self.matrix`.
[Here](https://gist.github.com/kroozo/d6cb56d64482280aecacc9a32f60b03d) is an example of how you could have both `column()` and `row()` provide mutable data backed by the same source.
Most people wouldn't use a `classmethod` here. Those are usually used for code that is typically called from outside of a class instance. While this technically can be a `classmethod`, it's not used as one and isn't how they are typically used in the Python world.
```
</details>


Protein Translation
-------------------
<details><summary>Notes</summary>

```text
The [`range`](https://docs.python.org/3/library/functions.html#func-range) function takes a `step` parameter which is useful for doing things like counting by 3s. That might be well suited for your `for` loop.
Is there any particular reason you're using `dict.get(key)` over the more traditional `dict[key]` lookup?
Note you can drop the `else` inside your loop and unindent the `list.append()`.
What's the purpose of having a default value for this function? Is the default a useful value?
Is there a reason for the `dict.get()` vs a regular lookup?
Does it make sense to store lists in your codons dictionary vs just string entries?
Recursion is fun and cool ... but not actually very efficient. Could a regular loop be used here?
Per the instructions, there are three STOP proteins. STOP isn't meant as the catch-all.
`textwrap.wrap()` is a cute way to chunk the text. However, [more_itertools.chunked](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.chunked) is a bit better matched for this.
Note how you got two distinct `return` points from this function. It might make more sense to simply break out of the loop when you're done and have a single return point. One return means less points to keep in sync.
A formatter tool might be worth running; there ought to be spaces around your `+` operator.
Rather than building the dict one entry at a time, you can define the dict all in one go. There's no need to have the dict name repeated so many times or to perform a whole lot of updates
Do you need a `try-except` to indirectly check if 'STOP' is in the list or can you check in a direct and explicit manner?
The Pythonic way to generate a list from an iterable is with list comprehensions.
Rather than ranging over each index and checking if it's a valid value, [`range()`](https://docs.python.org/3/library/functions.html#func-range) does support a step, letting you count by 3!
This solution iterates over the data two times, building two lists of data. Do you need two iterations or can you solve this in a single pass?
Python supports list slicing and string slicing. You can access a substring (or sub-list) using `str[start : end]`
For a cleaner way to chunk up the codon string, check out [more_itertools.chunked](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.chunked).
Do you need a regex for this? Regexes are a pretty heavy tool for splitting up a string.
The power of dictionaries lives in their fast hash-based lookups. If you are looping over all the elements of a dictionary, you are using them as a list of tuples and you miss out on their main advantage. Can you construct a mapping from codon to protein to use for fast (and simple) lookups?
```
</details>

Robot Name
----------
<details><summary>Notes</summary>

```text
You can get a random letter using `random.choice(string.ascii_uppercase)`
Lines N, M are duplicate code. You can reduce code duplication by calling `reset()` in your `__init__()`
A `set()` is ideal for maintaining an unordered set of non-repeating items. Checking membership and adding items is more efficient than in a `list`.
Your name generating function is recursive. Recursive functions are fun and neat and sometimes very useful. However, they are often very slow and expensive (compared to, say, a loop), especially when you need to recurse many times. Is recursion needed here?
If I created 100,000 robots, does this code ensure each robot will have a unique name?  If you're not familiar with it, you should take a look at [The Birthday Problem](https://en.wikipedia.org/wiki/Birthday_problem).
Your name generating function is recursive. Recursive functions are fun and neat and sometimes very useful. However, they are often very slow and expensive (compared to, say, a loop), especially when you need to recurse many times. Is recursion needed here?
A cleaner way to get 3 random digits would be `f"{random.randint(0, 999):03}"`
[`random.choices()`](https://docs.python.org/3/library/random.html#random.choices) might be a better fit than `random.choice` for this.
Your name generating function is recursive. Recursive functions are fun and neat and sometimes very useful. However, they are often very slow and expensive (compared to, say, a loop), especially when you need to recurse many times. Is recursion needed here?
In general, dunder-methods (double-underscore) should not be directly called when it can be helped. They are for internal use. Prefer instead to have `__init__` call -reset()`.
You might find [`string.ascii_uppercase`](https://docs.python.org/3/library/string.html#string.ascii_uppercase) useful here.
You can call `join()` fewer times by replacing `"".join(a) + "".join(b)` with `"".join(a + b)`
The purpose of classes and object oriented programming is to encapsulate all related logic in one object. If a function is only meant to be called from within an object, that code should be part of that object!
How well does this code scale if we decided to double the length of the robot name? Or make it 30 chars?
```
</details>

Pangram
-------
<details><summary>Notes</summary>

```text
[`string.ascii_lowercase`](https://docs.python.org/3/library/string.html#string.ascii_lowercase) might be useful here.
Suppose the input sentence is 100,000 characters long. Is it necessary to loop through each character to solve this?
Do you need to call `lower()` once for every character in the `sentence`? Function calls are cheap but not free.
Is it always necessary to loop through every letter to determine whether a sentence is a pangram?
Python has an [`any()`](https://docs.python.org/3/library/functions.html#all) and [`all()`](https://docs.python.org/3/library/functions.html#all) that might be helpful here.
Rather than calling `.lower()` a whole lot of times inside the loop, can you call it just once?
Is this sentence a pangram? "The quick brown fox jumped over the lazy dog." What steps did you take to determine that? Did you have to do any counting to accomplish that?
Python works quite well with strings and characters. It has methods like `str.isalpha()` and defined objects such as [`string.ascii_lowercase`](https://docs.python.org/3/library/string.html#string.ascii_lowercase). Is type conversion necessary?
The counting approach works fairly well and is an acceptable solution ... but isn't the approach that people tend to take when solving for a pangram in their head. It also is `O(n)` which is slower for large inputs.
Python has an [`all()`](https://docs.python.org/3/library/functions.html#all) that is designed specifically to clean up patterns like this one.
```

### Solutions

```python
return set(sentence.lower()).issuperset(string.ascii_lowercase)
return all(s in sentence.lower() for s in string.ascii_lowercase)
return len(c for c in sentence.lower() if c.isalpha()) == 26
```
</details>

RNA Transcription
-----------------
<details><summary>Notes</summary>

```text
For a more compact solution you can use a generator to loop over the data to build the DNA pieces then combine then with a `"".join()`.
If you want to go the extra step, type annotation is worth adding to your code!
Every time you do a string append, Python has to create a brand new string and discard the old string. This isn't a big deal when it's a small string or a small number of appends. However, when you do this a lot of times with a larger string, it can get expensive. Appending to an array, on the other hand, is relatively cheap. You can use an array to build a string by parts then something like `"\n".join(parts)` or `"".join(parts)` to combine them (using a more descriptive variable name than `parts` ideally).
Python is a pretty high level language with all sorts of string support. Can you come up with a solution that doesn't require someone pull out an ASCII table to read/modify?
For a more compact and less repetitive solution you can build a translation map (typically done with a `dict` though [`str.maketrans()`](https://docs.python.org/3/library/stdtypes.html#str.maketrans) is also an option). That way you don't need to have another `if` for each letter.
```
</details>

Word Count
----------
<details><summary>Notes</summary>

```text
The [`collections`](https://docs.python.org/3/library/collections.html) library provides some very helpful classes to clean up this particular common pattern. Using one of those would improve this code.
```
</details>
