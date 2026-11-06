# 闰年判断器简化升级版
def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

def main():
    print("=== Leap Year Checker ===")
    while True:
        try:
            year_input = int(input("Enter Year:"))
            if year_input <= 0:
                print("Please enter a valid year.")
                continue

            if is_leap_year(year_input):
                print(f"{year_input} is Leap Year")
            else:
                print(f"{year_input} is not Leap Year")
            break

        except ValueError:
            print("Please enter a valid numeric year.")

if __name__ == '__main__':
    main()