#007_1 惰性求值
'''
惰性求值（Lazy Evaluation）是一种计算策略，用于推迟表达式的求值，直到实际需要这个值为止。
这种方式可以提高程序的性能，并允许创建无限的数据结构。
在惰性求值模型中，当你创建一个表达式或数据结构（例如生成器）时，计算不会立即执行。相反，每次需要一个新的值时，该值才会被计算。
'''

# 使用yield
def generate_numbers():
    for i in range(3):
        yield i

# 使用生成器表达式
squares = (x*x for x in range(3))

# map
squares = map(lambda x: x*x, [1, 2, 3, 4])

# filter
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])

gen = generate_numbers()
print(next(gen))  # 输出 0
