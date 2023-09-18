#007_2 yield & next()
'''
在Python中，yield 关键字用于定义一个生成器函数。
这种函数返回一个生成器对象，该对象可以用于惰性地生成值。
与普通函数返回一个单一值不同，生成器函数可以返回多个值，每次一个。

高级用法：
1. yield from 语法
2. 生成器作为状态机
'''

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 输出 1
print(next(gen))  # 输出 2
print(next(gen))  # 输出 3

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(5)

for number in counter:
    print(number)

'''
yield 与 return 的区别
1. return 返回一个值并结束函数执行。而 yield 返回一个值但保留函数状态，以便后续继续执行。
2. 包含 yield 的函数返回一个生成器对象；普通函数返回一个单一值。
'''

gen = my_generator()

try:
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))  # 这会引发 StopIteration
except StopIteration:
    print('No more items.')
