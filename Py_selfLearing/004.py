# enumerate
'''
enumerate 是一个内置的 Python 函数，用于在遍历一个可迭代对象（如列表、元组、字符串等）时获取元素及其索引。
enumerate 函数返回一个迭代器，该迭代器生成由索引和元素组成的元组
'''
fruits = ['apple', 'banana', 'mango']
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

print(fruits.index('apple'))
print(fruits[0])
