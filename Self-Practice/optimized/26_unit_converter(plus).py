# 升级版单位转换器
# 工具函数：把用户输入的单位转为标准字典键（支持单数/复数）
def normalize_unit(unit):
    unit = unit.lower().strip()
    # 常见单数映射到复数（字典的键）
    singular_to_plural = {
        'meter': 'meters',
        'foot': 'feet',
        'inch': 'inches',
        'kilometer': 'kilometers',
        'mile': 'miles',
        'kilogram': 'kilograms',
        'pound': 'pounds',
        'ounce': 'ounces',
        'gram': 'grams'
    }
    return singular_to_plural.get(unit, unit)  # 如果没映射，就原样返回

# 通用转换函数（传入字典，而不是写两个函数）
def convert(value, from_unit, to_unit, conversion_dict):
    if from_unit not in conversion_dict or to_unit not in conversion_dict:
        return None
    base_value = value / conversion_dict[from_unit]
    result = base_value * conversion_dict[to_unit]
    return result

def main():
    print("=== Unit Converter ===")
    print("1. Length (meters, feet, inches, kilometers, miles)")
    print("2. Weight (kilograms, pounds, ounces, grams)")

    while True:
        choice = input("Select a conversion category (1-2): ").strip()
        if choice in ('1', '2'):
            break
        print("Invalid category. Please enter 1 or 2.")

    # 根据选择加载不同的转换字典
    if choice == '1':
        conversion_dict = {
            'meters': 1, 'feet': 3.28084, 'inches': 39.3701,
            'kilometers': 0.001, 'miles': 0.000621371
        }
        unit_type = "Length"
    else:
        conversion_dict = {
            'kilograms': 1, 'pounds': 2.20462, 'ounces': 35.274, 'grams': 1000
        }
        unit_type = "Weight"

    # ---------- 防弹衣输入区 ----------
    while True:
        try:
            value = float(input("Enter Value: "))
            if value <= 0:
                print("Value must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    from_unit = normalize_unit(input("Convert from unit: "))
    to_unit = normalize_unit(input("Convert to unit: "))

    # 调用通用转换
    result = convert(value, from_unit, to_unit, conversion_dict)

    if result is not None:
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
    else:
        print(f"Invalid units for {unit_type}. Please check your spelling.")