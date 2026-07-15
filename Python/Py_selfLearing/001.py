#001 列表切片
'''
sequence[start:stop:step]

start: 切片的开始位置。如果省略，默认为0。
stop: 切片的结束位置（不包括此位置）。如果省略，默认为序列的长度。
step: 切片的步长。如果省略，默认为1。
'''

lst = [0, 1, 2, 3, 4, 5]

print(lst[1:4])  # 输出 [1, 2, 3]
print(lst[:3])   # 输出 [0, 1, 2]
print(lst[3:])   # 输出 [3, 4, 5]
print(lst[::2])  # 输出 [0, 2, 4]

s = "abcdef"

print(s[1:4])  # 输出 "bcd"
print(s[:3])   # 输出 "abc"
print(s[3:])   # 输出 "def"
print(s[::-1]) # 输出 "fedcba"，这是一个常用的字符串反转技巧