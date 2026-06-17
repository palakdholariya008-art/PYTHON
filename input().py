Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="mark"
name
'mark'

first_name=input()
palak
first_name
'palak'

frist_name=input("Enter your name:")
Enter your name:

age=input("How old are you? ")
How old are you? 30
age
'30'

num1=input("Enter a number: ")
Enter a number: 15
print(num1)
15

print(num2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(num2)
NameError: name 'num2' is not defined. Did you mean: 'num1'?
num2=34
print(num2)
34

res=num1+num2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    res=num1+num2
TypeError: can only concatenate str (not "int") to str
>>> result = num1 +num2
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    result = num1 +num2
TypeError: can only concatenate str (not "int") to str
>>> num1
'15'
>>> num2
34
>>> res=num1+str(num2)
>>> res
'1534'
>>> print(res)
1534
>>> res=int(num1)+int(num2)
>>> print(res)
49
