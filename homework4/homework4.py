fav_foods = ["caprese", "caprese sandwich", "pad thai", "chow mein", "cucumber roll"]
print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("escargot")
fav_foods.insert(0,"apple")
fav_foods.remove(fav_foods[2]) 
#I originally put fav_foods.remove(2)
#I got "ValueError: list.remove(x): x not in list" 
#I fixed this by putting the number as an index in the list instead of on its own
print(len(fav_foods))
for i in fav_foods:
    print(i.upper())
first_and_last = fav_foods[::len(fav_foods)-1] 
print(first_and_last)
if "potato" in fav_foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(0,21)) 
#I first tried to cast the range as an int using int(range(0,21)) 
#This gave the error "TypeError: int() argument must be a string, a bytes-like object or a number, not 'range'" 
#I fixed this by just casting as a list.
def get_first_15(numbers):
    return numbers[0:15]
def get_every_5th(lst):
    return get_first_15(lst)[::5]
#I accidentally put return get_every_5th(lst)[::5]
#This called the function inside of itself, recurring infinitely "RecursionError: maximum recursion depth exceeded"
#I put what I originally meant to, get_first_15, instead and it worked properly
def reverse_and_stride(lst):
    reverse = get_every_5th(lst)[::-1]
    return reverse[::3]


numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])
def sum_nested(nested):
    sum = 0
    for row in nested:
        for item in row:
            sum += item
    return sum
print (sum_nested(numbers))
def five_by_five():
    result = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        result.append(row)
    return result
nested25 = five_by_five()

def replace_3s(nested):
    result = []
    for i in nested:
        temp_row = []
        for j in i:
            if j % 3 == 0:
                temp_row.append("?")
            else:
                temp_row.append(j)
        result.append(temp_row)
    return(result)
nested25_with_questions = replace_3s(nested25)

def sum_non_questions(nested):
    sum = 0
    for i in nested:
        for j in i:
            if j != "?":
                sum += j
    return sum
summed25_non_questions = sum_non_questions(nested25_with_questions)

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
ages.pop("Mariam")
for name in ages:
    print(name,ages[name])

#My favorite was 3.4 1's replace_3s which replaced all multiples of 3 in a nested list with "?"
nested25 = five_by_five() #nested list with 5 rows of nums from 1-25
print(replace_3s(nested25))