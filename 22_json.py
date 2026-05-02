import json

# Sample data to save into data.json
person = {
    "name": "Ali",
    "age": 25,
    "city": "Lahore",
    "languages": ["Python", "JavaScript", "SQL"],
    "is_student": False
}

file_name = "data.json"

# Write the Python data to data.json using json.dump
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4)

print(f"Data written to {file_name}")

# Read the JSON data back from data.json using json.load
with open(file_name, "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("Loaded data:")
print(loaded_data)
