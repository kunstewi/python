import sys

if len(sys.argv) != 4:
    print("Usage: python calc.py <num1> <operator> <num2>")
    sys.exit(1)

# parse arguements
num1 = float(sys.argv[1])
op = sys.argv[2]
num2 = float(sys.argv[3])

# operations
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else :
    print("Unknown Operator")
    sys.exit(1)

print("Result:", result)