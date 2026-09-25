# 账单计算器的进阶版
total = input("What was the total total? $")
tip = input("What percentage tip?10, 12, or 15? $")
people = input("How many people to split? $")

try:
    bill = float(total) # 原始消费金额，不会变，保留
    tip_percent = int(tip) # 小费百分比
    num_people = int(people) # 人数

    if bill <= 0:
        print("Error: Tip must be greater than Zero.")
        exit()
    if tip_percent < 0 or tip_percent > 100:
        print("Error: Tip must be between 0 and 100.")
        exit()
    if num_people < 1:
        print("Error: Need at least one person")
        exit()
except ValueError:
    # 当int()和float()捕捉到非数字类的字符串时报错
    print("Error: Please enter valid number only.")
    exit()

tip_amount = bill * (tip_percent / 100) # 计算消费金额
total_bill = bill + tip_amount # 计算总金额
tip_per_person = tip_amount / num_people # 人均小费
total_per_person = total_bill / num_people # 人均总付

print(f"Original bill:${bill:.2f}")
print(f"Tip amount:${tip_amount:.2f}")
print(f"Including the total tip:${total_bill:.2f}")
print(f"People:${num_people}")
print(f"Each person should pay:${total_per_person:.2f}")