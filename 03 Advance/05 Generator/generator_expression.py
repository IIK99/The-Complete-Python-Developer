print("\ngenerator expression")
generator_exp = (i * 5 for i in range(10) if i % 2 == 0)

for i in generator_exp:
    print(i)

print("\n")
gen_exp = (x * x for x in range(10))

for value in gen_exp:
    print(value)
