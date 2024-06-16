print("hello  world")


# comment line 
#

'''
 this is   new 

'''

#  here python use indenetaion   not block 
#    where  other lanagauage   use   {}



# if  ( condition) {




# }


# python cli  is   open terminal       use repl->read evaluete  print  line 

# type   >python  

# # (repl)   will  be open 

# # to exit 
# exit





# variable value can   be overwrite 
x =10
x = "zero"


print(x)

# data  can be of different type 

# x =5  (integer data  type )


# y ="string"(  string   data type )


# z =5.5 (float  data type )


# d =false (  boolean data  type )


# c =null  (nothing  data  type )

# in python    


# python is   dynamically type  we cannot give program which data  type variable 
# program automatically   find  data  type of variable 


# varaible  name are case-sensitive 
# count  or COUNT are different 

#  a  variable  name cannot   be any   of python  keyword 

name="isha"

roll =23
print(type(name))

# <class 'str'>


# different data  type   cannot   be used   in   conecate 
print("my name  is "+ name +   "  and  my roll no. is ",roll )

# //  print   expression


# print(" my  perxentage  has changed   to"  , percentage-1.4)


# printing   with separator 


# print(name, roll_number, percent, sep="-")

x =1
y =4
z =6

print(x,y,z,sep="__")
# by deafult space  add ho   jata   hai 
# o/t->
# 1__4__6

# data  type 

# numeric data  type 

# 1.int
# 2.float
# 3.complex ->    1+2j,23+45j



# # text data type 

# string 

# boolean data  type 
# true /false 



# sequnce data type 
# string 
# list  (sequnce of integer, string  )  [1,2,3,4,5] 
# # collection   of item is  unique   and can be modified 

# tuple 
#  (1,2,3,4,5,5)

# # dublicate value   can be  but not modified 


# dictionary   data  type 


# # data  store in ket-value pair 

# #   student   ={


# #     "value":2213123,
# #     "rollno":3121,
# #   }



'''



set  data  type -> unordered collection of unique item 
 {
 "apple","mango ","banaana"
 }

 


None  data  type :  null  value 


Ascii  and Unicode value 

american standard code for information interchange 
it helps  to represent character   using   numeric code 

A-Z   65-90


a-z  97-122

0-9 -> 48-57
(it act a sa character )
space ( )->32 



ord()  function  -> it gve ascii  calue of chacater 






'''






# char    ="a"






# print(ord(char))

# ord  functon  parameter must be length 1


# char()  it giev chacatre for the ascii value 

# ascii=34
# print(chr(ascii))






# input   take .

# using  input keyword 
# name1=input("enter name here :")
#        # input  function   store value in string 
# print(name1)


# # typecasting -> it is process of converting one data type into another data  type 
# rollno   = int(input("enter   roll number "))

# print(type(rollno))


# n1 = int(input("enter  first number"))

# n2 = int(input("enter    second number"))

# sum = n1+n2

# print("the sum is ",sum)

#   operator  


# arithematic operator
# +,-,*,/,%(modulus),**(exponential), //(floor division)


# floor(give nearest whole number )  eg->23.344
# # 23

# moduls-> 4//3 =>1

# 2**3->8


# logical  operator 

# and,Or, Not

# ^(xor)  -> 11->1
# 10->0
# 00->1
# 01->0

# operator precednce 


# BODMAS rule
# bracket open division multplicarton  addition subltration 

# () / * + -


# 1.()
# 2.** (  to calculate power )
# 3./,//
# 4.*
# 5.+,-
# 6biwise >>,<<
# 7&&, or not

# 8.comparsion 
# = ,== 
# 9/logical 


# condition




# list 


# indexed   o based  indexed 
# orederd   (item is list it remain same )
# mutable (that you are  able   to change  the   value   of   indexed)  list[1] ="new"
# dublicate allowed 
# any data type 
# mix of diferent  data  type 




# list 

fruits  = ["apple","mango","banana","pinapple"]



print(fruits)



if "banaan" in fruits:
    print("bnaana  is part of list ")


if "kiwi"  not in   fruits:
       print(" kiwi   is not ")


# access   item of list 

# indexing 
# negative  indexing 
# range  of indexes
# range   of negative indexes

print(fruits[2])

print(fruits[-1])


print(fruits[1:3])


print(fruits[-3:-1])










# fruits.remove("banana")
# fruits.pop()


# chaange   item in index 

# at an index 
# at range 



list =[12,3,4,7]
list[1] ="hello"
list[1:4] =" hello w21"
list[1:3]  =[21,21]


print(list)


# sorting a list 


list1 = [50,40,20,66,78]

# list1.sort()

# in reverse order 
# list1.sort(reverse=True)
list1.reverse()



print(list1)



# list  comprehession 

# when we make a list item from existing list 


# # travers a list by for loop 
# for i  in l:
#       if i >25
#       newlist.append(i)



