#23 Build a Translator

def translate(phrase):
    translation = ""
    for letter in phrase:
#       if letter in "AEIOUaeiou":
#       原版，改进前
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else :
            translation = translation + letter
    return translation

#第二版，添加了大小写辨识，改写后同步大小写
def translate2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else :
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
print(translate2(input("Enter a phrase: ")))