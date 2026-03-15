# Implement a script that accepts CLI arguments using `sys.argv`.

# making a calculator using sys.argv steps:
# main function
# check if the length of sys.argv is 4 or not if not 4 notify user how to use usage: print("Usage: python script.py <operation> <num1> <num2>")
# exit
# convert the entered value's types to int as they are default strings
# sys.argv[1] is add, subtract ... so convert them to lowercase in case user enters caps
# make sure try and except num1 and num2 are numbers
# write the logic for addition, subtraction, multiplication and divison

import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <operation> <num1> <num2>")
        print("Example: python script.py add 10 20")
        sys.exit(1)

    script_name = sys.argv[0]
    operation = sys.argv[1].lower()

    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: num1 and num2 must be numbers")
        sys.exit(1)

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: divison by 0 isn't allowed")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"Error: unknown operation {operation}")
        sys.exit(1)
    
    print(f"Executing {script_name}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
