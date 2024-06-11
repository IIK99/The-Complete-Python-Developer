# regular expression
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# re.
# findall 	Returns a list containing all matches
# search 	Returns a Match object if there is a match anywhere in the string
# split 	Returns a list where the string has been split at each match
# sub 	Replaces one or many matches with a string

print("\nWith re.findall()")
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.findall("Portugal", txt)
print(x)

print("\nWith re.search()")
x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())
x = re.search("Portugal", txt)
print(x)

print("\nWith re.split()")
x = re.split("\s", txt)
print(x)
x = re.split("\s", txt, 2)
print(x)

print("\nWith re.sub()")
x = re.sub("\s", "-", txt)
print(x)
x = re.sub("\s", "-", txt, 1)
print(x)

print("\nWith Match Object")
x = re.search("ai", txt)
print(x)  # will print an object
x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())
