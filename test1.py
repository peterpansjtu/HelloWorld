

data = ['\n', 'CSQ0000063909105\n', '', 'CSQ0000063', '909105']

trial = 1
code = ''
while True:
    if trial >= 10:
        break
    print(len(code))
    if len(code) >= 16:
        break
    part = str(data[trial]).replace("\r\n", "").replace("\n", "").replace("\r", "")
    print("Mirco Scanner read: ", part)
    code += part
    print("Mirco Scanner bar code: ", code)
    trial += 1

print("=============================================")


def two_equal_code(string):
    if len(string) % 2:
        return False
    sub_len = int(len(string) / 2)
    if string[:sub_len] == string[sub_len:]:
        return True
    return False


trial = 1
code = ''
while True:
    if trial >= 10:
        break
    part = str(data[trial]).replace("\r\n", "").replace("\n", "").replace("\r", "")
    print("Mirco Scanner read: ", part)
    code += part
    if two_equal_code(code):
        code = code[:int(len(code) / 2)]
        print("Mirco Scanner bar code: ", code)
        break
    trial += 1
print(code)
