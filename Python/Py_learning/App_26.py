#26 Reading Files

employee_file = open("employees_for26.txt", "r")
#"r", "w", "a", "r+",
#https://www.w3schools.com/python/ref_func_open.asp

# print(employee_file.readable())
# print(employee_file.read())
#先检测可读性，再读取文件

# print(employee_file.readline())
# print(employee_file.readline())
#按照行数读取文件

#print(employee_file.readlines())
#同时读取多行数据
#print(employee_file.readlines()[1])
#读取指定行数据

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
#always closing the file