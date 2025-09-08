# Take input from the user
user_input = input("Enter a string or number: ")

# Check if the input is a palindrome
if user_input == user_input[::-1]:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
