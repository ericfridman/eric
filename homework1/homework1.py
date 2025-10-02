# --- Variables and Data Types ---
a = 10
print(a)
print(type(a))
#a is an int, a whole number with no decimals
b = 1.5
print(b)
print(type(b))
#b is a float, a number with decimals
c = 3j
print(c)
print(type(c))
#c is a complex variable, j is used as i in math, to show a complex number
d = "hello"
print(d)
print(type(d))
#d is a string, a sequence of characters contained in quotes ""
e = [1,2,3]
print(e)
print(type(e))
#e is a list, an ordered, mutable collection of items, can be different data types.
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
#f is a dictionary, an unordered collection of key-valued pairs. Keys are unique and immutible
g = (1, 2)
print(g)
print(type(g))
#g is a tuple, an ordered immutible collection of items, a list you can't change later.
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
#h is a list again, now with strings instead of ints.
i = True
print(i)
print(type(i))
#i is a boolean, which can either be True or False
j = None
print(j)
print(type(j))
#j is a NoneType variable, which can only be None and holds no meaningful data.
k = [True, "blue", 12]
print(k)
print(type(k))
#k is another list, now with a bool, str, and int.
l = str(14)
print(l)
print(type(l))
#l is a string, originally an int cast using str()
m = 1e4
print(m)
print(type(m))
#m is a float, with the e functioning similarly to how it does on a calculator

# 1. How many different data types did you find?
# I found 9 different data types.

# 2. List all the data types you found.
# integer, float, complex, string, list, dictionary, tuple, boolean, NoneType
# 3. What variables have the same data types?
# The variables b and m are both floats, d and l are both strings, e, h, and k are all lists.
# 4. What was the data type of l? Why is it not an integer? What does str() do?
# l is a string, the str() function turns the enclosed value into a string
# 5. Look up one more data type not given above. Repeat the same procedure.
n = {1, 2, 3, 3, 4}
print(n)
print(type(n))
#n is a set, an unordered collection of unique items. it only stores each value once, no repeats.

# --- Booleans ---
print(10 > 9) #True, 10 > 9
print(10 == 9) #False, 10 != 9
print(10 <= 9) #False, 10 !<= 9
print(bool("abc")) #True, just because?
print(bool(123)) #True, why not
print(bool(["apple", "cherry", "banana"])) #True, same as previous two, maybe just having a value? 
print(bool(True)) #True, duh
print(bool(False)) #False, duh
print(bool(0)) #False, makes sense 0 not 1
print(bool("")) #False, confirms my guess, no value
print(bool(" ")) #True, space is a value
print(bool(())) #False, no value
print(bool([])) #False, no value
print(bool({})) #False, no value
print(bool(True and False)) #False, needs to be both for and
print(bool(True and True)) #True, both True
print(bool(False and False)) #False, both false
print(bool(True or False)) #True, just need one
print(bool(True or True)) #True, double True
print(bool(False or False)) #False, neither True
print(bool(not(False))) #True, not False is True
print(bool(not(True))) #False, not True is False

#What pattern do you notice about expressions returning True or False?
#Anything with a value is True, anything that's no value is False
#Which expression surprised you about its result?
#bool(" ") returning True, but a space is something which makes sense.
#Create an expression, not given above, that will return True. Why is it True?
print(bool(not (False and True)))
#Returns True because not gives the opposite value of False and True, which is False
#Create an expression, not given above, that will return False. Why is it False?
print(bool(not(not (False and True))))
#Returns False because not not True is False, opposite of previous expression

