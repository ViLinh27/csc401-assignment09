

##### final exam #####
'''
Final Exam:

OnLine students - make sure you regiser ASAP

InClass students - Usual classroom 5:45-9pm, Thursday 3/21/2019

You are allowed 2 double sided or 4 single sided
pages of notes.

Cumulative, covers Chapters 2-8

Same format as midterm but HARDER and LONGER:

Part 1) multiple choice - Make sure you review the textbook,
notes and quizzes.  Please note that there may be similar
problems on the final.  Read them carefully, they are
probably different.   It is more important that you know
the concepts rather than the answers.

Part 2) - you cannot get enough programming practice.
Work problems from the book.  Rework old programming problems
from class and hw.   You might also consider
working a problem a different way, for example
do a hw problem using composition rather than
inheritance or vice-versa.

A few study problems with solutions are below.  These
are not intended to be a comprehensive review,  just
examples of things I could ask.
'''

##### study problems #####


##### Temp #####


'''
Write a class that stores 'F' and 'C' temperatures
and allows conversion between them.

want this to work:
>>> t = Temp(32,'F')
>>> t
Temp(32,'F')
>>> t.convert()
>>> t
Temp(0,'C')
>>> Temp()
Temp(0,'C')
'''

class Temp:

    def __init__(self,degrees=0,units='C'):
        self.degrees = degrees
        self.units = units

    def __repr__(self):
        return "Temp({},'{}')".format( self.degrees, self.units )

    def convert(self):

        if self.units=='C': # C to F
            self.degrees = int(self.degrees*9/5+32)
            self.units = 'F'
        else: # F to C
            self.degrees = int((self.degrees-32)*5/9)
            self.units = 'C'
            



##### lineNumbers #####
            
'''
Write a function lineNumber that accepts two arguments
1) a multi-line text str, and
2) a str containing search words.

The function must return the index of the first
line of text that contains all the search words
(in any order).  If no line contains all the the
words, the function must return -1.

Note also these additional requirements:
1) any periods in the text should be ignored
2) matches should be case-insensitive
3) matches must be whole word matches,
   e.g, 'simp' does not match 'simple'

>>> print(text)
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

>>> lineNumber( text, 'better than')
0
>>> lineNumber( text, 'Worse' )
-1
>>> lineNumber( text, 'than better simple') # order doesnt matter
2
>>> lineNumber( text, 'complicate') # not whole word
-1
>>> lineNumber( text, 'implicit BETTER explicit') # case insensitive
1
>>> 
'''


text = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.'''


def lineNumber( text, words ):

    words = words.lower().split()
    # split text into lines
    lines = text.lower().replace(".","").split('\n')

    # index over lines
    for i in range(len(lines)):
        # count search terms found
        found = 0
        for word in words:
            # split so that matching is on whole words
            if word in lines[i].split():  #
                found+=1
        # if all found, return line #
        if found==len(words):
            return i
  
    # if not found, return -1
    return -1
    


 
##### Counter #####

'''
Write a Counter class that inherits from dict (you MUST
inherit).   The Counter class allows you to count
objects:

>>> c = Counter()
>>> c.count( 1 )
>>> c.count( 1 )
>>> c.count( 3 )
>>> c.count( 5 )
>>> c
Counter({1: 2, 3: 1, 5: 1})

Individual counts can be retrieved by indexing
into the Counter object.  If an item has not
been counted then a count of 0 is returned (rather
than an error).  This means that you must write the
__getitem__ method

>>> c[1]
2
>>> c[5]
1
>>> c[99]
0

There is also a countItems method that can count
multiple items:

>>> c = Counter()
>>> c.countItems( [1,2,3,2,3,3] )
>>> c
Counter({1: 1, 2: 2, 3: 3})

and a method that prints out all the positive counts.
Note that it will print the keys in sorted order.  This
is easily accomplished: instead of iterating over
a dict d, one can iterate over sorted(d):

>>> c.printCounts()
1 1
2 2
3 3

more thorough tests:

>>> from random import *
>>> seed(0)
>>> c = Counter()
>>> c.countItems( [randrange(5) for i in range(5)])
>>> c
Counter({3: 2, 0: 1, 2: 1, 4: 1})
>>> c.printCounts()
0 1
2 1
3 2
4 1
>>> c.countItems( [randrange(5) for i in range(500)])
>>> c.printCounts()
0 115
1 93
2 99 
3 97
4 101
>>> 
'''
    
        


class Counter(dict):

    def count( self,item):
        if item in self:
            self[item]+=1
        else:
            self[item]=1

    def __repr__(self):
        return "Counter({})".format( dict.__repr__(self))

    def __getitem__(self,key):
        if key in self:
            return dict.__getitem__(self,key)
        else:
            return 0

    def countItems( self, iterable ):
        for item in iterable:
            self.count( item)

    def printCounts( self ):
        for key in sorted(self):
            print( key, self[key] )
    



##### diceGame #####

'''
Write a functinon that simulates the following
dice game: a pair of dice is rolled repeatedly
until the roll showing is the same as one of
the previous 5 rolls.  (Two rolls are the same
if the number of pips on the two dice are the same.  I.e.,
the roll (1,6) is the same as (1,6) and the same as (6,1)
but not the same as (2,5).)   The function then returns
the number of the rolls made match the TOTAL of the
final roll.

For example, suppose that the following rolls are
made: (1,6), (2,3), (1,1), (4,1), (2,2), (6,6), (3,2)
The game then stops because the last roll (3,2) is the
same as the one of the rolls in the 5 previous (2,3).
The functiuon returns 3 which is the number of rolls
whose total is, 5 = 2+3, the total on the final roll.


>>> import random
>>> random.seed(8)
>>> random.seed(0)
>>> diceGame()
2
>>> random.seed(8)
>>> diceGame()
3
>>> random.seed(451)
>>> diceGame()
5
>>> random.seed(33079)
>>> diceGame()
11
>>> 
'''

'''
note that one could also write two loops one after
the other.  the first simulates and stores rolls
and the other counts the rolls whose total is the
same as the final total

using a set to store rolls make sure that the
dice order doesn't matter, e.g., {1,6}=={6,1}
is True.   could also store (min(d1,d2),max(d1,d2))

'''

def diceGame():

    rolls = []
    totals = []

    while True:

        d1 = random.randrange(1,7)
        d2 = random.randrange(1,7)
        # print( d1,d2 )
        totals.append( d1+d2 )
        if {d1,d2} in rolls[-5:]: # not using set, {1,6}=={6,1}
            return totals.count( d1+d2 )
        else:
            rolls.append( {d1,d2} )

  
        


















