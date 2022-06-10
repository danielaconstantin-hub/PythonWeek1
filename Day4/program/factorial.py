def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))