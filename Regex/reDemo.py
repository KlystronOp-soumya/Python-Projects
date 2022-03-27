import re

age_pattern_str = r'\d{2,3}'
name_pattern_str=r'[A-Z][a-z]*'

search_string="Jessica is 15 years old,her brother Jhon is 10 years old. Jacob is now 40 years old."

age_pattern = re.compile(age_pattern_str)
name_pattern = re.compile(name_pattern_str)

names=re.findall(name_pattern,search_string)
ages=re.findall(age_pattern,search_string)

print(names)
print(ages)

#re.match only matches to the bgining of the String and re.search mathces the entire string
