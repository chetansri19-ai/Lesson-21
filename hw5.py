try:
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    squares = [num * num for num in range(start, end + 1)]
    # Separate even and odd squares
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    print("All square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)

except ValueError:
    print("Error: Please enter valid integer values for the range.")