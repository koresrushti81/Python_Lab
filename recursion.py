# def fun(a):
#     print(a,end=" ")
#     if a==10:
#         return #if we write print then it exclude 10
#     fun(a+1)
# fun(1)

# a=1
# def fun ():
#     global a
#     print (a)
#     if a==10:
#         return 
#     a=a+1
#     fun()
# fun()

    #top down Approach

# def printData(i):
#     if i==11:
#         return
#     print (i)
#     printData(i+1)
# printData(1)

    # Bottom up Approach
# def printdata(i):
#     if i==0:
#         return
#     printdata(i-1)
#     print(i,end=" ")
# printdata(10)

   #factorial
#top down 
# def fact(x):
#     if x==1 or x==0:
#         return 1
#     else:
#         return x*fact(x-1)

# print(fact (5))
    
    # bottom up
#1} def fact(n, i=1):
#     if i > n:           
#         return 1
#     return i * fact (n, i + 1)

# print(fact (5))

# def fact(n,i=1,ans=1):
#     if i==5:
#         return (ans*i)
#     return(fact(n,i+1,ans*i))
# print(fact(5))

 


    