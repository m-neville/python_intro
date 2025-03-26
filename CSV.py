import csv

# Data to be written
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 28, "Chicago"]
]

# Writing to a CSV file
with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Writes multiple rows
