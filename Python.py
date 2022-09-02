#!/home/bionfo-lab-cmp1/miniconda3/bin/python3.9

#Python Excercises


#--------------------------------------------------------MATH FUNCTIONS PYTHON ----------------------------------------------------------------------------------------------------------------#
"""
SCRIPT 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""

number=[]
for no in range(2000, 3201):  #no between 2,000 to 3,200
        if (no%7==0) and (no%5!=0):  #no is divisible by 7 but not 5
                s = str(no)
                number.append(s)   

print(','.join(map(str, number)))

#Output
"""
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199


"""






"""
SCRIPT 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def compute(no):
    if no == 0:
        return 1
    return no * compute(no - 1)

no = int(input("Please type your digit for computation: "))
print(compute(no))

#Output: 7 results to 5040



"""
SCRIPT 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and th>
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
"""


no = int(input("Please input your number: "))
d=dict()
for x in range(1,no+1):
    d[x]=x*x

print(d)


#Output: 
# Please input your number: 6
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}




"""
SCRIPT 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
"""

digits = input("Please input your data here: ")
s = digits.split(",")  #split function generates a list
t = tuple(s)    #tuple function  generates a tuple from a list
print(s)
print(t)

# Output:
# Please input your data here: 50,40,30,20,15,7
# ['50', '40', '30', '20', '15', '7']
# ('50', '40', '30', '20', '15', '7')






"""
SCRIPT 5:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class input_str(object):
    def __init__(self):
        self.s = ""

    def get_str(self):
        self.s = input()
    
    def print_str(self):
        print(self.s.upper())

string = input_str()
string.get_str()
string.print_str()

#Output:
# hello world
# HELLO WORLD





"""
SCRIPT 6:
Create a script which calculates, prints value according to the formulae;
q = square root of [(2 * C * D )/H ] 
C = 50
H = 30
D is a variable whose input should be separated in a comma sequence.

"""

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
        value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))


# Output: Input 30, Output 10



"""
SCRIPT 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
"""

digits = input("Please input as comma-separated digits: ")
dimension = [int(x) for x in digits.split(',')]
rowNum = dimension[0]
colNum = dimension[1]
list = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
        for col in range(colNum):
                list[row][col]= row*col

print(list)

#Output
# Please input as comma-separated digits: 2,3,4
# [[0, 0, 0], [0, 1, 2]]



"""
SCRIPT 8:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

items=[x for x in input().split(',')]
items.sort()
print(','.join(items))

#Output:
# my,hat,at,your,place
# at,hat,my,place,your





"""
SCRIPT 9:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;

for x in lines:
    print(x)

#Output:
"""
hello you
you're amazing
got it?

HELLO YOU
YOU'RE AMAZING
GOT IT?

"""





"""
SCRIPT 10:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumericall>
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

"""


x = input()
words = [word for word in x.split(" ")]
print(" ".join(sorted(list(set(words)))))

#Output:
# once again and again you are you imagine
# again and are imagine once you




"""
SCRIPT 11:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that>
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

value = []
items=[x for x in input().split(',')]
for p in items:
        intp = int(p, 2)
        if not intp%5:
                value.append(p)

print(','.join(value))

#Output:
# 1100,0101,0111,1100

# 0101





"""
SCRIPT 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))




#------------------------------------------------------------KEY POINT: PERFORMING ARITHMETIC CALCULATIONS -------------------------------------------------------------------------------------#


"""
SCRIPT 13:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


string = input("Please input your string here: ")
d={"DIGITS":0, "LETTERS":0}
for c in string:
        if c.isdigit():
                d["DIGITS"]+=1
        elif c.isalpha():
                d["LETTERS"]+=1
        else:
                pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])


#Output:
# Please input your string here: my name is 12356
# LETTERS 8
# DIGITS 5





"""
SCRIPT 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

string = input("Please input your string here: ")
d = {"UPPER CASE":0, "LOWER CASE":0}
for char in string:
        if char.isupper():
                d["UPPER CASE"]+=1
        elif char.islower():
                d["LOWER CASE"]+=1
        else:
                pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])

#Output:
# Please input your string here: tOgOggle
# UPPER CASE 2
# LOWER CASE 6





"""
SCRIPT 15:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

a = input()
b1 = int( "%s" % a )
b2 = int( "%s%s" % (a,a) )
b3 = int( "%s%s%s" % (a,a,a) )
b4 = int( "%s%s%s%s" % (a,a,a,a) )
print(b1+b2+b3+b4)

