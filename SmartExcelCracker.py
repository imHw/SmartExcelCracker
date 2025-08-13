import msoffcrypto
import itertools
import string
import threading
import tkinter as tk
import config  # 引入配置文件

##########################
# 读取配置
##########################

encrypted_file = config.encrypted_file
output_file = config.output_file
fixed_array = config.fixed_array
array_positions_priority = config.array_positions_priority
min_length = config.min_length
max_length = config.max_length
mode_priority = config.mode_priority
custom_dict = config.custom_dict

current_password = ""  # GUI显示当前尝试密码

##########################
# 破解逻辑
##########################

def try_password(password):
    """
    尝试使用给定密码解密文件
    返回 True 表示成功
    """
    try:
        with open(encrypted_file, 'rb') as f_in:
            office_file = msoffcrypto.OfficeFile(f_in)
            office_file.load_key(password=password)
            with open(output_file, 'wb') as f_out:
                office_file.decrypt(f_out)
        return True
    except Exception:
        return False

def get_chars_by_mode(mode):
    """
    根据模式返回字符集
    """
    if mode == 1:
        return string.digits
    elif mode == 2:
        return string.digits + string.ascii_letters
    elif mode == 3:
        return string.digits + string.ascii_letters + "!@#$%^&*()-_+="
    else:
        raise ValueError("模式选择错误，只能是1,2,3")

def generate_passwords():
    """
    根据配置生成密码
    """
    global fixed_array, min_length, max_length

    for mode in mode_priority:
        chars = get_chars_by_mode(mode)
        for total_len in range(min_length, max_length + 1):
            remaining_len = total_len - len(fixed_array)

            for pos_type in array_positions_priority:
                if pos_type == "start":
                    start_pos_list = [0]
                elif pos_type == "end":
                    start_pos_list = [total_len - len(fixed_array)]
                elif pos_type == "middle":
                    start_pos_list = list(range(1, total_len - len(fixed_array)))
                else:
                    continue

                for start_pos in start_pos_list:
                    if remaining_len < 0:
                        yield fixed_array
                        continue

                    positions = [i for i in range(total_len) if not start_pos <= i < start_pos + len(fixed_array)]

                    for rest_chars in itertools.product(chars, repeat=remaining_len):
                        pwd = [''] * total_len
                        for i, d in enumerate(fixed_array):
                            pwd[start_pos + i] = d
                        for pos, ch in zip(positions, rest_chars):
                            pwd[pos] = ch
                        yield ''.join(pwd)

                    # 插入自定义字典
                    for word in custom_dict:
                        if len(word) + len(fixed_array) <= total_len:
                            temp_pwd = [''] * total_len
                            for i, d in enumerate(fixed_array):
                                temp_pwd[start_pos + i] = d
                            insert_pos = positions[0] if positions else len(fixed_array)
                            for j, c in enumerate(word):
                                temp_pwd[insert_pos + j] = c
                            for idx in range(total_len):
                                if temp_pwd[idx] == '':
                                    temp_pwd[idx] = chars[0]
                            yield ''.join(temp_pwd)

def crack_password():
    """
    破解线程：迭代生成密码并尝试解密
    """
    global current_password
    for pwd in generate_passwords():
        current_password = pwd
        if try_password(pwd):
            current_password = f"密码正确！密码是: {pwd}"
            return

##########################
# GUI显示
##########################

def update_label():
    global current_password
    label_var.set(current_password)
    root.after(100, update_label)

root = tk.Tk()
root.title("SmartExcelCracker - Password Attempt")
root.geometry("600x120")

label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var, font=("Arial", 16))
label.pack(expand=True)

threading.Thread(target=crack_password, daemon=True).start()

update_label()
root.mainloop()