# --- Operators ---
print(10 + 5) #15, adds
print(10 - 5) #5, subtracts
print(2 * 4) #8, multiplies
print(6 / 3) #2.0, divides
print(5 % 2) #1, modulus (remainder)
print(3 ** 2) #9, exponent, raises 3^2
print(15 // 2) #7, rounded down division

print(5 == 2) #False, compares if equal
print(10 != 10) #False, compares if not equal
print(2 < 5) #True, compares if less than
print(12 > 5) #True, compares if greater than
print(5 <= 6) #True, compares if less than or equal to
print(1 >= 10) #False, compares if greater than or equal to

x = 5
print(x)
x += 5 #adds 5
print(x)
x -= 4 #subtracts 4
print(x)
x *= 3 #multiplies by 3
print(x)

#1. What does the operator and do? Write an expression that results in True. Write an expression that results in False.
# The "and" operator returns True if both conditions are true.
print(True and True)
print(True and False)
#2. What does the operator or do? Write an expression that results in True. Write an expression that results in False.
# The "or" operator returns True if either condition is true.
print(True or False)
print(False or False)
#3. What does the operator not do? Write an expression that results in True. Write an expression that results in False.
# The "not" operator returns True if False and False if True
print(not(False))
print(not(True))

#1. What is the difference between / and //?
# / divides two numbers, returning a float with a decimal. // divides but rounds down, returning an int.
#2. What is the difference between % and //?
# % gives a mod, the remainder after division, and // performs regular division and rounds down.
#3. What operator would you use to calculate the remainder when dividing two numbers? Give an example.
# To calculate the remainder when dividing two numbers I would use %, 
# for example 3%2 would return 1, the remainder of 3/2.
#4. How do assignment operators work?
# Assignment operators change the value of a variable, so x+=2 would add 2 to x, while x-=2 would subtract 2.

# --- Strings ---
my_string = "Hello"
print(my_string) #prints the string as-is
print(my_string[0]) #prints the first character
print(my_string[1]) #prints the second character
print(my_string[2]) #prints the third character
print(my_string[3]) #prints the fourth character
print(my_string[4]) #prints the fifth character
print(my_string[-1]) #prints the fifth (last?) character
print(my_string[1:3]) #prints the second and third characters
print(my_string[0:5:2]) #prints the first, third, and fifth character
print(len(my_string)) #prints the length of the string (5)
print(my_string+"goodbye") #prints the two strings together, Hellogoodbye
print(my_string*7) #prints the string 7 times end to end

#1. Define the term slicing. For which of the manipulations did you slice your string?
# Slicing is calling certain slices of a string, using :. [start:end:step]
# Sliced for [1:3] (second until fourth, not inclusive for end, step defaults to 1) 
# and [0:5:2] start to finish, step of 2
#2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
# Returned "Hello, my name is Oski"
#3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
# Returned "Hello, my name is Oski"
#4. What is the difference between the two last print statements?
#   Hint: Look up f-strings.
# The second example is an f-string, which allows you to use {} inside a string to input variables or evauluate expressions. 
# The first uses a comma to seperate arguments, which prints automatically joined with a space.

# --- Terminal Commands ---
#1. cd
# Changes directories
# Ex: cd Desktop
#2. ls
# Lists contents of selected directory
# Ex: ls
#3. ls -a
# Lists contents of selected directory, includes hidden files
# Ex: ls -a
#4. mkdir
# Makes a new directory, folder
# Ex: mkdir homework1
#5. cat
# Displays the contents of a file
# Ex: cat notes.txt
#6. pwd
# Prints working directory, shows where you are
# Ex: pwd
#7. cd ..
# Moves one directory up, to parent folder
# Ex: cd ..
#8. cd .
# Stays in current directory
# Ex: cd .
#9. cd ∼
# Moves to home directory
# Ex: cd ~
#10. cp
# Makes a copy of file or directory
# Ex: cp notes.txt notes2.txt
#11. mv
# Moves or renames files
# mv notes2.txt notes3.txt
#12. rm
# Removes/deletes files
# Ex: rm notes.txt
#13. clear
# Wipes the terminal screen
# clear
#14. grep
# Searches for patterns inside files
# grep "Hello" notes.txt

#1. Look up 3 other commands not present. Define and explain how to use them on the command line.
# touch
# Creates an empty file if one doesn't exist
# Ex: touch notes.txt
# man
# Shows the manual for a given command
# Ex: man ls
# echo
# Prints to the terminal
# Ex: echo "Hello"
#2. What is the difference between ls and ls -a?
# ls only lists the visible files in a directory, while ls -a includes hidden files
#3. What is a hidden file?
# A hidden file is a file that beggins with a . making them invisible to commands like ls, but still accessible
#4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line.
# ls -l gives a longer listing, showing more information
# rm -r removes a directory and its contents
# grep -i is case-insensitive in its search
# Each of these can be used just like their original forms, just with the addition of the flag.