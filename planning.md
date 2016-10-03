# Planning and ideas

'An Introduction to Solving Biological Problems with Python' training can be divided into 4 sessions over two days.

1. DAY 1. MORNING. SESSION 1.: running the Python interpreter, variables and types, arithmetic, basic data structures
2. DAY 1. AFTERNOON. SESSION 2.: logic & flow control, loops, exceptions, importing libraries
3. DAY 2. MORNING. SESSION 3.: custom functions, variable scope, some biological examples
4. DAY 2. AFTERNOON. SESSION 4.: dealing with files, parsing file formats, introduction to BioPython

## DAY 1. MORNING. SESSION 1.

### Part 1.

INTRO: the python programming language & python interpreter (command line)
Python is free, cross-platform, widely used, well documented & well supported.
Python is a simple interpreted language, with no separate compilation step.

- Getting started
- Printing values
- Using variables: they are names for values, created by use. No declaration necessary.
A variable is just a name, it does not have a type. Values are garbage collected,
if nothing refers to data any longer, it can be recycled. Must assign value to variable
before using it. Python does not assume default values for variables,
doing so can mask many errors.
- Simple data types: Values do have types. Use functions to convert between types.
    - booleans
    - integers
    - floating point numbers
    - complex numbers
    - strings are sequences of characters
    - the None object
- Arithmetic: addition, subtraction, multiplication, division, exponentiation, remainder
- Saving code in files
    - Comments

#### EXERCISES

```
* create a variable, print out a message
* addition operator
* calculate the mean of two variables
* [1.1] Print DNA sequence from amino acid one.
```

### Part 2.

As well as the basic data types we introduced, python has several ways of storing
a collection of values. We are going to see four of them: tuples, lists, sets and
dictionaries.

- Collections: complex data types
    - tuples: A tuple is a sequence of immutable Python objects. Tuples are sequences,
    just like lists. The only difference is that tuples can't be changed i.e.,
    tuples are immutable and tuples use parentheses and lists use square brackets.
    - lists: the most popular [value, value, value, ...] it is mutable, it can be
    changed after been created. It is heterogeneous, it can store values of many kinds.
    Appending values to a list lengthens it, deleting values shortens it. Most
    operations on lists are methods. Two that are often used incorrectly sort() and reverse()
    - manipulating tuples and lists

Online Python doc: https://docs.python.org/2/  Library | 5.6. Sequence Types | Mutable Sequence Types (5.6.4)

#### EXERCISES

```
* [1.2] Print DNA sequence from a list of DNA codons
```

- String manipulations and format: strings are indexed exactly like lists.
Strings are immutable, they cannot be changed in place. Use + to concatenate strings.
Concatenation always produces a new string. Use string % to format output.
Use triple quotes for multi-line strings. Strings have methods: capitalize()
upper() lower() count() find() replace()

Online Python doc: https://docs.python.org/2/ Library | 5.6. Sequence Types | 5.6.1. String Methods

Online Python doc: https://docs.python.org/2/ Library | 5.6. Sequence Types | 5.6.2. String Formatting Operations

#### EXERCISES

```
* [1.3] String manipulation using your name
```

- Sets contain unique unordered elements. They are very similar to lists but
because the elements are not in order they do not have an index.

Online Python doc: https://docs.python.org/2/ Library | 5.7. Set Types

#### EXERCISES

```
* [1.4] Find the unique amino acid codes in a protein sequence
```

- Dictionaries contain a mapping of keys to values

Online Python doc: https://docs.python.org/2/ Library | 5.8. Mapping Types

```
Dictionary can be very useful when combined with string formatting e.g.
format_string = "Dear %(name)s, we have sequenced %(num)d libraries. The yield is %(yield)dM reads."
print format_string % {'name': 'Anne', 'num':3, 'yield': 182}
```

#### EXERCISES

```
* [1.5] Use a dictionary to map between codon sequences and amino acids they
encode to print out the name of the amino acids of a DNA sequence
```


```
>>> TAKE HOME MESSAGE
>>> Variables are labels that refer to data.
>>> Many variables may refer to the same piece of data.
>>> Use strings to store text.
>>> Use lists to store many related values in order.
>>> User sets to store unique related values in order.
>>> Use dictionaries to store key/value pairs.
```

## DAY 1. AFTERNOON. SESSION 2.

### Part 1.

INTRO: program control and logic - code blocks: if/loops/exceptions.
Real power of programs comes from repetition and selection. Why indentation?
Because it makes the code you write clearer and easier to read.
Python style guide (PEP 8) recommends 4 spaces.
Loops let us do things many times. Collections let us store many values together.

- code blocks
- conditional execution
    - the if statement: use if/elif/else to make choices
    - comparisons and truth

#### EXERCISES

```
[2.0] Compare your age with other persons and print if you are younger/older/same age
[2.?] Check if a DNA sequence contain a stop codon
```

- loops
    - the for loop: a for loop is used to access each value in turn
    - the while loop: a while loop is used to step through all possible indices
    - skipping and breaking loops
    - looping gotchas

