# 质数生成器
def is_prime(num):
    """
    判断一个数是否为质数
    质数定义：大于一的自然数，除了 1 和它本身，没有其它正因数

    参数：
        num(int):待判断的整数

    返回：
        bool: 是质数返回 True,否则返回False
    """
    # 根据定义，质数必须大于一
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        # 取模运算：如果 num 能直接被 i 整除，说明找到了除了 1 和自身的因子
        if num % i == 0:
            # 一旦发现，立即返回 False，不再继续执行（提前退出，提升效率）
            return False

    # 如果循环结束都没有返回 False,说明这个数没有任何因子，是质数
    return True

def generate_primes_up_to(limit):
    """
    生成从 2 到指定上线之间的所有质数列表

    参数：
        limit(int):搜索的上限（包含该数）

    返回：
        list:包含所有质数的列表
    """
    # 初始化一个空列表，由于存放结果
    primes_numbers = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes_numbers.append(number)

    # 返回收集好的质数列表
    return primes_numbers

if __name__ == '__main__':
    print("--- Prime Number Generators ---")

    while True:
        try:
            limit_str = input("Enter an upper limit to find prime numbers up to: ")

            # 强制类型转换
            limit = int(limit_str)

            if limit < 2:
                print("Please enter a number greater than or equal to 2.")
                continue

            # 调用核心生成代码
            primes = generate_primes_up_to(limit)

            print(f"\nPrime numbers up to {limit} are: \n{primes}:")

            break

        except ValueError:
            print("Invalid input.Please enter a whole number.")