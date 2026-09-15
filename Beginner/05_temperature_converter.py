# 温度转换器
def celsius_to_fahrenheit(celsius):
    """"摄氏度转华氏度：°F = °C * 9/5 + 32"""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度：°C = (°F - 32) * 5/9"""
    return (fahrenheit - 32) * 5/9

user_unit = input("Enter the unit to convert from (C/F):").strip().upper()

user_temperature_input = input("Enter the temperature:").strip().upper()

try:
    # 把字符串转数字放在 try 内部，这样输入 "abc" 就会被 except 捕获
    temperature = float(user_temperature_input)

    # 先校验单位是否合法
    if user_unit not in ("C", "F"):
        raise ValueError("Invalid unit.Please enter 'C' or 'F'.")
    # 根据不同的单位，检查绝对零度
    if user_unit == "C" and temperature < -273.15:
        raise ValueError("Temperature below absolute zero (-273.15°C).")
    if user_unit == "F" and temperature < -459.67:
        raise ValueError("Temperature below absolute zero (-459.67°F).")

# except 统一收尾，不管是输入非数字，还是单位错误，还是绝对零度，全部在这里温柔提示并退出
except ValueError as e:
    # 如果 e 是我们上面 raise 的，就打印具体内容；如果是 float 转换报错，e 默认是 "could not convert string to float"
    print(f"Input Error: {e}")
    exit()

if user_unit == "C":
    result = celsius_to_fahrenheit(temperature)
    print(f"{temperature:.2f}°C is {result:.2f}°F")
else:
    result = fahrenheit_to_celsius(temperature)
    print(f"{temperature:.2f}°F is {result:.2f}°C")