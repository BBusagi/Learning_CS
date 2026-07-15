#4 Working With Strings

print("Giraffe \nAcademy")

phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower())

print("islower:", phrase.islower())
print("isupper:", phrase.isupper())

print(phrase.upper())
print(phrase.upper().isupper())

#phrase = "Giraffe Academy"
#          0123456789
print("word:",phrase[0])
print("index:",phrase.index("f"))
print("index:",phrase.index("Aca"))
#print("index:",phrase.index("z"))

print("replace:",phrase.replace("Giraffe", "Elephant"))