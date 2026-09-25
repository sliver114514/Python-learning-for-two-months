from time import sleep

# 获取用户所需要的倒计时的时间
time = input("Enter the time to countdown from (MM:SS): ")

# 检查输入是否有效
if len(time) != 5 or time[2] != ":":
    print("Invalid time format")
    exit()

# 数字转换
minutes = int(time[:2])
seconds = int(time[3:])
total_seconds = minutes * 60 + seconds

# 开始倒计时
for i in range(total_seconds, 0, -1):
    print(f"{i//60:02}:{i%60:02}")
    sleep(1)

print("00:00")
print("Time's up!")
