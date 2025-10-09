# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(text):
    vowels = 0
    consonants = 0
    for i in text:
        if i.isalpha(): #opted to not count y because it scares me
            if i in "aeiouAEIOU": #i originally had a bunch of or statements, did some googling and this is way prettier
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(text):
    total_vowels = 0
    total_consonants = 0
    sentence_count = 0
    sentence = ""
    for i in text:
        if i.isalpha() == True or i == " " or i == "," or i == "'":
            sentence += i #remakes each sentence as the text inbetween punctuation
        else:
            sentence += i #adds punctuation to the end of sentence bc in testing it felt wrong not to
            count = counting_vowels_and_consonants(sentence)
            total_vowels += count[0]
            total_consonants += count[1]
            sentence_count += 1
            sentence = "" #resets sentence to prepare for next
    avg_vowels = total_vowels/sentence_count
    avg_consonants = total_consonants/sentence_count
    return (sentence_count, avg_vowels, avg_consonants)
    

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
print(f"In the paragraph there are {average_vowels_and_consonants(paragraph)[0]} sentences, across which there are an average of {average_vowels_and_consonants(paragraph)[1]} vowels per sentence and {average_vowels_and_consonants(paragraph)[2]} consonants per sentence. ")