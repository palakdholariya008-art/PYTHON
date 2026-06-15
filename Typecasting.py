Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Type conversation /type casting

num1=100

num1
100
type(num1)
<class 'int'>
float(num1)
100.0

num2=float(num1)

num2
100.0
type(num2)
<class 'float'>
num1
100

type(num1)
<class 'int'>
num1=float(num1)
num1
100.0
type(num1)
<class 'float'>

num3=56.66

num3
56.66
type(num3)
<class 'float'>
int(num3)
56
int(77.85)
77
num4=1000

num4
1000

str(num4)
'1000'
int()num4
SyntaxError: invalid syntax
x=str(num4)
x
'1000'

type(x)
<class 'str'>
str(num3)
'56.66'
int(num3)
56
s1='hello'
s1
'hello'
str(s1)
'hello'
s1="hello"
str(s1)
'hello'
int(s1)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int(s1)
ValueError: invalid literal for int() with base 10: 'hello'
float(s1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    float(s1)
ValueError: could not convert string to float: 'hello'

s2='12345'
type(s2)
<class 'str'>

int(s2)
12345

y
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    y
NameError: name 'y' is not defined
y=int(s2)
y
12345
type(y)
<class 'int'>

s3='55.34'
float(s3)
55.34

s4="pythom3.14.6"
s4
'pythom3.14.6'
float(s4)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(s4)
ValueError: could not convert string to float: 'pythom3.14.6'
int('1234a')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int('1234a')
ValueError: invalid literal for int() with base 10: '1234a'

int('123-')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    int('123-')
ValueError: invalid literal for int() with base 10: '123-'

lan="python"
ver=3.14

#contan

lan + ver
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    lan + ver
TypeError: can only concatenate str (not "float") to str

lan + str(ver)
'python3.14'

 
'100'+'100'
'100100'
int('100') + int('int')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int('100') + int('int')
ValueError: invalid literal for int() with base 10: 'int'
int('100') + int('100')
200


val1=True
val1
True

type(val1)
<class 'bool'>

str(val1)
'True'

bool('python')
True

bool(100)
True

bool(1.5)
True
bool(0)
False
bool(0.0)
False

bool(104)
True

bool(-100)
True
bool(-10.5)
True

bool(0.5)
True
# only 0 and 0.0 gives you false other noone gives you

bool("hi")
True
bool('a')
True
bool(' ')
True

#Empty string => '' , "" , """ """
bool("")
False

#None
>>> bool(None)
False
>>> 
>>> int(200)
200
>>> int(True)
1
>>> 
>>> int(False)
0
>>> float(True)
1.0
>>> float(False)
0.0
>>> str(False)
'False'
>>> str(None)
'None'
>>> str(True)
'True'
