def say_goodbye(name):
	print("Goodbye,", name)

def circle_area(radius):
	#Area = pi*radius^2
	pi = 3.14
	print(pi*radius**2)

def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b

def temp_extremes(readings):
	minimum = min(readings)
	maximum = max(readings)
	return (minimum,maximum)

def weekend(day):
	#only days 6 and 7, sat and sun, are weekends. thought it'd be fun to do in 1 line.
	return day >= 6

def fuel_efficiency(distance, fuel_quantity):
	return distance/fuel_quantity

def encrypt(num):
	last_digit = num%10
	first_digits = num//10
	return(int(str(last_digit) + str(first_digits))) #is there a better way to concatenate numbers?

def exponent(a,b):
	result = a
	for i in range(b-1):
		result *= a
	return result

def minimum_for(nums):
	lowest = nums[0]
	for i in nums:
		if i < lowest:
			lowest = i
	return lowest
def maximum_for(nums):
	highest = nums[0]
	for i in nums:
		if i > highest:
			highest = i
	return highest

def minimum_while(nums):
	lowest = nums[0]
	i = 0
	while i < len(nums):
		if nums[i] < lowest:
			lowest = nums[i]
		i += 1
	return lowest
def maximum_while(nums):
	highest = nums[0]
	i = 0
	while i < len(nums):
		if nums[i] > highest:
			highest = nums[i]
		i += 1
	return highest

def sum_digits(num):
	string_num = str(num)
	sum = 0
	for i in string_num:
		sum += int(i)
	return sum

x = 1234567890
result = sum_digits(x) #adds the individual digits of a number together
print(f"The result of Calculate the Sum (6.3) with x = {x} is {result}")