#### EXERCISES

```
[2.1] Loop over a list of bases using for and while loops
```

- more looping
    - using enumerate
    - using zip
    - filtering in loops

#### EXERCISES

```
[2.2] Calculate the GC content of a DNA sequence
```

### Part 2 (after break)

Python provides two very important features to handle any unexpected error in your
Python programs and to add debugging capabilities in them: exceptions and assertions.

- exceptions: An exception is an event, which occurs during the execution of a program,
that disrupts the normal flow of the program's instructions. In general, when a Python
script encounters a situation that it can't cope with, it raises an exception.
An exception is a Python object that represents an error.

#### EXERCISES

```
[2.3] Raise an exception if the DNA sequence is not valid
```

- importing modules and libraries
    - help(math)
    - import sys
    - print sys.version & sys.platform
    - print sys.path which defines the list of directories Python searches in to find modules.
    sys.argv: The most commonly-used element of sys is probably sys.argv, which holds the command-line arguments of the currently-executing program.

```
>>> TAKE HOME MESSAGE
>>> Use while to repeat something until something changes.
>>> Use for to do something once for each part of a larger whole.
>>> Use if and else to make choices.
```

## DAY 2. MORNING. SESSION 3.

### Part 1.

INTRO: function basics and definition
A programming language should not include everything anyone might ever want
Instead, it should make it easy for people to create what they need
to solve specific problems by defining functions to create higher-level operations.
In python it is done using the keyword 'def'.

- function definition syntax

#### EXERCISES

```
[3.1a] Create a function that calculate the means of two number and then from a list of number
[3.1b] Create a function to calculate the molecular weight of a DNA sequence
```

- function arguments

#### EXERCISES

```
[3.2] Extend the previous function to also calculate the weight of a RNA sequence
```

- return value

#### EXERCISES

```
[3.3] Write a function that counts the number of each base found in a DNA sequence
```

### Part 2.

- variable scope: globals vs within blocks
- advanced topics: anonymous functions (lambda); functions as values; nested functions

#### EXERCISES

```
BIO examples
- program ribosome that translates RNA into protein
  - extra points for also taking DNA (T -> U)
  - extra points for all reading frames.

- calculate GC content of DNA not on whole sequence but with sliding window.

- calculate hydrophobicity with sliding window.
```

```
>>> TAKE HOME MESSAGE
>>> Define functions to break programs down into manageable pieces.
>>> Remember that a function is really just another kind of data.
```

# Day 2. AFTERNOON. SESSION 4.

### Part 1.

INTRO: In this session we cover 2 widely used ways of reading data into our
programs, via the command line and by reading files from disk.

- reading command line arguments

#### EXERCISES

```
[4.1a] Write a script that takes 2 integers from the command line using the sys.argv
library, add the two numbers and printout the result
[4.1b] Write a script tha takes a DNA sequence from the command line and prints out
its length and GC content
```

  - the argparse library

#### EXERCISES

```
[4.1c] Use the argparse library to do the same exercise as above
```

### Part 2.

- file objects
    - mode modifiers
    - error checking
- closing files
- reading from files
    - the with statement
- writing to files

#### EXERCISES

```
[4.2a] Write a script that writes a list of number to a file, with each number
on a separate line
[4.2b] Open a file and for each line print out the line number and its length
```

- data formats
- delimited files
    - reading delimited files
    - writing delimited files
- more advanced examples
    - read csv file
    - write csv file

#### EXERCISES

```
[4.3a] Read a tab separated file
[4.3b] Write a csv file
```

- fixed format files (PDB)
- XML files
- python file libraries: os & os.path
- more advanced examples
    - recursive file search
    - recursive delete

- system calls

#### EXERCISES

```
[4.4] Write a script that execute the command 'ls' to get the list of files
then modify your script to only print python files
```

### Part 3.

- using BioPython

Biopython is to make it as easy as possible to use Python for bioinformatics by
creating high-quality, reusable modules and classes. Biopython features include
parsers for various Bioinformatics file formats (BLAST, Clustalw, FASTA, Genbank,...),
access to online services (NCBI, Expasy,...), interfaces to common and not-so-common programs
(Clustalw, DSSP, MSMS...), a standard sequence class, various clustering modules,
a KD tree data structure etc. and even documentation.

Basically, we just like to program in Python and want to make it as easy as possible
to use Python for bioinformatics by creating high-quality, reusable modules and scripts.

Biopython tutorial http://biopython.org | Tutorial | 1.2  What can I find in the Biopython package

#### BioPython EXAMPLES

- more advanced examples
    - writing FASTA files
    - reading FASTA files

```
>>> TAKE HOME MESSAGE
>>> Happy Python programming!
```

IDEAS: if you need help: http://stackoverflow.com/

IDEAS: Pylint is a tool that checks for errors in python code, tries to enforce a coding standard and looks for bad code smells: http://www.pylint.org/

IDEAS: Any code that hasn't been tested is probably wrong: Python unit testing framework unittest

IDEAS: from http://software-carpentry.org/v4/python
