# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     print(a+b+c)
# add(2,4,9)

# def add (a,b,c=None):
#     if c or c==0:
#         print ("Sum of three numbers:",a+b+c)
#     else:
#         print("Sum of two numbers:",a+b)
# add(3,7)

# keywords only argument
# def add (a,b):
#     print("A is :",a)
#     print("b is :",b)
# add(4,6)
# add(a=4,b=6)

# def add (*,a,b):
#     print("A is :",a)
#     print("b is :",b)
# add(b=4,a=6) #parameter name compulsary 

# def add (*,a=None,b):#for 1 default value (None)-->* otherwise remaining parameter should be None
#     print("A is :",a)
#     print("b is :",b)
# add(b=6)

# variable argument (variable length of argument)
# def fun(*a):
#     print (a)# returns in the form of tuple
#     print(a[0],a[1])
# fun(2,4,6,8,9)

#pass value to x, y and a
# def fun(x,y,*a):
#     print(x,y)
#     print (a)# returns in the form of tuple
#     print(a[0],a[1])
# fun(2,4,6,8,9)

#tuple
# x=(2,3,5)
# print(x)
# print(type(x))

#tuple packing 
# a,b,c=2,4,6
# print (a)
# print(b)
# print(c)
# print(a,b,c)

# p,q,*r=(2,43,45,6,7,8,8,9,45)
# print(p)
# print(q)
# print(*r)

#variable key word argument
# def fun(**x):
#     print(x)
#     print(x['a'])
#     print(x['b'])
#     print(x['c'])
# fun(a=1,b=3,c=4)

#positional only argument
# def fun(a,/,b):
#     print(a,b)
# fun(2,b=4)#after / we can give parameter name but not before

#helper function -->function inside function is called helper function
# def outer():
#     print("This is outer function")
#     def inner():
#         print("This is inner function")
#     inner()
#     inner()
# outer()
# outer()
  
#filter
# li=[2,4,6,8,9]
# for i in li:
#     if i%2==0:
#         print(i,end=' ')

# def isEven (n):
#     if n%2==0:
#         return n
# li=[24,2,7,6,4]
# ans =list(filter(isEven,li))
# print(ans)

#function annotation or type hints
# def sum (a:int ,b:int)->int:
#     return (a+b)
# print(sum(3,4))
# print(sum.__annotations__)

#Anonymous function --> lambda function
#square is a variable name it is not a function name 

# square =lambda x:x*x
# print(square(5))

# li=['2','3','amit','8']
# def toInt(n):
#     try:
#         return(int(n))
#     except:
#         return 0
    
# d= list(filter(toInt,li))
# print(d)

# li=[1,2,3,4,5,6,7]
# def isEven(n):
#     if(n%2==0):
#         return True # names
#     else:
#         return False # 0,0.0,none ,null
# data=list(filter(isEven,li))
# print(data)

# li=['3','4','6','8','9','1','2']
# def toInt(n):
#     return(int(n))
# data=[]
# for i in li:
#     data.append(toInt(i))
# print(data)
    
# li=['3','4','6','8','9','1','2']
# data=[]
# for i in li:
#     x=(lambda i : int(i))(i)
#     data.append(x)
# print(data)

# no1=34
# no2=9
# print(no1 if no1>no2 else no2)

# max=lambda x,y: print (x if x>y else y)
# max(3,5)

# fun = lambda x:[i for i in range (1, x+1)]
# print(fun(5))

#higher order function
# def square (x):
#     return x*x
# def applyfunction(fun,value):
#     return fun(value)
# print(applyfunction(square ,5)

# def square (x):
#     return x*x
# def applyfunction (fun,v1,v2):
#     return (fun(v1)+fun(v2))
# print(applyfunction(square,5,3))

# li=[1,2,3,4,5,6]
# data=list(map(lambda x:x*x,li))
# print(data)

# li=["12","34","64","98"]
# def toInt(x):
#     return int (x)
# data=list(map(toInt,li))
# print(data)

# li=["12","34","64","98"]
# data=list(map(int,li))
# print(data)

# li=["srushti","chandrakant","kore"]
# data=li[0].upper()
# print(data)

# li=["srushti","chandrakant","kore"]
# def toupper(x):
#     return( x.upper())
# data=list(map(toupper,li))
# print(data)

# li=["srushti","chandrakant","kore"]
# data=list(map(lambda x:x.upper(),li))
# print(data)

# li1=[1,2,3]
# li2=[4,5,6,7,8,9]
# data=list(map(lambda x,y:  x+y  ,li1,li2))
# data.extend(li2[len(li1):])
# print(data)

# li=[1,2,3,4]
# data=list(map(lambda x:(x,x*x),li))
# print(data)

# data={'roll':95,'name':'Srushti'}
# print(data)

# for i in data:
#     print(i) # returns keys only

# for i in data:
#     print(data[i])# returns value

# for i in data:
#     print(i,":",data[i])

# for i,j in data.items():
#     print(i,j)

# for i in data.items():
#     print(i)

# for i in data.items():
#     print(i[0],":",i[1])

# d={'a':'1','b':'2'}
# print(d.items())
# d=list(map(lambda a: (a[0],int( a[1])),d.items()))
# print(d)

# data=[1,2,3,4,5]
# d=list(map(lambda x:x if x%2==0 else x*-1 ,data))
# print(d)

# li=["hello gaurav","i am from kolhapur","hii","bye bye"]
# print(li)
# d=list(map(lambda x:len(li[0]),li))
# print(d)