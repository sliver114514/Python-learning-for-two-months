# 带注解版汇率转化器
# 定义一个字典 (dict)，储存”货币代码“到“汇率”的映射
# 约定：相对于 1 美元（USD）的数值
# 例如：RATES["DUR"] = 0.94,意思是 1 美元可以兑换 0.94 欧元
#      RATES["JPY"] = 149.85,意思是 1 美元可以兑换 149.85 日元
# 字典就是为此而生的“查表神器”
RATES = {
    "USD": 1.00,
    "EUR": 0.87,
    "GBP": 0.74,
    "JPY": 159.27,
    "AUD": 1.42,
    "CNY": 6.75
}

# 打印提示
print("Available currencies: USD, EUR, GBP, JPY, AUD, CNY")

# 输入源货币、目标货币，强制转化为大写
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

# 输入金额转化为浮点数
amount = float(input("Enter the amount to be converted: "))

# 如果源货币与目标货币任意一个不在字典里，就会进入报错分支
if from_currency not in RATES or to_currency not in RATES:
    print("Invalid currency. Please choose from the available currencies.")
else:
    # 核心算法
    # 金额（美元） = 金额（源货币） / RATES[源货币]  <- 除法
    # 金额（目标） = 金额（美元） * RATES[目标货币]  <- 乘法
    amount_in_usd = amount / RATES[from_currency]
    converted_amount = amount_in_usd * RATES[to_currency]

    # 输出结果
    print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")