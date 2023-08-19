#Program to count and display words with Starts with a Vowel
#approach 1 - advance using the regex pattern
#approach 2 - Normal iteration
import re
VOWELS=['a' , 'e', 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
vowelCount = 0
line = input("Enter a line: " )
pat_vowels = r'\b[aeiouAEIOU]\w*\b'
pat_special = r''
pat= re.compile(pattern=pat_vowels)

for eachWord in line.split(" "):
    print("Word under scanning:" , eachWord)
    if eachWord[0] in VOWELS:
        print(eachWord)
        vowelCount+=1

print("Total words: " , vowelCount)
