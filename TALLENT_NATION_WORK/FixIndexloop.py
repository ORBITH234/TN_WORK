# Implement get_item(items, index). Return the item at the given index. 
# If the index is outside the list, return Index out of range. 
# Negative indexes should also return Index out of range for this challenge.

def get_item(items, index):
    # Bug to fix: invalid indexes should not crash the program.
    if index < 0 or index >= len(items):
        return "Index out of range"
    return items[index]


# use ths to tes the code 
colors = ["red", "green", "blue"]

print(get_item(colors, 0))   # Output: "green"
print(get_item(colors, -1))  # Output: "Index out of range"
print(get_item(colors, 5))   # Output: "Index out of range"