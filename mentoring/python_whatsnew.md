# Selection of updates which sound interesting to me. Removing type-related.

* 3.11
  - PEP 654: Exception Groups and except*
* 3.10
  - **PEP 636, Structural Pattern Matching (`match case`)**
  - PEP 617, Parenthesized context managers are now officially allowed.
  - **PEP 618, Add Optional Length-Checking To zip.**
* 3.9
  - **PEP 584, union operators added to dict;**
  - **PEP 616, string methods to remove prefixes and suffixes.**
  - PEP 615, the IANA Time Zone Database is now present in the standard library in the zoneinfo module;
  - an implementation of a topological sort of a graph is now provided in the new graphlib module.
* 3.8
  - **PEP-572 Assignment expressions, `:=`**
  - **PEP-570 Positional-only parameters**
  - **f-strings support = for self-documenting expressions and debugging**
* 3.7
  - **dataclasses: PEP 557 – Data Classes**
  - **the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.**
* 3.6
  - **PEP 498, formatted string literals.**
  - **PEP 515, underscores in numeric literals.**
  - secrets: PEP 506 – Adding A Secrets Module To The Standard Library.
* 3.5
  - PEP 448, additional unpacking generalizations.

# Python Updates Summary

## 3.11

### New syntax features:

* PEP 654: Exception Groups and except*

### New built-in features:

* PEP 678: Exceptions can be enriched with notes

### New standard library modules:

* PEP 680: tomllib — Support for parsing TOML in the Standard Library

### Interpreter improvements:

* PEP 657: Fine-grained error locations in tracebacks
* New -P command line option and PYTHONSAFEPATH environment variable to disable automatically prepending potentially unsafe paths to sys.path

### New typing features:

* PEP 646: Variadic generics
* PEP 655: Marking individual TypedDict items as required or not-required
* PEP 673: Self type
* PEP 675: Arbitrary literal string type
* PEP 681: Data class transforms

### Important deprecations, removals and restrictions:

* PEP 594: Many legacy standard library modules have been deprecated and will be removed in Python 3.13
* PEP 624: Py_UNICODE encoder APIs have been removed
* PEP 670: Macros converted to static inline functions

## 3.10

### New syntax features:

* PEP 634, Structural Pattern Matching: Specification
* PEP 635, Structural Pattern Matching: Motivation and Rationale
* PEP 636, Structural Pattern Matching: Tutorial
* bpo-12782, Parenthesized context managers are now officially allowed.

### New features in the standard library:

* PEP 618, Add Optional Length-Checking To zip.

### Interpreter improvements:

* PEP 626, Precise line numbers for debugging and other tools.

### New typing features:

* PEP 604, Allow writing union types as X | Y
* PEP 612, Parameter Specification Variables
* PEP 613, Explicit Type Aliases
* PEP 647, User-Defined Type Guards

### Important deprecations, removals or restrictions:

* PEP 644, Require OpenSSL 1.1.1 or newer
* PEP 632, Deprecate distutils module.
* PEP 623, Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.
* PEP 624, Remove Py_UNICODE encoder APIs
* PEP 597, Add optional EncodingWarning

## 3.9

### New syntax features:

* PEP 584, union operators added to dict;
* PEP 585, type hinting generics in standard collections;
* PEP 614, relaxed grammar restrictions on decorators.

### New built-in features:

* PEP 616, string methods to remove prefixes and suffixes.

### New features in the standard library:

* PEP 593, flexible function and variable annotations;
* os.pidfd_open() added that allows process management without races and signals.

### Interpreter improvements:

* PEP 573, fast access to module state from methods of C extension types;
* PEP 617, CPython now uses a new parser based on PEG;
* a number of Python builtins (range, tuple, set, frozenset, list, dict) are now sped up using PEP 590 vectorcall;
* garbage collection does not block on resurrected objects;
* a number of Python modules (_abc, audioop, _bz2, _codecs, _contextvars, _crypt, _functools, _json, _locale, math, operator, resource, time, _weakref) now use multiphase initialization as defined by PEP 489;
* a number of standard library modules (audioop, ast, grp, _hashlib, pwd, _posixsubprocess, random, select, struct, termios, zlib) are now using the stable ABI defined by PEP 384.

### New library modules:

* PEP 615, the IANA Time Zone Database is now present in the standard library in the zoneinfo module;
* an implementation of a topological sort of a graph is now provided in the new graphlib module.

### Release process changes:

* PEP 602, CPython adopts an annual release cycle.

## 3.8

* PEP-572 Assignment expressions, `:=`
* PEP-570 Positional-only parameters
* Parallel filesystem cache for compiled bytecode files
* Debug build uses the same ABI as release build
* f-strings support = for self-documenting expressions and debugging
* PEP 578: Python Runtime Audit Hooks
* PEP 587: Python Initialization Configuration¶
* PEP 590: Vectorcall: a fast calling protocol for CPython
* Pickle protocol 5 with out-of-band data buffers

