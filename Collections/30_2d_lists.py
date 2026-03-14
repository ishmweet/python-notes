fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

#print(groceries[0])
#print(groceries[1][2])  #just like coordinates

for food in groceries:
    print(food, end=" ")
print()