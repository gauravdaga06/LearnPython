fruits = {"apple" : 5.7, "banana" : 3.2, "orange" : 4.5, "grape" : 6.0}

def total_cost(prices):
    return sum(prices.values())

print(f"Total cost of fruits: {total_cost(fruits)}")

def expensive_items(prices , threshold):
    return [item for item, price in prices.items() if price > threshold]

print(f"Expensive items (cost > 5): {expensive_items(fruits, 5)}")



nums = [3,8,1,9,4,7]

def greaterThan(arr, threshold):
    return [num for num in arr if num > threshold]

print(f"Numbers greater than 5: {greaterThan(nums, 5)}")
        