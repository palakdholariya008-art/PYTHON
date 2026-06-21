#Membership operation
#in
s1="Python is fun"
print("Python " in s1)
print("i" in s1)


#not in
print("I " not in s1)
print("Python" not in s1)

#comparison of string
print("Python " == "Python")

#removing spaces from a string -strip()

s1=("Python ")
print(s1.strip() == "Python")

#replace()

s1="We are learning python"
print(s1)
print(s1.replace("Python","Java"))
print(s1)

#coutning substring from a string
#count()
#string.count(substring)

s1="We are learning python.python is fun"
s2=" "

print(f"occurences of spces is {s1.count(s2)}")

#changing case of a string
#upper(),lower(),title(),capatilize()

s1="Python fun"
print(s1)
s1="Python is fun!!"
print(s1)
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())

#startswith()
#string.startswith(substring)
s3="Python is fun!!"
print(s3.startswith("P"))

#endswith()
print(s3.endswith("Python"))

