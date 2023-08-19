#Enter a string and find the longest word from it
import re
line = input("Enter the line: " )
MAX_LEN = -1
pat = r'([,!;.]{1}).+([.]{1})'

m= re.search(pattern=pat , string=line)

if m:
    print(m.group(1))
    print(m.group(2))

for eachGroup in m.groups():
    line = line.replace(eachGroup , " ")

print(line)
for eachWord in line.split(" "):
    if len(eachWord.strip()) >= MAX_LEN :
        MAX_LEN = len(eachWord.strip())
        maxWord = eachWord.strip()

print(maxWord)