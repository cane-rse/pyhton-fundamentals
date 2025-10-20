num1 = input("Enter a number: ")
if num1 == num1[::-1]:
    print(f"{num1} is a palindrome")
else:
    print(f"{num1} is not a palindrome")# This code checks if the entered number is a palindrome by comparing it to its reverse.
# This code checks if the entered number is a palindrome by comparing it to its reverse.
# A palindrome is a number or text that reads the same forwards and backwards.


def is_palindrome(word):
    # Normalize input: remove spaces and make lowercase
    normalized = word.replace(" ", "").lower()
    return normalized == normalized[::-1]

print("Palindrome Checker (type 'exit' to quit)")

while True:
    user_input = input("\nEnter a word or phrase: ").strip()
    
    if user_input.lower() == "exit":
        print("Goodbye! Keep reflecting and coding, one microcosm at a time 🌱")
        break

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome! ✅")
    else:
        print(f"'{user_input}' is not a palindrome. ❌")