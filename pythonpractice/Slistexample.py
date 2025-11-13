# When to use: ➡️ When you need to store items in order, and duplicates are okay.

# Creating a list of groceries
groceries = [1, "Apple", "Bread", 2, "Cucumber", "Carrot", 3, "Dal", "Franky"]

print("Groceries are:", groceries)

print("1st Grocery:", groceries[0])
print("3rd Grocery:", groceries[2])
groceries.append("Milk")
groceries.append("orange")
print("2nd Grocery:", groceries[2])
print("2nd Grocery:", groceries)
groceries[0]="kiwi"
print("3rd Grocery:", groceries)
