#21 Exponent Function

print(2**3)
# ==2^3

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,2))

#扩展
num1 = float(input("Enter base number: "))
num2 = int(input("Enter power number: "))

print(raise_to_power(num1,num2))
