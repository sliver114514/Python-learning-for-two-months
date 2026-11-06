# 简单的奇偶判断
def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    print("=== Odd / Even  Checker ===")
    while True:
        try:
            user_input = input("Enter a number to check if it's odd or even: ")
            number = int(user_input)

            result = check_odd_even(number)
            print(f"The number {number} is {result}")
            break

        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
