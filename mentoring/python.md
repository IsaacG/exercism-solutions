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
Hi! I'm excited to be your mentor for this code review. Reviewing code and providing feedback takes a lot of time and energy but I usually find it very rewarding when I get to work with someone to help them improve their solution! Code reviews are an iterative process. The reviewer looks over the code provides feedback/recommendations and the code author (that's you) responds, asking follow up questions, getting clarification and/or ***updating the code*** by submitting a new iteration. Then the process starts over and repeats until everyone is happy with the final, collaboratively developed result. I'm looking forward to working with you on this!

I am looking forward to seeing your next iteration of this solution and working with you to continue improving your code, one iteration at a time! (Hint, hint: please update your code and submit a new iteration.)

Don't worry about your response time and how long it takes you to update your solution. I mentor enough that I have multiple solutions in my inbox most days and it doesn't matter to me if your solution pops up in my inbox tomorrow or next week.

Using a data type as part of the variable name is typically considered an anti-pattern. Prefer describing what the variable represents or is used for.
That data dict is a good candidate for a module-level constant. There is not need to have it recreated every time the function is called.
This code uses both double quotes and single quotes. Either is fine, but avoid mixing and matching! Consistent code is good code.
Single character variable names are usually not recommended, especially for any scope larger than one or two lines.
`[f(a) for a in b]` iterates through `b` to create a list. You are then iterating over this list to compute a return value. You can avoid that extra middle step of building and storing a list by passing a generator to the function instead and having the function process the elements of that iterator directly! You can do this by doing `func(f(a) for a in b)`.
In languages where strings are immutable (like Python and Go), string concatenations are relatively expensive and should generally not be done in loops. Instead, string building techniques should be used, like collecting string pieces in a list then making use of `str.join()`.
The [Google Style Guide](https://google.github.io/styleguide/pyguide.html#214-truefalse-evaluations) recommends "Use the “implicit” false if at all possible".
The [Google Style Guide](https://google.github.io/styleguide/pyguide.html#22-imports) recommends "Use `import` statements for packages and modules only, not for individual types, classes, or functions.".

[PEP-257](https://peps.python.org/pep-0257/) says, "There’s no blank line either before or after the docstring."
[PEP-257](https://peps.python.org/pep-0257/) says docstrings should begin with a single line summary which should be a complete sentence, ending in a period.
[PEP-257](https://peps.python.org/pep-0257/) says docstrings which are multiple lines should start with a one line summary. The summary should be followed by a blank line then the rest of the docstring.
Docstrings should be imperative ("Do something ..." or "Return ...") vs descriptive ("Does sometime ..." or "Returns ...").
Commas (`,`) should be followed by a space, just like in this sentence!
Operators like `=` should be space padded.
Function definitions should be separated from other expressions by exactly two blank lines.

Please note, the mentoring sessions that people find the most valuable typically involve multiple rounds of comments and code improvements. This allows you to make improvements to your code, get additional feedback and adjust the code until it is really good. The initial round of comments is usually just the tip of the iceberg when it comes to what you can learn from a code review! (Plus, mentors can get burned out if they take the time to leave helpful comments and don't see any interaction with that feedback; it often makes them feel like the student isn't actually interested in improving the code or what they have to share.)

Can you [reduce nesting](https://github.com/uber-go/guide/blob/master/style.md#reduce-nesting)?
Can you avoid [magic strings](https://en.wikipedia.org/wiki/Magic_string) in your code?
Can you avoid [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)) in your code?
Can you [avoid repeating yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (DRY)?
This code contains [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)). Can you use a module constant, similar to `EXPECTED_BAKE_TIME`, to avoid magic numbers in your code?

In boolean logic (and Python), `var == True` is the same as `var` and `var == False` can be written `not var`.
The following is a common anti-pattern:

``python
# Avoid this pattern.
if condition:
    return True
return False

# That should be replaces with this.
return condition
``

Regular variables are usually named using `snake_case` and module constants use `ALL_CAPS`.
There's no need to comment just to say you submitted a new iteration; Exercism notifies mentors of new iterations.
For type annotation, the `list` should be `list[int]` (for Py 3.9+) or `from typing import List; List[int]`
Submitting the test file is not necessary ... and makes reviewing your solution more difficult.
`Exception` is a base exception class and is very generic. It conveys the least amount of information of (almost) all the exceptions. Avoid using this directly and always prefer [a more specific exception](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
Exception messages should start with an uppercase letter and end with a period (just like docstrings). When possible, prove as much detail as possible in the message so the user can figure out what went wrong (like, the bad value or the type of the data). That makes acting on the error much easier.
Type checking is best done with the builtin `isinstance()` method.
In Python, the `is` operator checks if two objects are the *same object* while `==` checks if two objects have the same *value*. `[1, 2] == [1, 2] -> True` but `[1, 2] is [1, 2] -> False`. You generally want to use `==` and only want `is` in very specific conditions.

[Guard clauses](https://en.wikipedia.org/wiki/Guard_(computer_science)) are used to check for conditions and prevent code from running if the conditons are not met. This allows you to handle boundary conditions once and then have the rest of the code [not nested or wrapped](https://github.com/uber-go/guide/blob/master/style.md#reduce-nesting) or have to worry about those conditions.
Can you use the [built-in `()` function](https://docs.python.org/3/library/functions.html) here?
The [built-in `any()` and `all()` functions](https://docs.python.org/3/library/functions.html) are useful for this pattern.
[Python's built-in types](https://docs.python.org/3/library/stdtypes.html)
[Built-in string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
[Avoid using mutable values for argument default values!](https://docs.python-guide.org/writing/gotchas/)

Disclaimer: I have tons of experience coding and mentoring but I am a bit rusty when it comes to Go. I'm jumping in here to help with Go mentoring as the mentoring request queue is getting rather long.
```

### Extra Credit

```text
If you want to go the extra step, type annotation is worth adding to your code! See [PEP-483](https://peps.python.org/pep-0483/) or [Real Python](https://realpython.com/python-type-checking/) for more information.
Docstrings aren't required here but they are nice to have - both for the module and functions.
```

### Data types

```text
`[1, 2, 3]` is a list. `(1, 2, 3)` is a tuple. `{1, 2, 3}` is a set.

Sets are not ordered and cannot contain duplicate values. If you don't care about the order and don't want duplicate entries, use a set.

Tuples are usually used when there is a very specific number of elements and the order is meaningful. For example, when storing a 2D coordinate (two values, the first is the X and the second is the Y) or a RGB color (three values, red, green, blue). Tuples may have mixed data types, eg a person's name and age (str and int eg `("Bob", 25)`). Tuples are immutable so you can't append to them; the number of items is fixed.

Lists are used when the number of elements doesn't have special meaning (though the order might matter, ie sorted data). The elements should all be similar data types.
```

### Long Queue

```text
Hello! I have tons of experience coding and mentoring but I am a bit rusty when it comes to Go. I'm jumping in here to help with Go mentoring as the mentoring request queue is getting rather long.

Since this request is more than a month old, I would first like to make sure you still want to have mentoring. If that's the case, great! I'll try to help as best as I can. If, on the other hand, mentoring is no longer desired, you can free up your mentoring slot by closing this discussion.

I am sorry that it took so long to get an answer to your request. Some languages have fewer active mentors.
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
Take a look at the following sentence. Can you tell -- without using a computer or paper/pen, if it is a pangram? "When zombies arrive, quickly call Judge Pat." Most people can tell if that is a pangram without needing to do any counting. Can you tell without counting? Can your program avoid counting?
[`string.ascii_lowercase`](https://docs.python.org/3/library/string.html#string.ascii_lowercase) might be useful here.
Suppose the input sentence is 100,000 characters long. Is it necessary to loop through each character to solve this?
Do you need to call `lower()` once for every character in the `sentence`? Function calls are cheap but not free.
Is it always necessary to loop through every letter to determine whether a sentence is a pangram?
Python has an [`any()`](https://docs.python.org/3/library/functions.html#all) and [`all()`](https://docs.python.org/3/library/functions.html#all) that might be helpful here.
Rather than calling `.lower()` a whole lot of times inside the loop, can you call it just once?
Given a sentence, can you, yourself without a program, determine if it is a pangram? Consider this sentence; can you determine if it is a pangram -- and pay attention to how you do it! `"The five smart wizards jump quickly."`. Actually check that sentence before reading on! Now ... most people figure out if a sentence is a pangram without doing any counting. If you solved it without counting, can your program do the same thing?
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
