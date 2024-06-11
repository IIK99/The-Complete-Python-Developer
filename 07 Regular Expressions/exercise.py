import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\/[a-zA-Z0-9-.]+$)")
string = "Andrei"
pattern_2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = "maludinRinaa1099%$9"

a = pattern.search(string)
check = pattern_2.fullmatch(password)
print(check)
