# # 番茄钟
import time

def countdown(minutes):
    """
    函数作用: 输入分钟数，在终端进行倒计时显示
    参数 minutes: 证书或浮点数，代表需要倒计时的总分钟数
    """
    seconds = minutes * 60
    while seconds > 0:
        # divmod(a, b) 是 Python 内置函数， 返回(a // b, a % b)
        # 这里我们把总秒数 second 除以 60， 得到:
        # min ->整除部分 (还剩多少分钟)
        # sec ->余数部分 (还剩多少秒， 范围 0~59)
        mins, secs = divmod(seconds, 60)

        # 使用 f-string（格式化字符串）把数字变成 2 位宽度，不足补 0
        # 例如：如果 mins=3, secs=5，则 timer = "03:05"
        timer = f"{mins:02d}:{secs:02d}"

        # print(timer, end="\r") 是终端倒计时的核心技巧：
        # - 默认 print() 会在末尾加换行符 \n，导致每次打印都换行。
        # - 这里指定 end="\r"，\r 是“回车符”，表示把光标移回当前行的开头。
        # - 这样下一次 print 就会覆盖掉上一次打印的数字，形成原地刷新动画。
        print(timer, end="\r")

        # 让程序真正地“睡” 1 秒钟（等待 1 秒后再继续循环）
        time.sleep(1)

        # 总秒数减 1，代表过去了一秒钟
        seconds -= 1

def main():
    """
        程序的主入口，负责与用户交互并调度工作/休息循环。
    """
    print("Pomodoro Timer")
    while True:
        try:
            work_minutes = int(input("Enter work duration in minutes:"))
            break_minutes = int(input("Enter break duration in minutes:"))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        # 开始工作阶段
        print("Work session started.")
        countdown(work_minutes) # 调用上面定义的倒计时函数
        print("Work session finished. Take a break!") # 工作结束提示

        # 开始休息阶段
        countdown(break_minutes) # 再次调用倒计时，这次倒计休息时间
        print("Break finish. Time to get back to work!") # 休息结束提示

if __name__ == '__main__':
    """
        这是 Python 的标准写法。
        作用：只有当你在终端直接运行 `python 这个文件.py` 时，
        才会执行下面的 main() 函数。

        如果你在其他脚本中 `import` 这个文件，那么 main() 不会自动执行，
        避免了不必要的程序启动。这在你的“百宝箱”项目中非常重要。
    """
    main()