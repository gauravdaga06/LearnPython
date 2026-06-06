age= 13;
if age >= 13 and age <= 19:
    print("You are a teenager.");
elif age >= 20:
    print("You are an adult.");
else:
    print("You are a child.");

names = ["Alice", "Bob", "Charlie", "David", "Eve"];

for name in names:
    print(name);

for i , name in enumerate(names):
    print(f"{i}: {name}");



for i in range(5):
    print(i);