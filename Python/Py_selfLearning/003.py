#003 内置排序算法_Timsort
'''
在 Python 中，sort 是列表（list）对象的一个内置方法，用于就地（in-place）排序列表。
这个方法使用 Timsort 算法，稳定 时间复杂度 O(nlogn)

sort 方法会直接修改原列表
sorted() 函数，返回一个新的排序列表
'''

#示例
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print(my_list)                  #[1, 1, 2, 3, 4, 5, 5, 6, 9]

my_list.sort(reverse=True)      #降序排序
print(my_list)                  #[9, 6, 5, 5, 4, 3, 2, 1, 1]

sorted_list = sorted(my_list)
print(sorted_list)              #[1, 1, 2, 3, 4, 5, 5, 6, 9]