# by list comprehension
# 
# 
# 
#  
list =[12,212,2,12,21,1,34]
new_list  = [ i for i in list if i >35]

print(new_list)


# copy a list 
new_list  = list.copy()
print(new_list)


new_list2  = list+ new_list


print(new_list2)


# nested list 
list5 =[10,203,404,[3232,323,323]]


list4= [32,21,21,4343]
list4.insert(2,[332,443])
print(list4[2][0])





# tuple  
'''

it store  multiple item in    a  variable 

colors =( 'blue','green','black')


ordered  (ordered  remain   same )
immutable (it's  value does not change )
dublicate allowed 
any data  type 
mix  of different data type 


creating a tuple 




'''






colours  = ('red','orange','yellow','green')



# creating  tuple of i item 
# fruit = ('apple')  it is  not tuple 
# now   it's data type is string 

# to make tuple 
# fruit  = ('apple',)  now it is  tuple 



fruits3  =  tuple("apple")
#  in this   case  it is tiple  not string 

fruit4 = tuple(("apple"))


print(colours[1])

print(colours[-1])

print(colours[1:3])

print(colours[-2:])
# (this is negative range indxing )
# 
# 
# 
# there is  no ending point 



# check if item exist in tuple 
if "green"  in colours:
      print("green is part of tuple")



# if  traverse 
for i    in colours:
      print(i)

more_colours = ("blue","violet")

colorus = colours+more_colours
print(colorus)


# # unpacking a tuple 
# # to put value of tuple in diffentr variable 
# colour1,colour2,colour3  = colours

# print(colour1,colour3,colour2)


# use of tuple 

# it is faster  then  list 
# list mutable where as  tuple is immutable 
# in tuple immutable  elememnt can be  used a s a key for dictionary 






# dictionary 
# create  a dictionary
# 
# 

numbers = {
      


      "jhon":3123,
      "riya":31231,
      "joy":14555
} 



# items
'''
ordered
unindexed

changable 

dublicate not allowed
any data type 



'''



# length of    dictionary 

phones = {
      

      "jhon":1212234234,
      "riya":123412312312,
      "joy":534634634
}


print(type(phones))




# k length 
print(len(phones))

# to access item in dictionary 
# print(/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////)



print(phones.get("jhon"))


# to print all keys 
print(phones.keys())


# update value in dict .

phones["jhone"]   ="  31221321"
print(phones)  

# add ietem 
phones['kia']  ="31232"
print(phones)


# add  anothe dict 
more_phones = {
      

      "kia":312312312312
}


phones.update(more_phones)

print(phones)


# to remove  element 
phones.pop("jhon")
print(phones)


phones.clear()

print(phones)


phones   = {
      


      "Area1"  :{
            

            "x":0,
            "y":1,
            "z":2
      },
      "Area2" :{
            

            "a":3,
            "b":4,
            "c":5
      }
}




print(phones["Area1"]["y"])



# function in python 


# def   fucntion_name  (parameter) :
#        #statement
#        Regular expression 


def   sum(n1,n2):
      ans = n1+n2
      return ans



# argument are value which we passed as a input  to the  function
# 
# 
# 
#  
# 
#   


a=5
b=6
ans =  sum(a,b)
print(ans)


def printHello():
    #   not passing any parameter  to this  function 
    print(" hello   world")



printHello()

def add(n1,n2=0):
      sum =n1+n2
      return sum
x =3
y=6
print(add(x,y))


# //
# position args 
print(add(1,3))



# keyword args   args pass by name 
print(add(n1=3,n2=56))


# default  agrs 
print(add(3))


# arbitary args (variable -length argumenet *args and ** kwargs)


# def addall (*args):
    #   all  args taken as tuple 
    # arhs ->tuple 


def  addall(*args):
    sum =0
    for i in args:
        sum+=i
    return sum 


ot =  addall(2,21,3232132,44)
print(ot)





# **kwargs  -> it used for key value pair .

def studentInfo(**kwargs):
     for x, y in kwargs.items():
          print(x,"is",y)


studentInfo(name="urvi",age=2,city="delhi")
studentInfo(name="ramesha",age=2,city="delhi")



# # recursive function 
# n! = n*n-1*n-2......n-1
# (n-1)! =n-1*n-2*....1
      # n!= n*(n-1)!

# # recursive  function -> function call itself 
# def recurse():
     
#      recurse()

# recurse()

   
# factoiral  of 0  is 1 
# o! =1





# string 

# sequnce of character 
# " "  or   ' '   or '''  '''


# immutable   it   can create a new string by manupulating  original string 


name1   ='college wala '

name2  ="college  new technology"

name3 = '''      mbs wala '''


print(name1,name2,name3)
print(type(name1))


# multi line string 
# array  like indexing 
# indxing   start   by 0 
text  ="Hello, world"
print(text[0])



# text= ""



# text="hello world"







