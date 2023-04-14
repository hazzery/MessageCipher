invertables = []
inverses = []
for x in range(26):
    try:
        invertables.append(pow(x, -1, 24))
    except ValueError:
        pass

for num in invertables:
    try:
        inverses.append(pow(num, -1, 35))
    except ValueError:
        inverses.append(0)
print(invertables)
print(inverses)
