# Swap two variables without using a temporary variable.

# using temp
x = 10
y = 20
temp = x

x = y
y = temp

print(x, y, temp)

# using tuple unpacking pythonic way
a = 50
b = 100

(a, b) = (b, a)

print(a, b)