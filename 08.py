# Write a script that behaves differently when run directly vs imported (`if __name__ == "__main__":`)

if __name__ == "__main__":
    print("this runs only when it's the main entry file")
else:
    print("this ran when it's not the main entry file")

# the if statement will run if directly run this file, and if you import this file in main.py and run main.py the else statement will run.
# remember python won't let you import a file starting with number so change the name when importing.