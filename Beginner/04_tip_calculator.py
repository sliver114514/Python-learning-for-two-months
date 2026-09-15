# 账单计算器
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15, etc. $")
people = input("How many people to split the bill? ")

try:
    total = float(total)
    tip = int(tip)
    people = int(people)
    if tip < 0 or people < 1 or tip > 100 or total <= 0:
        raise ValueError
except ValueError:
    print("Please enter valid values")
    exit()

tip_amount = total * (tip / 100) # 计算小费金额
total += tip_amount # 计算总金额(加上小费)
tip_per_person = tip_amount / people # 人均小费
total_per_person = total / people # 人均总付(架上小费)

print(f"The total amount is${total:.2f} with tips."
      f"\nA tip amount of ${tip_amount:.2f} is equal to ${tip_per_person:.2f}."
      f"\nSplit between {people} people."
      f"\nEach person should pay:${total_per_person:.2f} or ${tip_per_person:.2f} for tips.")