# Output:
# 11
# 11223344







"""
SCRIPT 16:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))

# Output
# 11,21,31,52,41
# 11,21,31,41






"""
SCRIPT 17:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


bank_acc = 0
while True:
    s = input("Please type in amount: ")
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        bank_acc += amount
    elif operation=="W":
        bank_acc -= amount
    else:
        pass
print(bank_acc)







"""
SCRIPT 18:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be pri>
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


import re
import unittest
 
def read_passwords():
  return [password for password in input().split(',')]
 
def is_valid_password(password):
  if len(password) < 6 or len(password) > 12:
    print("Incorrect") 
 
  if not re.search(r'[a-z]+', password):
    return False
 
  if not re.search(r'[0-9]+', password):
    return False
 
  if not re.search(r'[A-Z]+', password):
    return False
 
  if not re.search(r'[$#@]+', password):
    return False
 
  return True

class TestIsValidPassword(unittest.TestCase):
  def test_minimum_maximum_length(self):
    self.assertTrue(is_valid_password('a6@E66'))
    self.assertFalse(is_valid_password('55555'))
    self.assertFalse(is_valid_password('3333333333333'))
 
  def test_contains_at_least_one_lower_letter(self):
    self.assertFalse(is_valid_password('111111'))
    self.assertTrue('11111a')
 
  def test_contains_at_least_one_number(self):
    self.assertFalse(is_valid_password('aaaaaa'))
    self.assertTrue(is_valid_password('aAa$a1'))
 
  def test_contains_at_least_one_upper_letter(self):
    self.assertFalse(is_valid_password('aaaaa1'))
    self.assertTrue(is_valid_password('aaAa#1'))
 
  def test_contains_at_least_one_special_char(self):
    self.assertFalse(is_valid_password('aaAaa1'))
    self.assertTrue(is_valid_password('aaAa@1'))
 
  def test_givent_problem_values(self):
    self.assertTrue(is_valid_password('ABd1234@1'))
    self.assertFalse(is_valid_password('a F1#'))
    self.assertFalse(is_valid_password('2w3E*'))
    self.assertFalse(is_valid_password('2We3345'))
 
 
if  __name__ == '__main__':
  valid_passwords = [password for password in read_passwords() if is_valid_password(password)]
  #unittest.main()
  print (','.join(valid_passwords))






"""
SCRIPT 19:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by>
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

"""


import operator
list_set = []
while True:
    data = input()
    if not data:
        break
    list_set.append(tuple(data.split(",")))

print(sorted(list_set, key = operator.itemgetter(0,1,2)))


#Output
"""
Input
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85


[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""








"""
SCRIPT 20:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""

def number(n):
    x = 0
    while x < n:
        j = x
        x = x + 1
        if j%7==0:  #numbers divisible by 7
            yield j

for x in number(100):
    print(x)

#Output
"""
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
"""







"""
SCRIPT 21:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

import math
position = [0,0]
while True:
    x = input("Input the digits here: ")
    if not x:
        break
    mov = x.split(" ")
    direc = mov[0]
    steps = int(mov[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))

#Output: UP 5 DOWN 6 LEFT 10 RIGHT 8

# 5








"""
SCRIPT 22:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

"""


line = input("Write anything here: ")                     
frequency = {}      # frequency of words in text
for word in line.split():
    frequency[word] = frequency.get(word,0)+1

words = list(frequency)
words.sort()

for wd in words:
    print("%s:%d" % (wd,frequency[wd]))
    
#Output
"""
here is some code
code:1
here:1
is:1
some:1

"""





"""
SCRIPT 23:
Write a method which can calculate square value of number

Hints:
Using the ** operator

"""


def square(num):
    return num ** 2

print(square(2))
print(square(3))


#Output: 
# 4
# 9






"""
SCRIPT 24:

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
Hints:
The built-in document method is __doc__


"""

def absolute(number):
        # it will return absolute Number

    return abs(number)

print (absolute(int(input('Enter Number :'))))


print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)


#Output:
"""
Enter Number :25
25
Return the absolute value of the argument.
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.

"""






"""
SCRIPT 25:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later

"""

class my_name:
    # Define the class parameter "name"
    name = "My"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

Cyndie = my_name("Cyndie")
print("%s name is %s" % (My.name, Cyndie.name))

Kamau = my_name()
Kamau.name = "Kamau"
print("%s name is %s" % (My.name, Kamau.name))

# Output: 
# My name is Cyndie
# My name is Kamau





