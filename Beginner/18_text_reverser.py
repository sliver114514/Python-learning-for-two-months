def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_text = reverse_string(user_input)
    print(f"The reversed string is: {reversed_text}")