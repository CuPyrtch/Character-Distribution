"""
distribution.py
Author: CuPyrtch
Credit: None

Assignment:Character Distribution

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

input1=input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in \"" + input1 + "\" is: ")

sentence = input1.lower()
counts = []
letters = []
for i in range(97, 123):
    count = sentence.count(chr(i))
    if count > 0:
        counts.append(count)
        letters.append(chr(i))
answer = list(zip(counts, letters))





def compare(a, b):
    """
    compare - generic comparison function for testing two tupes.
    return true if a > b
    a > b if the a[0] > b[0]
    of if a[0] == b[0] and a[1] < b[1]
    compare:(5, 'a'),(3, 's') = True
    compare:(3, 's'),(3, 't') = True
    compare:(2, 'p'),(2, 'l') = False
    retval = a>b
    """
    retval = a[0] > b[0] or ((a[0] == b[0]) and (a[1] < b[1]))
    """ print("compare:"+str(a)+","+str(b),"=",retval) """
    return retval


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            """ print(value) """
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

print("sort this:"+str(answer))
bsort(answer, compare)

for i in range(0, len(answer)):
    tuple = answer[i]
    line = ""
    for j in range(0, tuple[0]):
        line = line + tuple[1]
    print(line)