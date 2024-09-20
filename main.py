print("Welcome to the Area of a Square calculator")
print("Application was made by Dynasty")

print("Enter the length of the square:")
length = float(input())

print()
print("Enter the breadth of the square:")
breadth = float(input())

area = length * breadth

print()
print("The area of the square with length " + str(length) + " and breadth " + str(breadth) + " is:")
print("\n\n" + str(area))


# The float() function is used to convert the input to a floating-point number, allowing for decimal values.

# The str() function converts numbers back to strings for concatenation in the print statements.