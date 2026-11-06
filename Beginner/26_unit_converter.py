# 单位转换器
# 长度转换器

def length_conversion(value, from_unit, to_unit):
    # 不直接计算“英尺”到“英寸”，而是先把所有单位都换算成“米”（基准单位）
    # 这样只需要存“1 单位 = 多少米“，逻辑就统一了
    conversions = {
        'meters' : 1,
        'feet' : 3.28084,       # 英尺
        'inches' : 39.3701,     # 英寸
        'kilometers' : 0.001,   # 公里
        'miles' :0.000621371    # 英里
    }

    # 防呆检测
    if from_unit not in conversions or to_unit not in conversions:
        return None  # 返回 None 表示转化失败

    # 除以源单位系数，得到“基准值（米）”
    meters = value / conversions[from_unit]

    # 乘以目标单位的系数，得到最终结果
    result = meters * conversions[to_unit]

    return result

# 重量转换器，逻辑同上
def weight_conversion(value, from_unit, to_unit):
    conversions = {
        'kilograms' : 1,
        'pounds' : 2.20462,
        'ounces' : 35.274,
        'grams' : 1000
    }
    #防呆检测
    if from_unit not in conversions or to_unit not in conversions:
        return None

    kilograms = value / conversions[from_unit]

    result = kilograms * conversions[to_unit]

    return result

def main():
    print("=== Unit Converter ===")
    print("1. Length (meters, feet, inches, kilometers, miles)")
    print("2. Weight (kilograms, pounds, ounces, grams)")

    choice = input("Select a conversion category (1-2):")

    if choice == "1":
        value = float(input("Enter a value: "))
        from_unit = input("Convert from unit: ").lower()
        to_unit = input("Convert to unit: ").lower()
        result = length_conversion(value, from_unit, to_unit)
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f}{to_unit}.")
        else:
            print("Invalid units.")

    elif choice == "2":
        value = float(input("Enter a value: "))
        from_unit = input("Convert from unit: ").lower()
        to_unit = input("Convert to unit: ").lower()

        result = weight_conversion(value, from_unit, to_unit)

        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.2f}{to_unit}.")
        else:
            print("Invalid units.")

    else:
        print("Invalid category.")

if __name__ == "__main__":
    main()
