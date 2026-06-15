Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1="Hello world"
s1
'Hello world'

type(s1)
<class 'str'>

s2='we are learning python'

s2
'we are learning python'

type(s2)
<class 'str'>

s3="""hello everyone.
we are looking at strings.
bye"""
s3
'hello everyone.\nwe are looking at strings.\nbye'


type(s3)
<class 'str'>
s4="python"
len(s4)
6
 s1
 
SyntaxError: unexpected indent
s1
'Hello world'
len(s1)
11
len(s2)
22
len(s3)
46


#indexing

s4[3]
'h'
s1[1]
'e'
>>> s2[5]
'e'
>>> s3[14]
'.'
>>> s3[-1]
'e'
>>> s1
'Hello world'
>>> s2
'we are learning python'
>>> s1 + s2
'Hello worldwe are learning python'
>>> s2 + ' ' +s2
'we are learning python we are learning python'