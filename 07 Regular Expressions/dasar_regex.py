# Dasar-Dasar Regex

#     Karakter Dasar:
#         a, b, c, dll.: Karakter yang cocok dengan diri mereka sendiri.

#     Metakarakter:
#         .: Cocok dengan karakter apa pun kecuali baris baru.
#         ^: Cocok dengan awal dari string.
#         $: Cocok dengan akhir dari string.
#         *: Cocok dengan 0 atau lebih pengulangan dari karakter sebelumnya.
#         +: Cocok dengan 1 atau lebih pengulangan dari karakter sebelumnya.
#         ?: Cocok dengan 0 atau 1 pengulangan dari karakter sebelumnya.
#         {n}: Cocok dengan tepat n pengulangan dari karakter sebelumnya.
#         {n,}: Cocok dengan setidaknya n pengulangan dari karakter sebelumnya.
#         {n,m}: Cocok dengan setidaknya n dan paling banyak m pengulangan dari karakter sebelumnya.

#     Karakter Khusus:
#         \d: Cocok dengan digit (angka).
#         \D: Cocok dengan non-digit.
#         \w: Cocok dengan karakter kata (alphanumeric dan underscore).
#         \W: Cocok dengan non-karakter kata.
#         \s: Cocok dengan whitespace (spasi, tab, newline).
#         \S: Cocok dengan non-whitespace.

#     Karakter Set:
#         [abc]: Cocok dengan salah satu dari karakter di dalam tanda kurung.
#         [a-z]: Cocok dengan karakter dari a sampai z.
#         [^abc]: Cocok dengan karakter selain a, b, atau c.

import re

# Pencocokan dasar
pattern = r"hello"
string = "hello world"
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())

# Pencocokan dengan metakarakter
pattern = r"\d+"  # Cocok dengan satu atau lebih digit
string = "123 abc 456"
matches = re.findall(pattern, string)
print("Matches found:", matches)

# Penggantian teks
pattern = r"abc"
replacement = "xyz"
string = "abc def abc"
new_string = re.sub(pattern, replacement, string)
print("Replaced string:", new_string)

# Pengecekan awal dan akhir string
pattern = r"^hello"
string = "hello world"
if re.match(pattern, string):
    print("String starts with 'hello'")

pattern = r"world$"
string = "hello world"
if re.search(pattern, string):
    print("String ends with 'world'")
