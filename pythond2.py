#a=7,8
#print(a)
#print(type(a))



#a, b, c = 9, 8, 7
#print(a, b, c)


#a, b=c=7, 8
#print(a)
#print(b)
#print(c)


#a=b, c = 4, 2
#print(a, b, c)

#Eg:1
# ----> swapping of variables
#a=7
#b = 5
#temp=a
#a=b  #a=5
#b=temp #b=7
# a=5, b=7
#print(a,b)


#Eg:2
#a=7
#b=5
#a=a+b #a=12
#b=a-b #b=12-7=5
#a=a-b #a=12-5=7
#print(a,b)
#a, b=b, a #only in python
#print(a,b)


#a=a*b
#b=a/b
#a=a/b
#print(int(a),int(b))


# id() --> used  to find the memory address of the variable
#a = 7
#b = 8
#print(a)
#print(b)
#print(id(a))
#print(id(b))



# -----> keywords


#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

#to check if the string is keyword or not
#print(keyword.iskeyword("sid")) #false

#if = 8
#print (if) #error coz if is a keyword


# !----> literals
# literals is the constant value asssigned to a variable
# A variable is considers to be constant when it is defines
# in caps

#a=78 # a is variable
#A=78 # A is constant

# hash()--> it creates a hash value for constant datatypes and
#provides error for non constant datatypes
#n1 = 89+7j
#print(hash(n1))
#f1 = [7, 8, 9]
#print(hash(f1)) # error ---> list is non-constant or mutable datatype


#! ----> operators
# ? operators are symbols which is used to perform various operions
# ? between 2 or more operand

#arthmatic
#Assignment
#Logical
#Relational or comparison
#Bitwise
#Identity
#Membership

# todo---> arithmatic --> +,-, *, /,%,//,**
#eg:1
#a = 8
#b = 6
#print(a+b+c)

# input ---> used to get the runtime input
#eval() ---> used to get the runtime values of all datatype
#n1 = int(input("enter the value: "))
#print(type(n1))


#n1 = eval(input("enter the value: "))
#print(type(n1))



#a = 4
#b = 2
#print(a/b) # is used to get the quotient value
#print(a%b) # is used to get the remainder value



# ! // --> floor devision


#a = 765433
#b = 19
#print(a/b)
#print(a/b) # -> the output will be inn integer & the output
# based on floor value


#!  ** --> used for power of a number
#print(2**4) #--> 16


# ! Assignment --> = +=, -=, /=,


#a=8
#a+=2
#print(a)

#a=30
#a-=5
#print(a)


# ! comparison --> ==, >, <, !+, <=, >=
#a = 8
#b = 7
#print(a>b)



#a = 9
#b = 5
#print(a==b)


# ! Bitwise operator --> &, |, ^, ~, <<, >>
#a = 7
#b = 4
#print(a&b)


# 2^4 2^3 2^2 2^1 2^0
 # 8   4   2  1
 # 0   1   1  1   #--> 7
 # 0   1   0  0   # --> 4 &
 #-------------------
 # 0   1   0  0
 

# ~ --->
#a = 9876
#print(~a)

#a = 9
#print(~a+1)

# ! logical --> used to compare the expressions
# and, or , not
#a = 6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))


# ! Identity operator
# is, is not
#a = 8
#b = 8
#print(a is b)
#print(a==b)

#a = [1, 2, 3]
#b = [1, 2, 3]
#print(a is not b)


# ! Membership operator
# in, not in
#l1 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num in l1)
#print(num not in l1)


#num = 678
#print(8 in num) #error


#Eg:1
#a = 6
#if a:
  #  print("hello")

#Eg:2
#a = 6
#if a>3:
  #  print("hey")
#else:
 #       print("no")


#Eg:3
#if 7>8:
#    print("hello")
#else:
  #  print("no")


Eg:4
#a= 0
#a = None
#a = false
#a=""
#if a:
 #   print("yes")
#else:
   # print("no")



# a number is even or odd
n = int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")











