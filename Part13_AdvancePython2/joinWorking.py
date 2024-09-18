# Creates a string from iterable objects.

l = ["Python", "Java", "DevOps", "YAML"]
joinedString = ":".join(l)
print(joinedString)
joinedString = " and ".join(l)
print(joinedString)

# Format(), since f"" is present in python, we rarely use format()
# We can use it this way if needed:
print("{} is a good {}".format("Raj","Boy"))
print("{1} is a good {0}".format("Raj","Boy"))
