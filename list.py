name="John"
age=20
percent=85.8

student=["John",20,85.8]  ##stores float ,strg, int
print(type(student))
print(student)

days_of_week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(days_of_week[4])
print(f"Last day of the week is {days_of_week[6]}")

#length of a list => the number of items/elements in the list
print(len(days_of_week))


#slicing of list
l1=[1,3,34,52,4,56,3,5,66,6]

print(l1[1:6:2])
print(l1[1:3:1])

#concatenation of lists
l1=[1,2,3,4,5,6,]
l2=[0,3,4]
print(l1 + l2)
print(l2+l1)


#Repetition of list
l1=[1,2,3]
l2=[0,4,3]

# *
print(l2 * 4)
print(l1 * 2)


#append()
#adds an item to the end of the list

fruits=["mango","apple","banana","grape"]
print(fruits)

#synax: list.append(item)

fruits.append("banana")
print(fruits)

#insert
#adds an element before the specified index
#syntax: list.insert(index,item)

fruits.insert(0,"banana")
print(fruits)

#extend(),remove(),pop()

#extend(){ append add single element to list and extend add multiple element to the list}
fruits=["Apple","Mango","Grape"]
fruits.extend(["banana","grapes"])
print(fruits)

#remove()
fruits.remove("banana")
print(fruits)

#pop()
fruits.pop(-1)
print(fruits)
