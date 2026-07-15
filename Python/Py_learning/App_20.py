#20 For Loop

for letter in "Giraffe Academy":
# 动态类型（dynamically-typed）自动推断变量类型
    print(letter)

friends =["Jim", "Karen", "Kevin"]
for name in friends:
    print(name)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

#friends =["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")