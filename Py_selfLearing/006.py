#006  字典_Dictionary
'''
在 Python 中，字典（Dictionary） 是哈希表的一种实现，提供了快速的查找、插入和删除操作。
在大多数情况下，查找、插入和删除操作的时间复杂度都是 O(1)。
然而，在最坏的情况下（例如，发生大量的哈希冲突），性能可能会下降 O(n)。

哈希表的核心思想是使用哈希函数将键（key）映射到一个数组（或其他类型的数据结构）的特定索引。
这个映射过程是通过哈希函数进行的，它接受一个键作为输入，并返回一个整数作为输出。这个整数就是数组的索引。
'''

# 使用花括号
my_dict = {'name': 'Alice', 'age': 30}
# 使用 dict() 构造函数
another_dict = dict(name='Bob', age=40)

# 输出
print(my_dict['name'])

# 修改键值对
my_dict['age'] = 31  
# 插入新键值对
my_dict['email'] = 'alice@email.com'

#删除键值对
del my_dict['age']

if 'name' in my_dict:
    print("Key exists.")

# 遍历所有的键
for key in my_dict.keys():
    print(key)

# 遍历所有的值
for value in my_dict.values():
    print(value)

# 遍历所有的键值对
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")