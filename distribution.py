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
answer.sort(reverse=True)

for i in range(0, len(answer)):
    tuple = answer[i]
    line = ""
    for j in range(0, tuple[0]):
        line = line + tuple[1]
    print(line)



