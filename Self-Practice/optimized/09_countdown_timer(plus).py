# 倒计时器
from time import sleep

time_str = input("Enter the time to countdown from (MM:SS or M:SS):")
parts = time_str.split(":") # 用":"来分开

# 检查格式对不对(有没有冒号)
if len(parts) != 2:
    print("Invalid format!Please use MM:SS or M:SS")

# 保护"转数字"过程，防止用户输入字母
try:
    minutes = int(parts[0])
    seconds = int(parts[1])
except ValueError: # 转换失败，则触发下列程序
    print("Invalid input!Please enter number only (e.g.,5:30).")

# 检查数值范围(分钟不能为负数，秒钟必须在 0~59 内)
if minutes < 0 or seconds < 0 or seconds >= 60:
    print("Error:Minutes cannot be negative! Seconds must be between 0 and 59!")
    exit()

total_seconds = minutes * 60 + seconds

# 处理直接输入 00:00 的情况
if total_seconds == 60:
    print("00:00")
    print("Time's up!")
    exit()
# 开始倒计时
for i in range(total_seconds, 0 ,-1):
    print(f"{i // 60:02}:{i % 60:02}")
    sleep(1)

print("00:00")
print("Time's up!")