# so hello now here i am writing the program which were our assignmnet, so let us beagn 

# Question 1
# writing a program to perform basic arthematic operations 
number1 = int(input("enter a number please: "))
number2 = int(input("enter a number please: "))
# for addintion 
print(number1+ number2)
#for subtbertion
print(number1 - number2, number2 - number1)
#for multiplication
print(number1 * number2)
#for divsion 
print(number1 / number2, number2 - number1)

#Question 2
#a program to demostrate type conversions between int, flaot, str, bool
word1 = "hello"
word2 = 45
word3 = 45.99
word4 = True
# this is the typecasting what of each of the above
word2 = str(word2)
word3 = int(word3)
word4 = float(word4)
word1 = bool(word1)
# now this will be the result after we typecast all of the variable thus 
print(type(word1))
print(type(word2))
print(type(word3))
print(type(word4))

#Question 3
#implementing some of the following instrcution on the list thus 
list = [1,2,3,4,5,"harry", "zack"]
#append 
list.append(4)
print(list)

#sort
#list.sort()# sort funcion will do not work on this type of list as this one is the mixture of both string
print(list)#and int, type objects so for the working of this sort fucntion, the lsit should be universal only 
#like there should be only one tyoe eitgher it be string, float, integer, etc.
#thus making this operation as a comment as it will not run thus.

#insert 
list.insert(2,"hanz")
print(list)
#pop
list.pop()
print(list)
#reverse
list.reverse()
print(list)
#remove
list.remove
print(list)
#indexing 
print(list[0])
print(list[-1])
#slicing 
print(list[2:5])
print(list[:3])
print(list[4:])
# so these were all the example of what was asked from us and that is theindexing and slicing
#along with oter operations thus.

#Question 4
#implementing tuple cration and demonstration it's imutability
tuple = (1,2,3,"harsh")
print("original tuple",  tuple)
try:
    tuple[0] = 10
except TypeError:
    print("Tuples are immutable! You cannot change their elements.")

#Question 5
#writing a program to implement dictionaries and then #update key- value and iterating them through keys and values
dict = {"name": "harry", "age": 20}
#updating a value here and adding a new oen thus 
dict["age"] = 22
dict["city"] = "tokyo"
#now iterating them through keys and values then 
for key, value in dict.items():
    print(key, ":", value)

#Question 6
#implenting basic set operations such as union, intersection, and difference.
#now here we do this by making 2 sets 
set1 = {1,2,3,4,5}
set2 = {7,8,9,10,11}
#now performing set operations here
print("Union: ", set1 | set2)
print("Intersection: ", set1 & set2)
print("difference: ", set1- set2, set2 - set1)
# so this was our code for the follwoing program

#Question 7
string = input("enter a senatnce of your choice: ").lower()
#we wrote lower in the input line coz it converts the whole strinbg to lowercase immediately 
#it makes it easy to run the program and we don't need to check this for both lower and upper case thus.
vowels = "aeiou"
count = sum(1 for ch in string if ch in vowels)
print("vowel count: ", count)
#checking prime here
number = int(input("enter a number: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
        if is_prime:
            print(number, "is prime")
        else:
            print(number, "is not prime")
#now finding factorial using for loop 
fact = 1 ## Starting with 1 (because multiplying by 0 would make everything 0)
for i in range(1, number + 1): # Loop from 1 up to n (inclusive)
    fact *= i  #multiply fact by i each time 
    print("factorial(loop): ", fact) #printing the fianl factorial value here 
# factoriual using recursion 
def factorial(x): # we are taking the base case here where factorial is either 0 or 1, factorial is 1.
    return 1 if x <= 1 else x * factorial(x- 1)
print("factorial(recursion):", factorial (number))
# here in this final step, we are calling the fucntion and then printing the final result.
# here is the qucik idea = loop method = it goes step by step multiplying from 1 to n.
# recursion = breaks the peoblems into smaller version of itself until it reaches 1.

#Question 8
# defining the function firstly
def add(a, b):
    return  a + b # returning the sum here 
# calling the function 
result = add( 18, 79)
print("sum: ", result)

