# ---> while loop
#----> break using while loop


#eg:1
# 1.) iterate from 20 to 30 and break the loop in 27
#i = 20
#while i<31:
#   print(i)
#    if i ==27:
#        break
#    print(i)
#    i+=1


#i = 20
#while i<31:
#    print(i)
#    if i ==27:
#        break
#    i+=1
    
# ! ---> continue
# ---> Eg:1

#i = 20
#while i<31:
#    if i ==27:
#        continue
#    print(i)
#    i+=1

#i = 20
#while i<31:
#    i=i+1
#    if i ==27:
#        continue
#    print(i)
    
       
# ! Eg:5
#while to iterate from 12 to 22
#find the sum of all numbers
#i = 12
#sum=0
#while i<23:
#    sum+=i
#    i+=1
#    if i == 23:
#        print(sum)
#   

# find the average of value from 20 to 25
#i = 20
#avg = 0
#while i<26:
#    avg+=i
#    i+=1
#print(avg/6)

# ! ----> nested for loop
# Eg:1
#for i in range(1,3+1):
#    for j in range(1,4+1):
#        print(i,j)


#for row in range(1,3+1):
#    for col in range(1,4+1):
#        print(row,col)

#for row in range(4):
#    for col in range(4):
#        print("*", end=" ")
#    print()
        


#for row in range(5):
#   for col in range(5):
#        print(row, end=" ")
#   print()
        

#sum = 0
#for row in range(5):
#   for col in range(5):
#       sum= sum+1
#       print(sum, end=" ")
#   print()

#! to print starts in right angled triangle
#for row in range(0,6):
#   for col in range(0. row+1):
#      print("*", end=" ")
#    print()


#for row in range(6,0, -1):
#   for col in range(0,row):
#      print("*", end=" ")
#   print()   

#for row in range(5):
#    for col in range(5):
#        if col==0 or col ==5-1 or row ==0 or row ==5-1:
#            print("*",end=" ")
#        else:
#             print(" ", end=" ")
#    print()   




#for row in range(5):
#    for col in range(5):
#        if (row==0 and col==3) or (row==1 and (col>=2 and col<=4) or
#                                   (row==2 and (col>=1 and col<=5))):
#            print("*",end=" ")
#        else:
#             print(" ", end=" ")
#    print()   



#for row in range(0,5):
#    for col in range(0,6):
#        if (row==1 and col==0) or (row==1 and (col>=2 and col<=4) or
#                                   (row==2 and (col>=1 and col<=5))):
#            print("*",end=" ")
#        else:
#             print(" ", end=" ")
#   print()


 #----> List

# ----> list

# ---> Datatypes
# primary

# Number --> int, float complex
# string
# Boolean
# None

# Colection
# List
# tuple
# set
# dictionary




# 1.) if the collection of elements are sorounded by square brackets,
#it is considered to be list

# ! eg:1
    #l1 = [4, 7, 9, 9.89, "hello", 7+9j,[8, 9, 0]]


# * characteristics of list
# 1.) list have to be sorrounded by[]
# 2.) it is mutable (the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) the elements inside list will be ordered format
# 5.) it can hold duplicate values
# 6.) its heterogenous

# To access the elements in list
#l1 = [1, 4, 1, 7,89.7,  7.5, "p", "i"]
#print(l1)


# ----> indexing
# In the collection datatype like list , tuple, string, the element will
#be alloted with pre-defined unique value called index value

# we have 2 types of indexing
#positive indexing --> starts with 0 from left hand side
#negative indexing --> starts with -1 from right hand side

# ? --> positive indexing
#lst1 = [1, 4, 1, 7,89.7, 7.5, "p","i"]
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])


# ? --> negative indexing
#lst1 = [1, 4, 1, 7,89.7, 7.5, "p","i"]
#print(lst1[-1])
#print(lst1 [-5])


# ? ---> slicing
#lst1 = [1, 4, 1, 7,89.7, 7.5, "p","i"]
# lst[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])


# print(lst1[0:7:1]) #lst1[0:7] --> both are same
#print (lst1[0:7:2])

#lst1 = [1, 4, 1, 7,89.7, 7.5, "p","i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) -->[]
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

#! To insert to add element inside list
# append()
#l1 = [9, 8, 0, 6]
#l1.append("car")
#print(l1)





























#s1 = "hello world to all"
