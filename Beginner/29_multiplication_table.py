# # 乘法表生成器
def generate_table(number, table_range=10):
    print(f"\nMultiplication Table for {number}:")
    # +1 是为了让其打印到本位
    for i in range(1, table_range + 1):
        print(f" {number} × {i} = {number * i}")

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a number for multiplication table: "))
            break
        except ValueError:
            print("Invalid input.Please enter integers.")

    while True:
        range_input = input("Enter a range (default is 10): ")
        if range_input.strip() == "":
            generate_table(num)
            break
        else:
            try:
                table_limit = int(range_input)
                if table_limit <= 0:
                    print("Please enter a positive integer.")
                    continue
                generate_table(num, int(range_input))
                break
            except ValueError:
                print("Invalid input.Please enter integers or leave blank for default.")