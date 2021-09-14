# Help

## Running the tests

You can run the included tests by typing `pytest <exercisename>_test.py` on the command line from within the exercise's directory.

You can also tell Python to run the pytest module on the command line from either within the exercise directory or with a path to the exercise directory.
`python -m pytest <exercisename>_test.py` from within the exercise directory.

`python -m pytest /fully/qualified/path/to/<exercisename>/` OR `python -m pytest realtive/path/to/<exercisename>` from a non-exercise directory.

Many IDE's and code editors also have built-in support for using PyTest to run tests.

- [Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [PyCharm Professional & Community Editions](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test)
- [Atom](https://atom.io/packages/atom-python-test)
- [Spyder](https://www.spyder-ide.org/blog/introducing-unittest-plugin/)
- [Sublime](https://github.com/kaste/PyTest)
- [vim-test](https://github.com/vim-test/vim-test)

See the [Python tests page](https://github.com/exercism/python/blob/main/docs/TESTS.md) for more information.

### Common `pytest` options

- `-v` : enable verbose output.
- `-x` : stop running tests on first failure.
- `--ff` : run failures from previous test before running other test cases.

For other options, see `python -m pytest -h`. PyTest documentation can be found [here](https://docs.pytest.org/en/latest/getting-started.html).

## Submitting your solution

You can submit your solution using the `exercism submit tuples.py` command.
This command will upload your solution to the Exercism website and print the solution page's URL.

It's possible to submit an incomplete solution which allows you to:

- See how others have completed the exercise
- Request help from a mentor

## Need to get help?

If you'd like help solving the exercise, check the following pages:

- The [Python track's documentation](https://exercism.org/docs/tracks/python)
- [Exercism's support channel on gitter](https://gitter.im/exercism/support)
- The [Frequently Asked Questions](https://exercism.org/docs/using/faqs)

Should those resources not suffice, you could submit your (incomplete) solution to request mentoring.

Below are some resources for getting help if you run into trouble:

- [The PSF](https://www.python.org) hosts Python downloads, documentation, and community resources.
- [Python Community on Discord](https://pythondiscord.com/) is a very helpful and active community.
- [#python on Libera.chat](https://www.python.org/community/irc/) this is where the cored developers for the language hang out and get work done.
- [Exercism on Gitter](https://gitter.im/exercism/home) join the Python room for Python-related questions or problems.
- [/r/learnpython/](https://www.reddit.com/r/learnpython/) is a subreddit designed for Python learners.
- [Python Community Forums](https://discuss.python.org/)
- [Pythontutor](http://pythontutor.com/) for stepping through small code snippets visually.


Additionally, [StackOverflow](http://stackoverflow.com/questions/tagged/python) is a good spot to search for your problem/question to see if it has been answered already.
 If not - you can always [ask](https://stackoverflow.com/help/how-to-ask) or [answer](https://stackoverflow.com/help/how-to-answer) someone else's question.