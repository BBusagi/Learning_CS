#10 List Functions

lucky_numbers =[4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1,"Kelly")
friends.remove("Jim")
#friends.clear()
friends.pop()
print(friends)
print(friends.index("Kevin"))
friends.append("Kevin")
print(friends.count("Kevin"))
lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)