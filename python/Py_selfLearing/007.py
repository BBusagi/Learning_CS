#007 列表推导式&生成器表达式
'''
列表推导式（List Comprehensions）
[expression for element in iterable if condition]

列表推导式 -> 列表 -> !!!方括号!!!

生成器表达式（Generator Expressions）
(expression for element in iterable if condition)

生成器表达式 -> 对象 -> !!!圆括号!!!
生成器是惰性求值（lazy evaluation），这意味着它只在需要时计算下一个值。

区别：
1. 内存使用：生成器表达式更内存高效，因为它们不一次性生成所有值。这在处理大数据集时特别有用。
2. 用途：列表推导式主要用于生成新的列表。生成器表达式则更多地用于迭代操作，不需要一次性生成所有数据。
3. 语法：两者的语法非常相似，主要区别在于使用的括号类型（方括号用于列表推导式，圆括号用于生成器表达式）。
'''

squares1 = [x*x for x in range(10)]
print(squares1)
print(min(squares1))

squares2 = (x*x for x in range(10))
print(squares2)
print(min(squares2))