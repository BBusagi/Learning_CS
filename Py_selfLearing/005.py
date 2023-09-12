#005 格式化字符串_f-string
'''
在Python中，以 f 或 F 前缀开头的字符串称为格式化字符串（f-string）。
它们用于嵌入表达式到字符串字面量中，从而创建一个新的字符串。

在f-string中，表达式被包含在大括号 {} 中，并可以直接访问变量、常量、字面量和表达式。
'''
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

name = "Alice"
age = 30
print("My name is " + name + " and I am " + str(age) + " years old.")