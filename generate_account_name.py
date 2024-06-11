import random
import string


def generate_account_name():
    # 首字母必须是字母
    first_letter = random.choice(string.ascii_letters)
    # 其余部分可以是字母或数字
    rest = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    return first_letter + rest


def generate_password():
    # 密码长度设为12
    length = 12
    # 确保密码包含字母、数字和特殊符号
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_characters, k=length))
    return password


# 生成100个账户名称和对应的密码
accounts = [(generate_account_name(), generate_password()) for _ in range(100)]

for account, password in accounts:
    print(f"账户名称: {account}, 密码: {password}")
