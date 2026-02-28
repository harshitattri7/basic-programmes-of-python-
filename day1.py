print("python")

#datatypes
# integer---->10,20
# String---->"name","10"
# float------>2.5
# complex------>


# a=2
# b="python"
# print('a')
# print(b)


# d=type(a)
# print(d)


# print(type(b))
#type casting
# a=2
# b=float(a)
# print(b)
# print(type(b))


# a=2.2
# b=int(a)
# print(b)
# print(type(b))

# a=2
# b=str(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# print(a+2)
# print(b+2)



# a=input("enter you name: ")
# print(a)


# a=input("enter any number")
# print(a)
# print(type(a))
# print(a+2)


# a=int(input("enter number"))
# print(type(a))
# print(a+2)

#print("harshit attri")
#print(type)

# a=245235
# b=("54814534")
# print(a)
# print(b)
# print(type(a))
# print (type(b))

# d=float(b)

# ADD=a+d
# print(ADD)

# NEW=int(input("enter your age :"))
# new1=int(input("entere your mothers age : "))
# total=(NEW+new1)
# print(total)
# print(type(total))



# operators
# comparison op-- <,>,<=,>=,==,!=
# arithmetic op-- +,-,*,/,%,**
# logical op-- and,or
# assignment op-- =,a=a+b(a+=b),a=a-b(a-=b)

# and-
# true+true-True
# true+false-False
# false+false-False

# or-
# true+true-True
# true+false-True
# false+false-false

# a=2
# b=8
# print(b>a)


# a=2
# b=3
# c=3
# print(a>b or b==c)

#a=1
#b=1
#print(a)
#a=a+b
#print(a)


#a=float(input("enter your age : "))
#b=float(input("enter your brothers age :"))
#print(a<b and a==b)


#t=float(input("enter a smaller number : "))
#v=float(input("enter greater number : "))
#print(t<v)



# t=float(input("enter a first number : "))
# v=float(input("enter second number : "))
# print(t>0 or v>0)


# k=0
# i="admin"
# g=0
# while k<3:
#     a=(input("enter username :"))
#     if a==i:
#      print("correct usernme ")
#      g=g+1
#      break
#     else:
#      print("try again",3-k,"attempt left")
#      k=k+1

# #password
# if g==1:
  
#     k=0   
#     j=123

#     while k<3:
#         b=int(input("enter password"))
#         if b==j:
#          print("correct password")
#         else:
#          print("wrong password, try again",3-k,"attempt left")
#         k=k+1

#calculator
# a=int(input("enter first no. : "))
# b=int(input("enter second number : "))
# s=input("enter operation +,-,*,/ : ")

# if s=="+":
#     print(a+b)
# elif s=="-":
#     print(a-b)
# elif s=='*':
#     print(a*b)
# else:
#     print(a/b)


# a=1000
# print("1. deposit")
# print("2. withdrawl")
# print("3. check bank balance")
# print("4. exit")
# while True:
#     s = int(input("enter your choice : "))
#     if s==4:
#         break
#     elif s==1:
#         g=int(input("enter teh amount : "))
#         a=a+g
#         print(a)
#     elif s==2:
#         if a<=0:
#          print("insufficient balance!!!")
#         else:
#          k=int(input("enter teh amount : "))
#          a=a-k
#          print(a)
#     elif s==3:
#         print(a)
#     else:
#         print("wrong choice")


# 


# 

# 


# a=5000
# def dep(a):
#     b=int(input("enter the amount : "))
#     a=a+b
#     print(a)

# def wid(a):
#  b=int(input("enter the amount : "))
#  if b>a:
#     print("insufficient balance")
#     a=a-b
#     print(a)

# def bal(a):
#     print(a)



# o="admin"
# r=123
# while True:
#     u=input("enter the username : ")
#     p=int(input("enter the password : "))
    
#     if o==u and r==p:
#         print("you are logged in!")
#     else:
#         print("try again!")
#         break



#     print(" 1. deposit")
#     print(" 2. withdrawl")
#     print(" 3. balance")
        
#     while True:
#        c=int(input("enter choice : "))
    
       
#        if c==1:
#           dep(a)
#        elif c==2:
#           wid(a)
#        elif c==3:
#           bal(a)
        



class cal():
    def add(self):
        self.fn=int(input("enter first number : "))
        self.sn=int(input("enter the second number : "))
        self.plus=self.fn+self.sn
        print(self.plus)

    def sub(self):
        self.fn=int(input("enter first number : "))
        self.sn=int(input("enter the second number : "))
        self.minus=self.fn-self.sn
        print(self.minus)

    def mul(self):
        self.fn=int(input("enter first number : "))
        self.sn=int(input("enter the second number : "))
        self.mul=self.fn*self.sn
        print(self.mul)


    def div(self):
        self.fn=int(input("enter first number : "))
        self.sn=int(input("enter the second number : "))
        self.div=self.fn/self.sn
        print(self.div)

obj=cal()

while True:
    
    print(" 1. add")
    print(" 2. subtract")
    print(" 3. multiplication")
    print(" 4. division")
    print(" 5. exit")

    t=int(input("enter the choice : "))

    if t==1:
        obj.add()
    elif t==2:
        obj.sub()
    elif t==3:
        obj.mul()
    elif t==4:
        obj.div()
    elif t==5:
        print("exit..")
        break
    else:
        print("invalid choice")