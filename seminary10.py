import csv, json

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 24, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"}
]

# Determine fieldnames (headers) from the keys of the first dictionary
fieldnames = data[0].keys()

# To write to a CSV file
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(data) # Write all dictionary rows
print("Data written to output.csv")


# To generate a JSON string
json_string = json.dumps(data, indent=4)
print("JSON String:")
print(json_string)

# To write to a JSON file
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nData written to output.json")