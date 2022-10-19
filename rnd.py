import random

# [0, 1) -> float (azaz 64 bites, lebegőpontos) véletlen számot állít elő
random.random()
# [a, b] a < b véletlen egész számot állít elő
random.randint(10, 100)
# [start, stop) "step"esével vett intervallumból választ egy véletlen számot
random.randrange(0, 100, 2)

r31:int = random.randint(100, 999)
print(r31)
r32_1:float = random.random() * 25
print(r32_1)
r32_2:float = random.randint(0, 250) / 10
print(r32_2)
r33:float = random.randint(0, 100) / 10 + 15
print(r33)
r34:int = random.randint(0, 49) * 2
print(r34)
r35:int = random.randint(20, 40) * 5
print(r35)