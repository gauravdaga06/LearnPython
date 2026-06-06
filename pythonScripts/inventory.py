fruits = {"apple" : 5.7, "banana" : 3.2, "orange" : 4.5, "grape" : 6.0}

def total_cost(prices):
    return sum(prices.values())

print(f"Total cost of fruits: {total_cost(fruits)}")

def expensive_items(prices , threshold):
    expensive = []
    for item, price in prices.items():
        if price > threshold:
            expensive.append(item)
    return expensive

print(f"Expensive items (cost > 5): {expensive_items(fruits, 5)}")