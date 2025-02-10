#creating a list
list=[]
print("Blank list:",list)

#creating a list of numbers
list1=[1,2,3,4,5]
print("List of numbers:",list1)

#creating a list of multiiple datatypes
list2=[1,2,"Mon",2.4]
print("List of multiple datatypes:",list2)

#indexing and slicing
list3=["Jan","Feb","March","April","May"]
print(list3[0])
print(list3[1:4])

#creating a multi-dimensional list
list4=[["Jan","Feb"],["June","July"]]
print("Multi-dimensional list:",list4)

#creating empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

#creating a dictionary using dict method
dict1 = dict({1: "Mon", 2: "Tues"})
print("Dictionary using dict method:", dict1)

#creating a dictionary with each item as a pair
dict2 = dict([(1, "Jan"), (2, "Feb")])
print("Dictionary with each item as a pair:", dict2)

#tuple
#one item tuple
t=(0,)
print(t)

#four item tuple
t1=(1,2,3,4)
print(t1)

#without parenthesis
t2=1,2,3,4
print(t2)

#nested tuple
t3=('abc',('def,','ghi'))
print(t3)

#creating the empty set
set1 = set ()
print("Empty Set: ", set1)

#adding elements to a set
for i in range (1,6):
    set1.add(i)
print("Set after adding elements: ", set1)
set2 = set ()

#adding elements to set2
for i in range (1,3):
    set2.add(i)
print("Set after adding elements: ", set2)