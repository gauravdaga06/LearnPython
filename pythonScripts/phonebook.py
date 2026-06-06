phNum = {"John": "123-456-7890", "Jane": "987-654-3210", "Doe": "555-555-5555"}
for name, number in phNum.items():
    print(f"{name}: {number}")
print(phNum.get("Abe", "Not found"))
print(phNum.get("John", "Not found"))