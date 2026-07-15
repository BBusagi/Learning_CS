#27 Writing to Files

employee_file = open("employees_for26.txt", "a")
#employee_file.write("Toby - Human Resources")
employee_file.write("\nToby - Human Resources")

# employee_file = open("index.html", "w")
# employee_file.write("<p>This is HTML</p>")
employee_file.close()

#拓展
#writeline ,添加数组列表
#employee_file.writelines(["\nKelly - Customer Service","\nRiku - Boss"])
#拆分写法：
# lines =[
#     "\nKelly - Customer Service",
#     "\nRiku - Boss"
# ]
# employee_file.writelines(lines)