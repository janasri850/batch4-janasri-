# !  ----> common functions for list
#l1 = [6, 7, 8, 9, 0]
#print(len(l1))

#print(max(l1))
#print(min(l1))
#l1 = [6,8,9,"p","u"]
#print(max(l1))# ---> error coz its a combination of int and string 
#print(min(l1) # ---> error coz its a combination of int and string

#l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#index() ---> to get index value of specific element
#print(l1.index(9))


#l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# count() --> how many num of times an element is repeated
#print(l1.count(6))

#! some functions which is specifically used for list
#to add element inside list
# ? insert() --> to add element at specific index position
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2, "cars")
#print(l1)

#pop () ---> last element will be deleted
#l1.pop()
#print(l1)

# pop (index_value) --> used to delete element at specific index
#l1.pop(4) # 4 is index value
#print(l1)
  

#remove(element) ---> used to delete element directly
#l1.remove(8.89)
#print(l1)
#* clear() --> to complete delete all element in list
#l1.clear()
#print(l1)

# del --> to delete the list
#del l1 #or del(l1)
#print(l1)

# ? ---> join 2 list
#l1 = [9, 0, 8]
#l2 = ["p", "o", "t", 34]
#print(l1+l2)

# or
# extend () --> to combine 2 lists
#l1.extend(l2)
# print(l1)

# ? ------> copy()
# l1= [6, 7, 8, 9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)

# print(id(l1))
# print(id(l2))

# ! diff between shallow copy and deep copy
# shallow copy
# import copy
# l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
# l2 = copy.copy(l1)
# l1.append(890)
# print(l1)
# print(l2)

# * deep copy
#import copy
#l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
#print(l1[-1][1]) --> to index nested list
#l2 = copy.copy(l1)
#l1.append(890)
#print(l1)
#print(l2)


# ? sort --> arrange element in list in ascending or descending order
#l1 = [9, 7, 45, 0, -6,5,12]
#l1. sort() # to arrange in ascending order
#print(l1)

#l1.sort(reverse=true) # to sort in descending order
#print(l1)

#l1 = ['z', 'i', 'o', 'p', 9]
#l1.sort()
#print(l1) # --> error

# ? list constructor
# * list() ---> to convert other collection datatype to list
#13 = ((8, 9, 0)
#print(list(13))       

# 14 = (8,9)
#print(list(14))

# ---> nested list

#l1 = [8,9,[0,8,7],["p","o",'y'],[8,'t']]
#print(l1[-2][1])
#print(l1[-3])
# ? to delete "t" from l1
#l1[-1].remove('t')
#print(l1)

# ?  combine these ["p","o",'y'],[8,'t'] lists in l1 to ["p","o",'y',8,'t']

#l1 = ["p","o",'y']
#l2 = [8,'t']
#l1[len(l1):] = l2
#print('l1 =',l1)

# ! -----> tuple
#*char of tuple

# 1.) tuple have to be surrounded by()
# 2.) The elements inside tuple are not changable
# 3.) The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) it is heterogenous
# 6.) it allow duplicate elements

#eg:1
#t1 = (8,8, 9,6,5.78,[9,0],(6,8),"hey", 9+6j)
#print(t1)
#print(type(t1))

# ? indexing, slicing are all same as list
#l1 = [8]
#print(type(l1)) #tuple

#t1 = 8,9
#print(type(t1))

# len(), min(), max(),index(), count() --> all same as list

#to add element inside tuple ---> cannot add
#cannot delete any element from tuple

#* join 2 tuples
#t1 = (8, 9, 0)
#t2 = (6, 7, 8)
#print(t1+t2)

# * to add all element inside list and tuple
# sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))

# * sort tuple
#t1 = (8, 9, 0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples
#l1 = [9,8,0,6,5]
#for i in l1:
#    print(i) 

# * iterate based on index value
#l1 = [9, 8, 0, 6, 5, 8, 56]
#for i in range(0, len(l1)):
#     print(l1[i])

# ! ---> string
#s1 = 'o'
#print(type(s1))

#s1 = 'u'
#print(type(s1))

#s1 = "hello world"
#* to access string
#print(s1)

# indexing and slicing --> same as list and tuple
#print(s1[0:5])

# --> common function
   
# len(), min(), max(), index(), count()
#s1 = "hello world"
# print(len(s1))
# print(max(s1))
# print(min(s1))

# ord() ---> used to find the ASCII value of a character
# s1 = 'u'
# print(ord(s1))

# ! Functions of string
#s1 =  "hello world"

# ? to convert all characters to upper case
# print(s1.upper())

# ? to convert lower case
# s1 = "HEREDGIOU"
# print(s1.lower())

# ? strip() --> to eliminate the space in beginning and end of string
#s1 = "Where are you?"
#print(s1.lstrip())
#print(s1.rstrip())
#print(s1.sstrip())
# split() -->
#s1 = "where are you?"
#print(s1,split())
#print(s1,split("r"))
 
#print(s1,count('e'))
  


# * join the strings

#s1 = "hello"
#s2 = 'world'
#print(s1+s2)

#s1='''
#how are you
#i am find
#hey there
#'''
# * splilines() --> used to split the string based on lines
# print(s1.splitlines())

#* find()
#s1 = "hello world"
#print(s1.find('h'))
#print(s1.index('h'))

# * join() -->
#l1 = ["hey", "there"]
#print(" ".join(l1))
#print("$".join(l1))

#s1 = "welcome to all"
# * print(s1.endswitch('1'))
# * print(s1.startswitch('w'))

# s1 = "67"
#print(type(s1))
#print(s1.isdigit())

# * print the string in reverse manner
#s1 = "welcome to all"
#print(s1[::-1])

# ! ---> eg:1
#wap to find the number of lower case letters
#s1 = "HEY there you aRE"
#count = 0
#for i in s1:
#     if i.islower():
#          count+=1
#print("the total num of lower case letters:",count)


# ! --->eg:2 r---> "$"
#s1 = 'restarter'
# s1 = "IMAGIN"
#fst = s1[0]
#bal = s1[1:]
txt = bal.replace(fst,"$")
#print(s1.replace('r',"$"))

#str1 = "bbbbbyyybbbaaioo"
#str = "%"




























































