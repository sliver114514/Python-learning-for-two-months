# bmi计算器
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")

# python 内置的语法糖
elif 18.5 <= bmi <25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")