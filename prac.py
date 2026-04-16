# Counting Trees
""" def count_trees(amt, height):
    current_increase_streak = 1
    current_decrease_streak = 2
    largest_increase_streak = 1
    largest_decrease_streak = 1

    for track in range(int(amt) - 1):

        if height[track] < height[track+1]:
            current_increase_streak += 1
            if current_decrease_streak > largest_decrease_streak:
                largest_decrease_streak = current_decrease_streak
            current_decrease_streak = 1 

        if height[track] > height[track+1]:
            current_decrease_streak += 1
            if current_increase_streak > largest_increase_streak:
                largest_increase_streak = current_increase_streak
            current_increase_streak = 1

    print(largest_increase_streak)
    print(largest_decrease_streak)
count_trees(4, [1,3,4,2]) """

#Sushi Receipt
sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt_order(orders):
    receipt = {}
    for order in orders:
        if order["name"] in receipt:
            receipt[order["name"]]["quantity"] += 1
        else:
            receipt[order["name"]] = {
                "price":order["price"],
                "quantity" : 1
            }

    for sushi, value in receipt.items():
        price = value["price"] * value["quantity"]
        print(sushi, price)
receipt_order(sushi_orders)

#Doctors Problem
""" wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff_dict = {}

for dept, staff_mem in wards.items():
    for staff in staff_mem:
        if staff in staff_dict:
            staff_dict[staff].append(dept)
        else:
            staff_dict[staff] = [dept]

print(staff_dict) """