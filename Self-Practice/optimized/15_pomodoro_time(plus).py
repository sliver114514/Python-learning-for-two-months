# # 番茄钟高级版
import time  # 提供 sleep 函数， 控制倒计时节奏
import sys  # 提供 stdout.write 和 flush. 用于实现“原地刷新”效果
import shutil  # 用于获取当前终端窗口的宽度，让进度条自适应

def get_config():
    """
    作用：获取用户输入，并做容错处理
    设计亮点：使用 input(...) or 默认值 的技巧
    如果用户直接回车(输入空字符串)， or 左侧为假，则取右侧默认值
    """
    print("\n欢迎使用高级 (在终端中 Ctrl+C 安全退出)")
    try:
        # 注意；int() 转换非字符会抛出ValueError，我们统一用 try 来捕获
        work = int(input("请输入工作时长(分钟) [默认25]: ") or 25)
        short_break = int(input("请输入短休息时长(分钟) [默认5]: ") or 5)
        long_break = int(input("请输入长休息(分钟) [默认15]: ") or 15)
        rounds = int(input("请输入目标番茄数(达到后自动结束) [默认4]: ") or 4)
        return work, short_break, long_break, rounds
    except ValueError:
        # 只要有任何一项输入了乱码 (比如字母)，统统回到默认值，程序绝不崩溃
        print("输入无效，将使用默认值 (25/5/15/4)")
        return 25, 5, 15, 4

def get_terminal_width():
    """
    作用：获取终端宽度，用于决定进度条画多长
    为什么要单独封装？因为 shutil 在某些环境 (如 PyCharm 内置终端) 可能会报错
    为什么用 try 兜底，最多返回到 80 列宽
    """
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def draw_progress(phase_name, elapsed, total, round_info=""):
    """
    作用：在一行内动态刷新显示进度条 + 百分比 + 剩余时间
    :param phase_name: 当前阶段文字 (如 "工作中......")
    :param elapsed: 已经过去的秒数 (用于计算百分比)
    :param total: 总秒数
    :param round_info: 当前第几轮 (如"[第 1/4 轮]")

    核心技巧：\r 将光标移动到首行，结合 sys.stdout.write 不换行
    实现"同一行不断覆盖更新"
    """
    if total <= 0:
        return

    # 计算剩余秒数，以及完成进度百分比 (0~100)
    remaining = total - elapsed
    percent = min(100, int((elapsed / total) * 100))

    # 动态决定进度条宽度：取“终端减40”和“50”中的较小值
    # 以免文字太长把进度条挤到下一行
    # get_terminal_width 返回当前终端窗口的总列数
    bar_width = min(50, get_terminal_width() - 40)
    filled = int(bar_width * percent / 100)  # 填充的格子数
    bar = '█' * filled + '░' * (bar_width - filled)  # 显示完成与未完成

    # 格式化剩余时间为 分:秒
    rem_mins, rem_secs = divmod(remaining, 60)

    # 组装最终要打印的一行文本，末尾留几个空格用于覆盖掉之前较长的残留字符
    line = f"\r{phase_name} {round_info} |{bar} {percent:>3}% 剩余 {rem_mins:>3}min {rem_secs:02d}  "
    # sys.stdout.write 是 print 的"底层形态"，它俩是同一个函数的不同写法
    sys.stdout.write(line)  # 写进缓冲区但不换行
    sys.stdout.flush()  # 强制立即刷新到屏幕，否则可能被缓冲

def countdown_with_progress(seconds, phase_name, round_info=""):
    """
    作用：执行指定秒数的倒计时，并每秒调用一次绘制函数
    返回值：True 表示正常走完：False 表示用户按了 Ctrl+C 中断

    关键：for elapsed in range(seconds + 1):
    当 elapsed = 0 时，显示 0%：
    当 elapsed = seconds 时，显示 100%，完美覆盖整个区间
    """
    try:
        # 从 0 到 seconds，总共循环 seconds + 1 次，确保最后能显示 100%
        for elapsed in range(seconds + 1):
            draw_progress(phase_name, elapsed, seconds, round_info)
            time.sleep(1)  # 间隔 1 秒，实现真实倒计时
        print()  # 倒计时自然结束后换行，让后续 print 不接在进度条后面
        return True

    except KeyboardInterrupt:
        # 在此处捕获 Ctrl + C
        print("\n\n 用户中断，正在安全退出当前阶段...")
        return False  # 返回False，通知上层调度器“该收场了”

def run_pomodoro():
    """
    作用：调度整个番茄钟流程 (工作 -> 休息 -> 下一轮)
    这是整个程序的“大概”，负责判断什么时候短休，什么时候长休
    什么时候彻底结束
    """
    # 获取用户配置，拆成四个变量
    work, short_b, long_b, total_rounds = get_config()

    current_round = 1  # 当前从第一轮开始
    print(f"\n设定完成：共{total_rounds}个番茄钟，每{work}分钟工作，{short_b}分钟短休，每四轮一次长休")
    print("按 Ctrl+C 随时安全退出程序\n")

    # try 捕获用户在“非倒计时阶段”按下 Ctrl + C
    try:
        while current_round <= total_rounds:
            round_tag = f"[{current_round}/{total_rounds}]"
            print(f"{round_tag} 开始专注工作...")
            # 调用倒计时引擎，如果返回 False，说明用户中断，立即 break 跳出循环
            if not countdown_with_progress(work * 60, "工作中", round_tag):
                break

            # 判断是否全部结束
            if current_round == total_rounds:
                print(f"\n恭喜！已完成全部{total_rounds} 个番茄钟！收工！")
                break

            # 番茄钟的经典规则：每四轮休息一次长轮
            is_long_break = (current_round % 4 == 0)
            break_type = "长休息" if is_long_break else "短休息"
            break_duration = long_b if is_long_break else short_b

            print(f"\n{round_tag} 进入 {break_type} ({break_duration}分钟)...")
            if not countdown_with_progress(break_duration * 60, break_type, round_tag):
                break  # 中断跳出

            # 轮次递增
            current_round += 1

    except KeyboardInterrupt:
        # 防止用户在“输入配置之后、倒计时开始之前”按下 Ctrl + C 导致报错
        print("\n\n感谢使用，已安全退出")
        return

    # 无论是自然结束还是中断跳出，都会执行到这里
    print("\n下次见！")

# 程序入口
if __name__ == "__main__":
    run_pomodoro()
