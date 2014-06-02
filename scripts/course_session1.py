# Printing values
print "Hello world from python!"
print 34
print 2 + 3
print "The answer is:", 42
# NB be careful with white space at the beginning of code lines

print "----------"

# using variables
my_first_variable = 3
print my_first_variable

x = 2 + 2
print x

serine = "TCA"
print serine, "codes for serine"
serine = "TCG"
print "as does", serine
# NB in the interpreter you don't need to print everything, but this is not the case in a file

y = 13
y = y + 1
print y
y += 1
print y

print "----------"

# simple data types
# booleans
a = True
b = False

# integers
x = -7
y = 123
print x, y

# floating point numbers
i = 3.14
j = -42.5
print i * j
k = 1.5e3
print k
l = 3e-3
print l
k = 5e12
print k

# complex numbers - imaginary number usually called i but here it is j like in electronic
m = 3+4j
print m
n = 1.2-5.8j
print n

# strings
s = "AAAAATTTTCCCGGG"
serine = 'TCA'
my_string = "Yeah! It's a string with apostrophes"
text = """A string that extends
over multiple lines"""
print text

# The None object - representing something undefined
z = None
print z

print "a is", type(a)
print "x is", type(x)
print "i is", type(i)
print "m is", type(m)
print "s is", type(s)
print "z is", type(z)

# Arithmetic
x = 3
y = 4
print x + y
print x - y
print x * y
print x/float(y)
print x // y
print x % y
print x ** y
print ((x + 1) - y ) * 4

# NB if you divide 2 integers you will only get an integer result.
print 3/4
print float(3)/4

# save code in files ending with extension .py
# executed using 'python my_script.py'

# comments

# EXERCISES 1.1

print "----------"

# Collections

my_tuple = (123, 54, 92)
print 'tuple:', my_tuple

my_list = ['ATC', 'CGT', 'AAA', 'AAA']
print 'list:', my_list

my_set = set([1,1,1,1,2,3])
print 'set:', my_set

my_dict = {'A': 'Adenine', 'C': 'Cytosine', 'G': 'Guanine', 'T': 'Thymine'}
print 'dict:', my_dict

print "----------"

# tuple is a sequence of immutable object. Tuples are sequences just like lists.
empty_tuple = ()
single_element_tuple = ('Ala',) # note the trailing ','
print single_element_tuple
mixed_types_tuple = (2, 3, False, 'Arg', None)
print mixed_types_tuple
t = (2,3,4)
print t
x, y, z = t
print z
# tuple cannot be altered
#t[1]=4
# TypeError: 'tuple' object does not support item assignment

print "----------"

# list the most popular, can be altered once created (mutable).
l = [1, 3, 6, 9, 12]
print l
matrix = [[1, 0], [0, 2]]
print matrix
list_from_tuple = list(t)
print t
print list_from_tuple
tuple_from_list = tuple(l)
print l
print tuple_from_list

print "----------"

# manipulating tuples and lists
# index access NB. the first element is at index 0
print t
print t[1]
print l
print l[2]
print l[-1]
# slices
print l[1:3] # NB. includes positions from 1 up to 3 but not including 3
print l[2:]
print l[:-1]
# checking if a value is in a list
print 123 in l
print 1 in l
print 999 not in l
print 'length:', len(l)
print 'number of 3s:', l.count(3)
l[2] = 33
print l
l.append(101)
print l
l.insert(3, 111)
print l
l.remove(111)
print l
del l[0]
print l
last_element = l.pop()
print last_element
print l
l.extend([34, 35, 36])
print l
print l + [45, 46, 47]
print l
l[1:3] = [9, 9, 9]
print l
l.reverse()
print l
l.sort()
l = [2, 4, 9, 6]
print l
sorted_copy = sorted(l)
print l
print sorted_copy
bases = ['A', 'T', 'G']
print "-".join(bases)

# EXERCISES 1.2

print "----------"

# string manipulation Strings are like tuples of characters
seq = "ATGTCATTT"
print seq[0]
print seq[-2]
print seq[0:6]
print 'ATG' in seq
print 'TGA' in seq
print len(seq)
#seq[3] = 'Z'
# TypeError: 'str' object does not support item assignment
print 'TCA at position:', seq.find('TCA')
print 'The last C is at position:', seq.rfind('C')
print 'Position of the stop codon:', seq.find('TGA')
string_with_white_space = "    Chromosome start here...     "
print len(string_with_white_space)
print string_with_white_space.lstrip()
print len(string_with_white_space)

string_without_space = string_with_white_space.strip()
print string_without_space
print len(string_without_space)
print len(string_with_white_space)

seq = "ATG TCA CCG GGC"
codons = seq.split()
print codons
bases = list(seq)
print bases
print "|".join(codons)

#print "chr" + 1
# TypeError: cannot concatenate 'str' and 'int' objects

# format strings
format_string = "This is a string %s, then a integer %d and a float %f" % ("my_string", 1, 7.7)
print format_string
format_string = "This is a string %s, then a integer %d and a float %.2f" % ("my_string", 1, 7.7)
print format_string

# EXERCISES 1.3

print "----------"

# sets contain unique elements
l = [1, 2, 3, 4, 4, 4, 5]
print l.count(4)
s = set(l)
print s
s.add(6)
print s
s.add(5)
print s
s1 = set([2,4,6,8,10])
s2 = set([4,5,6,7])
print 'Union:', s1 | s2
print 'Intersection:', s1 & s2

# EXERCISES 1.4

print "----------"

# dictionaries contain a mapping of keys to values
dna = {'A': 'Adenine', 'C': 'Cytosine', 'G': 'Guanine', 'T': 'Thymine'}
print dna
print 'A represents', dna['A']
#print 'What about N?', dna['N']
# KeyError: 'N'

print 'T' in dna
print 'Y' not in dna
print len(dna)

dna['Y'] = 'Pyrimidine'
print dna
del dna['Y']
print dna
print dna.keys()
print dna.values()
print dna.items()

# EXERCISES 1.5

