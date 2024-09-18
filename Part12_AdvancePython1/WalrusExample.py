# Without walrus operator:
items = [1, 2, 3, 4, 5]
squared1 = []
for item in items:
    square = item ** 2
    if square > 10:
        squared1.append(square)
print(f"Squared 1 : {squared1}")

# With walrus operator:
items = [1, 2, 3, 4, 5]
squared2 = [square for item in items if (square := item ** 2) > 10]
print(f"Squared 2: {squared2}")

# It's most beneficial in situations where you need to use a value immediately after computing it, 
# especially in conditional statements or loops.