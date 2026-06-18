#Fstring

name="John"
age=20
language="English"

print(name,"is",age,"years old")

#using f-string (if we want to value as in varible then we use it)
print(f"{name} is {age} years old")

#\n - next line
#\t- tab
#\\ - backslash
#\* - inserts a single quote inside a single-quoted string

#\n
print("Hello world \nhow are you?")

#\t
print("John 20")
print("John\t20")

#\\

print("New\\old")
print("YES\\NO")

#\'

print('This is Python\'s class')
print("This is Python\'s class")

#\"

print("He says, \"we are learing Python\"")

#string Operations

s1="Pyhton is fun"
print(s1[0])
print(s1[-1])

language="Python"
version=13.4
print(language + str(version))
#print("Python" - "p")#not supported
print(s1 * 3)
