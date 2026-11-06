def generate_fibonacci(n_terms):
    """
    生成斐波那契数列的前 n_terms 项

    斐波那契数列定义从第三项开始，每一项都等于前两项之和
    通常约定：第一项 = 0，第二项 = 1

    参数：
        n_terms (int): 要生成数列的项数 (非负整数)

    返回：
        list: 包含斐波那契数列的列表
    """

    # 若用户输入小于 0 的项，返回空列表
    # 数学上“前 0 项”没有意义，但作为函数必须处理，防止程序报错
    # 用 <= 而不是 ==，也是为了防止负数
    if n_terms <= 0:
        return []

    # 显示处理特殊情况，是代码可读性的重要体现
    if n_terms == 1:
        return [0]

    # 初始化前两项，这是斐波那契数列的“种子”
    # 因为后一项依赖前两项，所以要打好“地基”
    sequence = [0, 1]

    # 这里的循环条件是:只要当前长度没达到目标，就继续生长
    while len(sequence) < n_terms:

        # sequence[-1] 指向列表的最后一个袁术
        # sequence[-2] 指向列表的倒数第二个元素
        # 比如当前 sequence = [0, 1, 1, 2]:
        #   sequence[-1] = 2(最后一项)
        #   sequence[-2] = 1(倒数第二项)
        # 两者相加结果就是 3 ，这正是下一个斐波那契数
        # 这是 python 特有的“语法糖”
        # 传统写法是 sequence[len(sequence)-1] + sequence[len(sequence)-2]
        next_value = sequence[-1] + sequence[-2]

        # 将计算出的新选项添加到列表末尾
        sequence.append(next_value)

if __name__ == '__main__':
    print("--- Fibonacci sequence Generator ---")

    while True:
        try:
            # 获取用户输入（字符串）
            num_str = input("Enter the number of Fibonacci terms to generate: ")
            num_terms = int(num_str) # 强制转换

            if num_terms < 0:
                print("Please enter a non-negative number.")
                continue

            # 调用核心生成函数
            fib_sequence = generate_fibonacci(num_terms)

            print(f"\nThe Fibonacci sequence is {num_terms} terms is: \n{fib_sequence}")

            # 正确输入并执行完毕，跳出循环
            break

        except ValueError:
            print("Invalid input,please enter a whole number.")