"""
SCRIPT 26:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

"""

def add_two(no1, no2):
	return no1 + no2

print(add_two(5,6))

#Output: 11





"""
SCRIPT 27:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

"""

def conv_int_str(n):
    print(str(n))

conv_int_str(10)
#Output: 10




#-------------Repetition of no 27 --------------------------------------------------------------#
"""
SCRIPT 28:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

"""

def conv_int_str(n):
    print(str(n))

conv_int_str(10)

#Output: 10





"""
SCRIPT 29:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

"""

def add_string(s1,s2):
    print(int(x)+int(y))

add_string("1","8")


#Output: 9




"""
SCRIPT 30:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings

"""

def concatenate(s1,s2):
    print(s1+s2)

concatenate("7","9") 
#Output: 79





"""
SCRIPT 31:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

"""

def max_length(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
max_length("one","three")

#Output: three






"""
SCRIPT 32:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
"""

def even_odd(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
even_odd(7)

#Output: 'It is an odd number'


#--------------------------------------------------KEY POINT: DEFINING FUNCTIONS PYTHON----------------------------------------------------------------------------------------------------#







#---------------------------------------------------------LISTS, DICTIONARIES IN PYTHON ---------------------------------------------------------------------------------------------------#


"""
SCRIPT 33:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

"""

def make_dict():
    d=dict()
    d[1]=1
    d[2]=2**2  #value for 2 is its square
    d[3]=3**2  #value for 3 is its square
    print(d)
        
make_dict()

# Output: {1: 1, 2: 4, 3: 9}




"""
SCRIPT 34:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.

"""

def make_dict():
	d=dict()  # create a dictionary
	for x in range(1,21):
		d[x] = x ** 2   #square function
	print(d)

make_dict()

# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}





"""
SCRIPT 35:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""

def make_dict():
	d=dict()
	for x in range(1,21):
		d[x] = x ** 2  #square function
	for (k,v) in d.items():	
		print(v)

printDict()

#Output: 
"""
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
"""








"""
SCRIPT 36:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""

def make_dict():
	d=dict()
	for x in range(1,21):
		d[x] = x**2
	for key in d.keys():	
		print(key)

make_dict()

#Output:
"""
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

"""





"""
SCRIPT 37:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.

"""

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)     #square function
	print(li)

printList()

# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]




"""
SCRIPT 38:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

"""


def make_list():
	li=list()
	for x in range(1,21):
		li.append(i**2)  #square function
	print(li[:5])   # print first 5 elements in list

make_list()

#Output: [1, 4, 9, 16, 25]




"""
SCRIPT 39:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

"""


def make_list():
	li=list()
	for x in range(1,21):
		li.append(i**2)  #square function
	print(li[-5:])   # Print last 5 elements in list

make_list()

#Output: [256, 289, 324, 361, 400]






"""
SCRIPT 40:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

"""

def make_list():
	li=list()
	for x in range(1,21):
		li.append(x**2)
	print (li[5:])

make_list()


#Output: [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]


#-----------------------------------------------KEY POINT: WORKING WITH LISTS, DICTIONARIES IN PYTHON----------------------------------------------------------------------------------------#






#------------------------------------------ TUPLES, PYTHON ----------------------------------------------------------------------------------------------------------------------------------#




"""
SCRIPT 41:
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.

"""

def print_tup():
	li=list()
	for x in range(1,21):
		li.append(x**2)
	print(tuple(li))
		
print_tup()

#Output: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)






"""
SCRIPT 42:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

Hints:

Use [n1:n2] notation to get a slice from a tuple.

"""

tup_list=(1,2,3,4,5,6,7,8,9,10)
tup1=tup[:5]
tup2=tup[5:]
print(tup1)
print(tup2)

#Output:
# (1, 2, 3, 4, 5)
# (6, 7, 8, 9, 10)






"""
SCRIPT 43:
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

"""


tup=(1,2,3,4,5,6,7,8,9,10)
li=list()
for x in tup:
	if tup[x]%2==0:
		li.append(tup[x])

new_tup = tuple(li)
print(new_tup)


#----------------------------KEY POINT: USE OF TUPLES IN PYTHON -----------------------------------------------------------------------------------------------------------------------------#



"""
SCRIPT 44:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.

"""


string = input()
if string == "YES" or string == "Yes" or string == "yes":
    print "Yes"
else:
    print "No"
  
  
  
  
  
    
#-------------------------------------------USE OF LAMBDA, MAP, FILTER FUNCTION PYTHON--------------------------------------------------------------------------------------------------------#

"""
SCRIPT 45:
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

"""


list_digits = [1,2,3,4,5,6,7,8,9,10]
even_no = list(filter(lambda x: x%2==0, list_digits))
print(even_no)

#Output: [2, 4, 6, 8, 10]



"""
SCRIPT 46:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints
Use map() to generate a list.
Use lambda to define anonymous functions.

"""

list_digits = [1,2,3,4,5,6,7,8,9,10]
square_no = list(map(lambda x: x**2, list_digits))
print(square_no)

#Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



"""
SCRIPT 47:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

"""


list_digits = [1,2,3,4,5,6,7,8,9,10]
even_no = list(map(lambda x: x**2, filter(lambda x: x%2==0, list_digits)))
print(even_no)

#Output: [4, 16, 36, 64, 100]



"""
SCRIPT 48:
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

"""


even_no = list(filter(lambda x: x%2==0, range(1,21)))
print(even_no)

#Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




"""
SCRIPT 49:
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints
Use map() to generate a list.
Use lambda to define anonymous functions.

"""

square_no = map(lambda x: x**2, range(1,21))
print(square_no)

#Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]




#------------------------KEY POINT: USE OF LAMBDA, MAP, FILTER IN LIST GENERATION, MANIPULATION ----------------------------------------------------------------------------------------------#










#-----------------------------------------------------------------------CLASSES AND OBJECTS PYTHON ------------------------------------------------------------------------------------------------#

"""
SCRIPT 50:
Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.

"""

class American(object):
    @staticmethod
    def printNationality():
        print("America")

an_american = American()
an_american.printNationality()
American.printNationality()

#Output: America, America 




"""
SCRIPT 51:
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

"""


class American(object):
    pass

class NewYorker(American):
    pass

an_american = American()
a_new_yorker = NewYorker()
print(an_american)
print(a_new_yorker)

#Output:
# <__main__.American object at 0x7febc3c04df0>
# <__main__.NewYorker object at 0x7febc3c04dc0>




"""
SCRIPT 52:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

"""


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

a_circle = Circle(2)
print(a_circle.area())

# Output: 12.56

"""
SCRIPT 53:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

"""

class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())

