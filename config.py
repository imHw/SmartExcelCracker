# config.py

# 文件路径（请替换为你的加密 Excel 文件路径）
encrypted_file = "/path/to/encrypted.xlsx"

# 解密后输出文件路径
output_file = f"{encrypted_file.rsplit('.', 1)[0]}_破解版.xlsx"

# 固定数组（顺序固定）
fixed_array = "135"

# 数组出现位置优先级
# 可选值: "start", "end", "middle"
array_positions_priority = ["start", "end", "middle"]

# 尝试密码长度范围
min_length = 4
max_length = 11

# 模式优先级
# 1 = 数字, 2 = 数字+字母, 3 = 数字+字母+特殊字符
mode_priority = [1, 2, 3]

# 自定义字典（可选）
custom_dict = ["2025", "abcd"]
