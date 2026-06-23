
"""
reverse(),sort(),count()
"""

days_of_week=["mon","tue","wed","thur","fri","sat","sun"]
print(days_of_week)

#reverse()
days_of_week.reverse()
print(days_of_week)

nums=[23,434,5,56,78,45,3,23,46,54,63,47,67,78]
print(nums)

#sort() min ... max
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

#count()

numbers=[2,3,34,5,56,7,7,88,9]
print(numbers.count(7))

#in
print(3 in numbers)

NUMBERS=[10,23,4,5,40]

#SMALLEST NUMBER IN THE LIST
#MIN()
print(min(NUMBERS))

#Biggest number in the list
#max()

print(max(NUMBERS))


#NESTED LIST
l1=[5,1.5,4,3,2,"python",None,[1,2,3,4]]
print(l1[-1])
print(l1[-1][0]) #first one last element and then last index is for first elemnet of indexing

#list inside a list
l2=[[1,2],[3,4],[5,6,[0,1]]]
print(len(l2))

