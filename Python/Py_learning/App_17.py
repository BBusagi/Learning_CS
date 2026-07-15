#17 Dictionaries

monthConversions = {
#   "Key": "Value",
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Mar"))

print(monthConversions["Luv"])
print(monthConversions.get("Luv"))
#default value
print(monthConversions.get("Luv","Not a valid Key"))