import random

# a = "Hello how are you"
# #how
# #you
# #Hello

# print(a[6:9:1])
# print(a[14:17:1])
# print(a[0:6:1])

# a="23"
# a= int(a)
# b=float(a)
# print(type(a))
# print(b)
# print(type(b))

# a=10
# print(a/2)
# print(type(a/2))

# name = "Sarvadnya"
# age = 17.4

# print(f"My name is {name} and my age is {age}")
# print("My name is",name,"and my age is",age)

# age = int(input("Enter your age:-"))
# print(f"Your age is: {age}")
# print(type(age))

# age = int(input("Enter your age:-"))
# if age>=18:print("You are eligible to vote.")
# else :print("Your are not eligibile to vote.")


#1.
"""
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
if n1>n2:
    print(f"{n1} is greater")
else:print(f"{n2} is greater")
"""

#2.
"""
gen = input("Enter your Gender(M/F):-")
if gen == "M":
    print("Good Morning Sir")
elif gen == "F":
    print("Good Morning Ma'am")
else:
    print("Please enter valid gender type.")
"""

#3.
"""num = int(input("Enter the number:-"))
if num%2==0:print(f"{num} is even")
else:print(f"{num} is odd")"""

#4.
"""name = input("Enter your name:-")
age = int(input("Enter your age:-"))
if age>=18 :
    print(f"Hello {name}, you are valid voter")
else:
    print(f"Hello {name}, you are not valid voter")"""

#5.
"""year = int(input("Enter the year:-"))
if year%400 == 0 and year%100==0: 
    print(f"{year} is a leap year")
elif year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else : print(f"{year} is not leap year")"""

#6.
"""temp = int(input("Enter temperature:-"))
if temp<=0:
    print("Freezing Cold")
elif 0<temp<=15:print("Cool nature")
elif 15<temp<=25:print("Pleasant")
else : print("Very hot")"""

"""for i in range(5,51,5):
    print(i)"""

"""n = int(input("Enter the number:-"))
for i in range(n,n*10+1,n):
    print(i)"""

#1.
"""n=int(input("Enter number:-"))
for i in range(n):
    print("Hello world")"""

#2.
"""n=int(input("Enter number:-"))
for i in range(1,n+1):
    print(i)"""

#3.
"""n=int(input("Enter number:-"))
for i in range(n,0,-1):
    print(i)"""

#4.
"""n=int(input("Enter number:-"))
for i in range(1,11):
    print(f"{n} * {i} = {i*n}")"""

#5.
"""a=0
n=int(input("Enter number:-"))
for i in range(1,n+1):
    a=a+i
print(f"Sum = {a}")"""

#6.
"""a=1
n=int(input("Enter number:-"))
for i in range(1,n+1):
    a=a*i
print(f"{n}! = {a}")    """

#7.
"""n=int(input("Sum will start from "))
m=int(input("to "))

oddsum=0
evensum=0

for i in range(n,m+1,2):
    oddsum = oddsum + i
print(f"Oddsum = {oddsum}")
for j in range(n-1,m+1,2):
    evensum = evensum + j
print(f"Evensum = {evensum}")"""

#8.
"""n=int(input("Enter the number:-"))
for i in range(1,n+1):
    if n%i==0:print(i)"""

#9.
"""n=int(input("Enter the number:-"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:print(f"{n} is perfect number") 
else : print(f"{n} is not perfect number")"""

#10.
"""n=int(input("Enter your number:-"))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count + 1
if count == 2:
            print(f"{n} is prime number")
else : print(f"{n} is composite number")"""

#11.
"""str = input("Enter the word:-")
a=str[::-1]
print(a)"""

#12.
"""str = input("Enter the word:-")
a=str[::-1]
if str==a:
    print(f"{str} is a palindrome")
else : print(f"{str} is not a palindrome")"""

#13.
"""str=input("Enter the word:-")
char=0
dig=0
spe=0

for i in str:
    if i.isdigit():
        dig=dig+1
    elif i.isalpha():
        char = char+1
    else : spe = spe + 1

print("Character = ",char,'Digits = ',dig,'Special characters = ',spe)"""

#While loop
#1.
"""n= int(input("Enter the number"))
while n!=0:
    print(n%10)
    n = n//10"""

#2.
"""n=int(input("Enter the number:-"))
rev = 0
while n!=0:
    rev = rev * 10 + n % 10
    n=n//10

print(rev)"""

#3.
"""n=int(input("Enter the number:-"))
a=n
rev = 0
while a!=0:
    rev = rev * 10 + a % 10
    a=a//10
if rev==n:
    print(f"{n} is palindrome")
else : print(f"{n} is not palindrome")"""

#Data structure
#List
"""
List is type of Data structure used to store multiple values in a single variable.
Lists are mutable.
Lists support heterogeneous data.
List can be traversed by two ways:-
    1.Via Index using for loop
    2.Direct traversal
"""

# print(dir(list))
"""
list = [3,4,52,6,2,6]
list.append(34)
list.insert(2,23)
list.pop(-2)
list.sort()
list.reverse()
list.remove(4)
print(list)"""

#1.
"""l = [53,-1,46,-64,6546,-546,-5556,-5,9]
pos = []
neg = []

for i in l:
    if i>=0:
        pos.append(i)
    else :
        neg.append(i)

print(f"Positive = {pos}")
print(f"Negative = {neg}")"""

