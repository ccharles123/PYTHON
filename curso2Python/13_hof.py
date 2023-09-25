#hacemos el ejemplo con una funcion clasica:
def increment(x):
    return x + 1

def highOrderFunction(x, func):
    return x + func(x)

result = highOrderFunction(2, increment)
# 2 + (2 + 1) = 5
print(result)

#hacemos el mismo ejemplo con lambdas:
increment2 = lambda x: x + 1
highOrderFunction2 = lambda x, func2: x + func2(x)
result2 = highOrderFunction2(2, increment2)
result3 = highOrderFunction2(2, lambda x: x + 2) # 2 + (2 + 2) = 6
result4 = highOrderFunction2(2, lambda x: x * 5) # 2 + (2 * 5) = 10
print(result2)
print(result3)
print(result4)