#Output: 20


"""
SCRIPT 54:
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

"""


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())

#Output: 9

"""
SCRIPT 55:
Please raise a RuntimeError exception.

Hints:

Use raise() to raise an exception.
"""

raise RuntimeError('something wrong')



"""
SCRIPT 56:
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

"""



def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception, err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
    


"""
SCRIPT 57:
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

"""


class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")



#------------------------------------------------------------------KEY POINT: 'class()' FUNCTION IS USED TO CREATE OBJECTS ----------------------------------------------------------------------#






#----------------------------------------------------- PYTHON REGEX (REGULAR EXPRESSIONS) FUNCTION ------------------------------------------------------------------------------------------------#

"""
SCRIPT 58:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.
"""

import re
email_address = input("Please type your email address here: ")
email_format = "(\w+)@((\w+\.)+(com))"            #email format: cyndie@icipe.com
match = re.match(email_format, email_address)
print(match.group(1))

#Input: cyndie@icipe.com
#Output: cyndie



"""
SCRIPT 59:
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

"""

import re
email_address = input("Please add your email address here:  ")
email_format = "(\w+)@(\w+)\.(com)"
match = re.match(email_format, email_address)
print(match.group(2))

#Input: cyndie@icipe.com
#Output: icipe



"""
SCRIPT 60:
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.

"""



import re
seq = input()
print(re.findall("\d+",seq))   

#Input: 3 horses and 5 cows and 2 chicken and 1 dog
#Output: ['3', '5', '2', '1']

#-------------------------------------------------------KEY POINT: 're' FUNCTION IS USED TO SEARCH FOR PATTERNS IN A SEQ-----------------------------------------------------------------------------# 





#----------------------------------------------------------------- PYTHON UNICODE, ASCII-----------------------------------------------------------------------------------------------------#
"""
SCRIPT 61:
Print a unicode string "hello world".

Hints:

Use u'strings' format to define unicode string.

"""


string = u"hello world!"
print(string)

# Output is still 'hello world!'

"""
SCRIPT 62:
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

"""

ascii_string = input("Write anything here: ")
unicode_string = unicode( ascii_string ,"utf-8")
print(unicode_string)



"""
SCRIPT 63:

Write a special comment to indicate a Python source code file is in unicode.

"""

