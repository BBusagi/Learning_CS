#002 栈
'''
在Python中，栈（Stack）是一种后进先出（LIFO, Last-In-First-Out）的数据结构，
最后一个添加的元素总是第一个被移除的。
Python的列表（List）和内置的数据结构collections.deque都可以用来实现栈。
'''

# 使用列表实现栈
stack = []

# 入栈（Push）
stack.append(1)
stack.append(2)
stack.append(3)

# 出栈（Pop）
print(stack.pop())  # 输出 3
print(stack.pop())  # 输出 2
print(stack.pop())  # 输出 1