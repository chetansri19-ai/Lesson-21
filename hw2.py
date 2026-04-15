try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 150:
        print("Error: Age entered is not realistic.")
    else:
        print("Valid age entered.")

        # Check even or odd
        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Error: Please enter a valid number for age.")