```
# -*- coding: utf-8 -*-

#----------------------------------------#
```


#------------------------------------------------KEY POINT: CONVERTING UNICODE TO ASCII, VICE VERSA --------------------------------------------------------------------------------------#

"""
SCRIPT 64:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float
"""


n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)



"""
SCRIPT 65:

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

"""


def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))




"""
SCRIPT 66:
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.
"""

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))




"""
SCRIPT 67:
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13


Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))




"""
SCRIPT 68:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))






"""
SCRIPT 69:
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

"""


def generate_no(n):
    for x in range(n+1):
        if x%5==0 and x%7==0:     #function generate_no() generates no divisible by 5 and 7 between 0 and n.
            yield x

n=int(input("Please input a figure: "))
values = []
for x in generate_no(n):
    values.append(str(n))   # create a string from the output

print(",".join(values))   # join the string made of digits, separated by a comma







"""
SCRIPT 70:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.

"""



list_digits = [2,4,6,8]
for x in list_digits:
    assert x%2 == 0    # assert() verifies all digits in list are even nos.
    






"""
SCRIPT 71:
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.

"""


expression = input("What do you want to calculate? ")
print(eval(expression))  #performs calculation





#---------------------- No. 73 and 72 are similar --------------------------------------#

"""
SCRIPT 72:  
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

"""
    
 import math
def search(list_digits, element):
    bottom = 0
    top = len(list_digits)-1
    index = -1
    while top>=bottom and index==-1:
        middle = int(math.floor((top+bottom)/2.0))
        if list_digits[middle] == element:
            index = middle
        elif list_digits[middle] > element:
            top = middle - 1
        else:
            bottom = middle + 1

    return index

list_digits = [2,5,7,9,11,17,222]
print(search(list_digits,11))
print(search(list_digits,12))



"""
SCRIPT 73:
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

"""

import math
def search(list_digits, element):
    bottom = 0
    top = len(list_digits)-1
    index = -1
    while top>=bottom and index == -1:
        middle = int(math.floor((top+bottom)/2.0))     # function search() returns index of elements to be searched for in a list
        if list_digits[middle] == element:
            index = middle
        elif list_digits[middle] > element:
            top = middle - 1
        else:
            bottom = middle + 1

    return index

list_digits = [2,5,7,9,11,17,222]
print(search(list_digits,11))  #Output : 4
print(search(list_digits,12))  #Output : -1









#---------------------------------------------------------------------USING `RANDOM` FUNCTION TO GENERATE RANDOM DIGITS --------------------------------------------------------------------------#


"""
SCRIPT 74:
Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

"""

import random
print(random.random()*100)  #randomly generate a float between 10 and 100 (*100)

# Output: 68.1712212199406



"""
SCRIPT 75:
Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

"""


import random
print(random.random()*100-5)  #randomly generate a float between 5 and 95 (*100-5)

# Output: 86.53671800809406





"""
SCRIPT 76:
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

"""

import random
print(random.choice([i for i in range(11) if i%2==0])) #generate a random even number between 0 and 10

# Output: 0



"""
SCRIPT 77:
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.
"""


import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))

# Output : 70



"""
SCRIPT 78:
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

"""


import random
print(random.sample(range(100), 5)) #generate random list of 5 digits 

# Output: [70, 24, 62, 51, 64]


"""
SCRIPT 79:
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

"""


import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))  #generate random list of 5 even nos. 

#Output: [100, 122, 172, 176, 192]


"""
SCRIPT 80:
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:
Use random.sample() to generate a list of random values.

"""


import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))

# Output: [140, 700, 910, 770, 945]


"""
SCRIPT 81:
Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
Use random.randrange() to a random integer in a given range.

"""



import random
print(random.randrange(7,16))

# Output: 13

#------------------------------------------------------------------- KEY POINT: USING RANDOM FUNCTION IN PYTHON--------------------------------------------------------------------------------------#



"""
SCRIPT 82:
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

"""


import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

#output for compress:    "b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'"
#output for decompress:  "b'hello world!hello world!hello world!hello world!'"




"""
SCRIPT 83:
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.

"""

from timeit import Timer   #import timeit()function to measure time
time = Timer("for i in range(100):1+1")   
print(time.timeit())

#output was '1.099715970998659'




"""
SCRIPT 84:
Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

"""



from random import shuffle  #used to import shuffle() function
digits = [3,6,7,8]
shuffle(digits)
print(digits)