## 3.7

### New syntax features:

* PEP 563, postponed evaluation of type annotations.

### Backwards incompatible syntax changes:

* async and await are now reserved keywords.

### New library modules:

* contextvars: PEP 567 – Context Variables
* dataclasses: PEP 557 – Data Classes
* importlib.resources

### New built-in features:

* PEP 553, the new breakpoint() function.

### Python data model improvements:

* PEP 562, customization of access to module attributes.
* PEP 560, core support for typing module and generic types.
* the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.

### Significant improvements in the standard library:

* The asyncio module has received new features, significant usability and performance improvements.
* The time module gained support for functions with nanosecond resolution.

## 3.6


### New syntax features:

* PEP 498, formatted string literals.
* PEP 515, underscores in numeric literals.
* PEP 526, syntax for variable annotations.
* PEP 525, asynchronous generators.
* PEP 530: asynchronous comprehensions.

### New library modules:

* secrets: PEP 506 – Adding A Secrets Module To The Standard Library.

### CPython implementation improvements:

* The dict type has been reimplemented to use a more compact representation based on a proposal by Raymond Hettinger and similar to the PyPy dict implementation. This resulted in dictionaries using 20% to 25% less memory when compared to Python 3.5.
* Customization of class creation has been simplified with the new protocol.
* The class attribute definition order is now preserved.
* The order of elements in **kwargs now corresponds to the order in which keyword arguments were passed to the function.
* DTrace and SystemTap probing support has been added.
* The new PYTHONMALLOC environment variable can now be used to debug the interpreter memory allocation and access errors.

### Significant improvements in the standard library:

* The asyncio module has received new features, significant usability and performance improvements, and a fair amount of bug fixes. Starting with Python 3.6 the asyncio module is no longer provisional and its API is considered stable.
* A new file system path protocol has been implemented to support path-like objects. All standard library functions operating on paths have been updated to work with the new protocol.
* The datetime module has gained support for Local Time Disambiguation.
* The typing module received a number of improvements.
* The tracemalloc module has been significantly reworked and is now used to provide better output for ResourceWarning as well as provide better diagnostics for memory allocation errors. See the PYTHONMALLOC section for more information.

### Security improvements:

* The new secrets module has been added to simplify the generation of cryptographically strong pseudo-random numbers suitable for managing secrets such as account authentication, tokens, and similar.
* On Linux, os.urandom() now blocks until the system urandom entropy pool is initialized to increase the security. See the PEP 524 for the rationale.
* The hashlib and ssl modules now support OpenSSL 1.1.0.
* The default settings and feature set of the ssl module have been improved.
* The hashlib module received support for the BLAKE2, SHA-3 and SHAKE hash algorithms and the scrypt() key derivation function.

## 3.5


### New syntax features:

* PEP 492, coroutines with async and await syntax.
* PEP 465, a new matrix multiplication operator: a @ b.
* PEP 448, additional unpacking generalizations.

### New library modules:

* typing: PEP 484 – Type Hints.
* zipapp: PEP 441 Improving Python ZIP Application Support.

### New built-in features:

* bytes % args, bytearray % args: PEP 461 – Adding % formatting to bytes and bytearray.
* New bytes.hex(), bytearray.hex() and memoryview.hex() methods. (Contributed by Arnon Yaari in bpo-9951.)
* memoryview now supports tuple indexing (including multi-dimensional). (Contributed by Antoine Pitrou in bpo-23632.)
* Generators have a new gi_yieldfrom attribute, which returns the object being iterated by yield from expressions. (Contributed by Benno Leslie and Yury Selivanov in bpo-24450.)
* A new RecursionError exception is now raised when maximum recursion depth is reached. (Contributed by Georg Brandl in bpo-19235.)

### CPython implementation improvements:

* When the LC_TYPE locale is the POSIX locale (C locale), sys.stdin and sys.stdout now use the surrogateescape error handler, instead of the strict error handler. (Contributed by Victor Stinner in bpo-19977.)
* .pyo files are no longer used and have been replaced by a more flexible scheme that includes the optimization level explicitly in .pyc name. (See PEP 488 overview.)
* Builtin and extension modules are now initialized in a multi-phase process, which is similar to how Python modules are loaded. (See PEP 489 overview.)

### Significant improvements in the standard library:

* collections.OrderedDict is now implemented in C, which makes it 4 to 100 times faster.
* The ssl module gained support for Memory BIO, which decouples SSL protocol handling from network IO.
* The new os.scandir() function provides a better and significantly faster way of directory traversal.
* functools.lru_cache() has been mostly reimplemented in C, yielding much better performance.
* The new subprocess.run() function provides a streamlined way to run subprocesses.
* The traceback module has been significantly enhanced for improved performance and developer convenience.

