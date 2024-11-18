print('hello')
print("hello") #you can print a string using either double quotes or single quotes
a='hello'
b='there'
print(a+" "+b)#the + operator is used to combine strings & the "" are used to create a whitespace
word="HELLO"
print(word*5) #the * operator will print the reapetedly(5times in this example)

#the len() function is a built in function that returns the length of an object
george_length=len("george")
print(george_length)

#type function is a built in function that returns data type/class of an object
print(type(64)) #<class 'int'>
print(type("64")) #<class 'str'>
print(type(64.90)) #<class 'float'>

#format() method
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
print("Mohammed has {} balloons".format(27))
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))

#F-String Formatting
name = "John"
print(f"Hello {name}")
a = 5
b = 3
print(f"The sum of {a} and {b} is {a+b}")
#split() method
  #The syntax for the split method is: string.split(sep, maxsplit)
  #The split method has two arguments (sep and maxsplit). The sep argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). If the sep argument is not provided, the default separator is whitespace.
  #True to its name, the maxsplit argument provides the maximum number of splits. The argument gives maxsplit + 1 number of elements in the new list, with the remaining string being returned as the last element in the list. You can read more about these methods in the Python documentation too.
new_str = "The cow jumped over the moon."
new_str.split()

# Exponentiation operator**(power operator)
n = int(input())
for i in range(n):
    print(i ** 2)  # Print the square of each integer
