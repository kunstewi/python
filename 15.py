# Use the `input()` function to take user data and cast it to `int`.

# make a function get_user_age
# take a input
# check the type of input
# in try except block explicitely cast the type to int
# write the logic for age remaining to retirement
# otherwise ValueError
# if name = main call the function

def get_user_age():
    raw_input = input("Please enter your age: ")
    print(f"type of entered input: {type(raw_input)} ") # it would be class string by default

    try:
        age = int(raw_input)
        years_to_retirement = 65 - age

        if years_to_retirement > 0:
            print(f"you have approx {years_to_retirement} years to retire")
        else:
            print(f"you have reached past the retirement age")

    except ValueError:
        print(f"Error: {raw_input} is not a valid whole number")

if __name__ == "__main__":
    get_user_age()