# 2.
"""l = [4, 8, 2, 9, 1]
sum = 0
for i in l:
    sum += i 
avg = sum/len(l)
print(avg)"""

#3.
"""l = [4, 8, 2, 9, 1]
large = l[0]
index = 0
for i in range(len(l)):
    if l[i] > large:
        large = l[i]
        index = i
print(f"Greatest = {large} at index {index}")"""

#4.
"""l = [4, 8, 2, 9, 1]
copy = l
large = copy[0]
for i in copy:
    if i > large:
        large = i
index = copy.index(large)
copy.pop(index)
selarge = copy[0]
for i in copy:
    if i > selarge:
        selarge = i
print(f"Second Greatest = {selarge}")"""

"""l = [4, 8, 2, 9, 1]
large = l[0]
sec_large = l[0]

for i in l:
    if i > large:
        sec_large = large
        large = i
print(f"Second greatest = {sec_large}")"""

#4.
"""l=[1,3,4,5,7,12,53]
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        print("Your list is not sorted")
        break
else: print("Your list is sorted")"""

#Tuple
"""
Tuple is type of Data structure also used to store different kinds of data.
Tuple is immutable.
Tuple is defined using parenthesis ().
Tuple are unpacked so that we can access values directly.
"""

"""tuple = (23,"aslkd",234) #default form to define tuple
tup = 23,"aslkd",234 #can be define without parenthesis"""

"""a = ["monday", "tuesday", 34, 55]
tup =  tuple(a)
print(type(tup))"""

"""def tup():
    return "Sarvadnya", 17, "sarvadnya.yeole@mail.com"
info =tup()
name, age,email = info
print(name)
print(age)"""

#Tuple methods
"""
tuple.index(elem) --shows index of elem
tuple.count(elem) --counts how many times elem occur in tuple
"""

#Set
"""
Set stores only unique values.
Set automatically removes duplicates and has no guaranteed order.
Set is immutable.
"""
#Set Operations
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union          → {1,2,3,4,5,6}
a & b   # Intersection   → {3,4}
a - b   # Difference     → {1,2}
a ^ b   # Symmetric diff → {1,2,5,6}
"""
#Set Methods
"""set.add(elem) -- Adds an elem to set
set.clear()   -- Removes all the elements from the set
set.copy()    -- Returns copy of set

difference() --
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.difference(b) -- removes common element from the set
                -- a = {1,2}
b.difference(a) -- b = {5,6}
also written as 'a-b' and 'b-a'

difference_update() -- 
a.difference_update()

discard() -- Removes the specified item from set
intersection() '&' -- Returns set that is intersection of two other sets
intersection_update() '&=' -- Removes the items of set which are not present in other specified set
isdisjoint() -- Returns true if no items of set is present in another set
issubset() '<=' -- Returns true if all items of set is present in another set
           '<' -- for larger set
issuperset() '>=' -- Returns true if all items of another set is present in set
             '>' -- for smaller set
pop() -- Removes random element of set
remove() -- Removes specified element
symmetric_difference() '^' -- Returns set with symmetric differences of two sets in other words it removes common elements and return uncommon elements of both sets in a single set
ymmetric_difference_update() '^=' -- Inserts the symmetric differences from set to another
union() '|' -- Return set containing union of sets
update() '|=' -- Update the set with union of set and other
"""

#Dictionary
"""
A dictionary stores data as key: value pairs

d = {32:23,30:200,40:400}
d[50] = 500 -- creating a new key value pair
d[32] = 100 -- updating a key value that already exist
"""

#Dictionary Methods
"""
d={10:290,20:345,30:343}
d.clear() -- Removes all the elements from the set
d.copy() -- Returns copy of dictionary
d.fromkeys() -- Returns dictionary with the specified keys and values
             -- q=d.fromkeys([12, 20, 23],234)  q={12:234, 20: 234, 23:234}
d.get() -- Returs the value of specified keys and value
d.items() -- Returns a list containing a tuple for each key value pair 
          -- dict_items([(10, 290), (20, 345), (30, 343)])
d.keys() -- Returns the list containing dictionary's keys
         -- dict_keys([10, 20, 30])
d.pop() -- Removes the element with specified key
d.popitem() -- Removes the last inserted key-value pair
d.setdefault() -- Returns value of specified key, if key doesn't exist insert the key with specified value
               -- d.setdefault(60:23432) 
               -- d = {10:290,20:345,30:343,60:23432}
d.update() -- Update the dictionary with specified key-value pair
           -- d.update({10:330}) == d = {10:330,20:345,30:343}
           -- d.update({55:234}) == d = {10:290,20:345,30:343,55:234}
d.values() -- Return a list of all values in the dictionary
"""

#Traversing of Dictionary (loops)
"""
d = {10:100,20:200,30:300,40:400}
for i in d:
    print(f"key {i} : value {d[i]}")
"""

#1.
"""
d1 = {'a':10,'b':20,'c':30}
d2 = {'d':40,'f':50,'e':60}

for i in d2:
    d1[i] = d2[i]

print(d1)
"""

#2.
"""
d = {"a":10,"b":20,"c":30}
sum = 0
for i in d:
    sum += d[i]

print(sum)
"""

#3.
"""
l = ['a','b','a','c','b','a']
d = {}
for i in l:
    if i in d.keys():
        d[i]+=1
    else:d[i]=1
print(d)
"""

#4.
"""
d1={"a":5,"b":3}
d2={"b":4,"c":2}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)
"""