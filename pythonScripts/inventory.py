fruits = {"apple" : 5.7, "banana" : 3.2, "orange" : 4.5, "grape" : 6.0}

def total_cost(prices):
    return sum(prices.values())

print(f"Total cost of fruits: {total_cost(fruits)}")

def expensive_items(prices , threshold):
    return [item for item, price in prices.items() if price > threshold]

print(f"Expensive items (cost > 5): {expensive_items(fruits, 5)}")



nums = [3,8,1,9,4,7]

def greater_than(arr, threshold):
    return [num for num in arr if num > threshold]

print(f"Numbers greater than 5: {greater_than(nums, 5)}")

price_in_cents = {fruit : int(price *100) for fruit, price in fruits.items()}
print(f"Price in cents: {price_in_cents}")

expensive = {fruit : price for fruit, price in fruits.items() if price > 5}
print(f"Expensive fruits: {expensive}")

length_of_fruits_name = {fruit: len(fruit) for fruit in fruits.keys()}
print(f"Length of fruit names: {length_of_fruits_name}")
        