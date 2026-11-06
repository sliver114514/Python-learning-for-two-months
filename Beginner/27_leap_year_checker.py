# 闰年检测器
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def main():
    print("=== Leap Year Checker ===")
    try:
        year_input = int(input("Enter a year: "))
        if is_leap_year(year_input):
            print(f"Yes, {year_input} is a leap year.")
        else:
            print(f"No, {year_input} is not a leap year.")
    except ValueError:
        print("Please enter a valid numeric year.")

if __name__ == '__main__':
    main()