fruits = ["Apple", "Oranges", "Mango", "Pineapple", "Oranges"]

unique = []

for item in fruits:
    if item not in unique:
        unique.append(item)

print(f"your unique numbers are  {unique}")
