# 简单利息计算器,并加上了防呆检测
def calculate_simple_interest(principal, rate, time):
    """
    计算单利 (Simple Interest)
    公式：SI = (P * R * T) . 100

    参数解读 (从数学到代码映射):
    - principal (P): 本金，用户存进去的钱
    - rate (R): 年利率 (以百分比为单位。比如用户输入 5，代表 5%)
    - time (T):时间，单位年
    """
    interest = (principal * rate * time) / 100
    return interest

def main():
    print("=== Simple Interest Calculation ===")

    while True:
        try:
            p = float(input("Enter the principal amount: "))
            if p < 0:
                print("Please cannot be negative.Please try again.")
                continue

            r = float(input("Enter the annual interest rate (in %): "))
            if r < 0:
                print("Please cannot be negative.Please try again.")
                continue

            t = float(input("Enter the time (in years): "))
            if t < 0:
                print("Please cannot be negative.Please try again.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    si = calculate_simple_interest(p, r, t)

    print(f"\nThe simple interest is: {si:.2f}") # 利息
    print(f"Total amount (Principal + Interest): {p + si:.2f}") # 本金加利息

if __name__ == "__main__":
    main()