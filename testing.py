x = 1
print(type(x))

if type(x) == int:
    x = 1.0
    if type(x) == int:
        print(True)
    else:
        print(False)

print()
x = 1.0
try:
    x = int(x)
    print(True)
except TypeError:
    print(False)