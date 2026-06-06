def describe_person(name, age, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}."

print(describe_person("Alice", 30, "New York"))
print(describe_person("Bob", 25))