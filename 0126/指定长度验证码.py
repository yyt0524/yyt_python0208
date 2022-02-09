
import random

def generate_code(code_len):
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = code_len - 1
    code = ''
    for item in range(code_len):
        index = random.randint(0, len(chars)-1)
        code += chars[index]
    return code

length = eval(input('enter the code length: '))
print('the random code is : ',generate_code(length))