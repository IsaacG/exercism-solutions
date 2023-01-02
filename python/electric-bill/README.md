# Electric Bill

Welcome to Electric Bill on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.
If you get stuck on the exercise, check out `HINTS.md`, but try and solve it without using those first :)

## Introduction

Python has three different types of built-in numbers: integers ([`int`][int]), floating-point ([`float`][float]), and complex ([`complex`][complex]).
Fractions ([`fractions.Fraction`][fractions]) and Decimals ([`decimal.Decimal`][decimals]) are also available via import from the standard library.

Whole numbers including hexadecimal ([_`hex()`_][hex]), octal ([_`oct()`_][oct]) and binary ([_`bin()`_][bin]) numbers **without** decimal places are also identified as `ints`:

```python
# Ints are whole numbers.
>>> 1234
1234
>>> type(1234)
<class 'int'>

>>> -12
-12
```

Numbers containing a decimal point (with or without fractional parts) are identified as `floats`:

```python
>>> 3.45
3.45
>>> type(3.45)
<class 'float'>
```

## Arithmetic

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//`, and `%`).

### Addition and subtraction

Addition and subtraction operators behave as they do in normal math.
If one or more of the operands is a `float`, the remaining `int`s will be converted to `float`s as well:

```python
>>> 5 - 3
2
# The int is widened to a float here, and a float is returned.
>>> 3 + 4.0
7.0
```

### Multiplication

As with addition and subtraction, multiplication will convert narrower numbers to match their less narrow counterparts:

```python
>>> 3 * 2
6

>>> 3 * 2.0
6.0
```

### Division

Division always returns a `float`, even if the result is a whole number:

```python
>>> 6/5
1.2

>>> 6/2
3.0
```

### Floor division

If an `int` result is needed, you can use floor division to truncate the result.
Floor division is performed using the `//` operator:

```python
>>> 6//5
1

>>> 6//2
3
```

### Modulo

The modulo operator (`%`) returns the remainder of the division of the two operands:

```python
# The result of % is zero here, because dividing 8 by 2 leaves no remainder
>>> 8 % 2
0

# The result of % is 2 here, because 3 only goes into 5 once, with 2 leftover
>>> 5 % 3
2
```

Another way to look at 5 % 3:

```python
>>> whole_part = int(5/3)
1

>>> decimal_part = 5/3 - whole_part
0.6666666666666667

>>> whole_remainder = decimal_part * 3
2.0
```

## Round

Python provides a built-in function [`round(number, <decimal_places>)`][round] to round off a floating point number to a given number of decimal places.
If no number of decimal places is specified, the number is rounded off to the nearest integer and will return an `int`:

```python
>>> round(3.1415926535, 2)
3.14

>>> round(3.1415926535)
3
```

## Priority and parentheses

Python allows you to use parentheses to group expressions.
This is useful when you want to override the default order of operations.

```python
>>> 2 + 3 * 4
14

>>> (2 + 3) * 4
20
```

Python follows the [PEMDAS][pemdas] rule for operator precedence.
This means calculations within `()` have the highest priority, followed by `**`, then `*`, `/`, `//`, `%`, `+`, and `-`:

```python
>>> 2 + 3 - 4 * 4
-11

>>> (2 + 3 - 4) * 4
4

# In the following example, the `**` operator has the highest priority, then `*`, then `+`
# Meaning we first do 4 ** 4, then 3 * 64, then 2 + 192
>>> 2 + 3 * 4 ** 4
770
```

## Precision & Representation

Integers in Python have [arbitrary precision][arbitrary-precision] -- the amount of digits is limited only by the available memory of the host system.

Floating point numbers are usually implemented using a `double` in C (_15 decimal places of precision_), but will vary in representation based on the host system.
Complex numbers have a `real` and an `imaginary` part, both of which are represented by floating point numbers.

For a more detailed discussions of the issues and limitations of floating point arithmetic across programming languages, take a look at [0.30000000000000004.com][0.30000000000000004.com] and [The Python Tutorial][floating point math].

[0.30000000000000004.com]: https://0.30000000000000004.com/
[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
[bin]: https://docs.python.org/3/library/functions.html#bin
[complex]: https://docs.python.org/3/library/functions.html#complex
[decimals]: https://docs.python.org/3/library/decimal.html#module-decimal
[float]: https://docs.python.org/3/library/functions.html#float
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
[fractions]: https://docs.python.org/3/library/fractions.html
[hex]: https://docs.python.org/3/library/functions.html#hex
[int]: https://docs.python.org/3/library/functions.html#int
[oct]: https://docs.python.org/3/library/functions.html#oct
[pemdas]: https://mathworld.wolfram.com/PEMDAS.html
[round]: https://docs.python.org/3/library/functions.html#round

## Instructions

The company you work for wants to reduce their carbon footprint, so they want you to write a program to calculate the power usage and cost of running their electronics.

## 1. Get extra hours

Your employer has a program that calculates the time it takes to run different electronics.
Currently, the time is stored in hours.
When your employer added the hours, they noticed that the time duration was not correct.
They want you to add 3 extra hours to the time data.
They would also like to know how many "extra" hours there are after converting the data to "full" days (a day is 24 hours).
The time to convert may not be in full days.

Implement a function `get_extra_hours()` that accepts an integer which holds the number of hours.
The function should make the appropriate "extra hours" adjustment, and then `return` an integer representing how many hours needs to be removed from the total to get the time in "full" days.

```python
>>> get_extra_hours(25)
4
```

## 2. Get kW value

Your employer wants to know the power usage of the different electronics in kW.
kW stands for kilowatt, where watts are a unit of power.
Kilo in the unit name is a prefix in the metric system meaning 1000.
One kilowatt == 1000 watts.

Implement a function `get_kW_value()` that accepts an integer which holds the number of watts.
The function should then `return` the watts as kilowatts rounded to 1 decimal place.

```python
>>> get_kW_value(1150)
1.2
```

## 3. Get kWh value

To be able to calculate the cost of running the electronics, your employer needs to know the power usage in kWh.
kWh stands for kilowatt-hour, where hour is a unit of time.
One kilowatt-hour == 1000 watts used for 1 hour.
An hour is made up of 60 minutes and a minute is made up of 60 seconds.
One hour is equal to 3600 seconds.
To calculate the kWh value, you must convert watts to kW, and then floor-divide the result by 3600.

Implement a function `get_kWh_value()` that accepts an integer which holds the number of watts.
The function should then `return` the kilowatt-hours as an integer.

```python
>>> get_kWh_value(5000000)
1
```

## 4. Get efficiency

Electronics are not 100% efficient.
Therefore, your employer wants you to calculate the _efficiency_ of the electronics.
To get efficiency, you must divide the power factor (_a float between 0 and 100_) by 100.

Implement a function `get_efficiency()` that accepts a float that holds the power factor.
The function should then `return` the calculated efficiency as a float.

```python
>>> get_efficiency(80)
0.8
```

## 5. Get cost

Your employer wants to know the cost of running the electronics.
The cost of running the electronics is the power used multiplied by the cost per kWh.
The power used is the power given divided by the calculated efficiency.

Implement a function `get_cost(<watts>,<power_factor>,<price>)` that accepts an integer that holds the number of watts, a float that has the power factor, and a float that holds the cost per kWh.
The function should then `return` the cost of running the electronics as a float.

```python
>>> get_cost(5000000, 80, 0.25)
0.3125
```

## Source

### Created by

- @meatball133
- @BethanyG

### Contributed to by

- @MatthijsBlom