#------ Repetition of no. 84-------------------------------------------------------------#
"""
SCRIPT 85:       
Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

"""


from random import shuffle   
digits = [3,6,7,8]
shuffle(digits)
print(digits)



"""
SCRIPT 86:
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

"""


subject = ["I", "You"]
verb = ["Play", "Love"]
obj = ["Hockey","Football"]
for a in range(len(subject)):
    for b in range(len(verb)):
        for c in range(len(obj)):
            string = "%s %s %s." % (subject[a], verb[b], obj[c])          #script uses index of all characters to assemble a string. Output is ' I Play Hockey, I Play Football....etc'
            print(string)
 
 
 
 
 
            
#----------------------------------------------------------------------------- LIST COMPREHENSION ----------------------------------------------------------------------------------------------------#

"""
SCRIPT 87:
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

"""

digits = [5,6,77,45,22,12,24]
digits = [x for x in digits if x%2!=0]    # outputs digits which are odd numbers
print(li)



"""
SCRIPT 88:
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.

"""


digits = [12,24,35,70,88,120,155]
digits = [x for x in digits if x%5!=0 and x%7!=0]   #outputs digits not divisible by 5 and 7
print(digits)



"""
SCRIPT 89:
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.


"""


digits = [12,24,35,70,88,120,155]
digits = [x for (a,x) in enumerate(digits) if a%2!=0]  #used to output digits in 1st, 3rd and 5th index (odd nos) 
print(digits)




"""
SCRIPT 90:
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

"""

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)




"""
SCRIPT 91:
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

"""

digits = [12,24,35,70,88,120,155]
digits = [x for (a,b) in enumerate(li) if b not in (0,4,5)]
print(digits)





"""
SCRIPT 92:
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.

"""


a = [12,24,35,24,88,120,155]
a = [digit for digit in a if digit != 24]    #used to output all other digits except 24
print(a)



"""
SCRIPT 93:
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.

"""


list_a = set([1,3,6,78,35,55])
list_b = set([12,24,35,24,88,120,155])
list_a &= list_b    #"&=" operator intersects two variables.
x = list(list_a)
print(x)


"""
SCRIPT 94:
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

"""

def rem_duplic( digits ):       #function to remove duplicates from given list
    digits_new = []
    minus_duplic = set()
    for item in digits:
        if item not in minus_duplic:     #set stores value without duplicates
            minus_duplic.add( item )     #duplicates are stored in the digits_new dictionary
            digits_new.append(item)      #minus_duplic stores values not repeated

    return digits_new

digits = [12,24,35,24,88,120,155,88,120,155]
print(rem_duplic(digits))





#-------------------------------------------------------------------------------KEY LESSON: MANIPULATION OF LISTS ---------------------------------------------------------------------------------#



"""
SCRIPT 95:
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

"""


class Person(object):       #this class is used to define a person
    def getGender( self ):
        return "Unknown"

class Female( Person ):       #this class is used to print a female
    def getGender( self ):
        return "Female"

class Male( Person ):         #this class is used to return male
    def gender( self ):
        return "Male"

man = Male()
woman = Female()
print(man.getGender())
print(woman.getGender())





"""
SCRIPT 96:
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

"""



string = input("Please input your string: ")
str_dict = dict()
for string in string:
    str_dict[string] = str_dict.get(string,0)+1
print('\n'.join(['%s,%s' % (x, y) for x, y in str_dict.items()]))



"""
SCRIPT 97:
Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.

"""


reverse = input("Please input your string: ")
reverse = reverse[::-1]    #iterates a string in reverse.
print(reverse)



"""
SCRIPT 98:
Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

Hints:
Use list[::2] to iterate a list by step 2.
"""


string = input("Please type your string as input: ")
string = string[::2]     #[::2] iterates a list by 2
print(string)


"""
SCRIPT 99:
Please write a program which prints all permutations of [1,2,3]

Hints:
Use itertools.permutations() to get permutations of list.

"""

import itertools
print(list(itertools.permutations([1,2,3])))




"""
SCRIPT 100:
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

"""


heads = int(input('Enter the total number of heads:'))
legs = int(input('Enter the total number of legs:'))
if legs % 2 !=0 or heads ==0 or heads > legs:    #Conditions to print 'No Solution'
   print('No solution')
else:  
   a = int((legs + (-2*heads))/2)
   b = int(heads - a)
   print('{} {}'.format(a,b))



#---------------------------------------------------------------------------THE END. ADIOS AMIGOS! -----------------------------------------------------------------------------------------------#
