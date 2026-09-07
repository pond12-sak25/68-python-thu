# Inventory เริ่มต้น
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# -----------------------------
# 1) Update Inventory
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            if item[1] < 0:
                item[1] = 0
            return
    print(f"{item_name} not found in inventory.")

# -----------------------------
# 2) Calculate Total Value
def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]  # quantity * price
    return total

# -----------------------------
# 3) Find Most Expensive Item
def find_most_expensive(inventory):
    if not inventory:
        return None
    most_exp = max(inventory, key=lambda x: x[2])  # หา item ที่มีราคาแพงสุด
    return most_exp[0]

# -----------------------------
# 4) Add or Update Item
def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])

# -----------------------------
# Actions ตามโจทย์
print("เริ่มต้น:", inventory)

# 1. Update inventory after selling 20 bananas
update_inventory(inventory, "Banana", 20)
print("หลังขายกล้วย 20 ลูก:", inventory)

# 2. Calculate total value
total_value = calculate_total_value(inventory)
print("มูลค่ารวมทั้งหมด:", total_value)

# 3. Find the most expensive item
most_exp_item = find_most_expensive(inventory)
print("ผลไม้ที่แพงที่สุดคือ:", most_exp_item)

# 4. Add "Eggs" with 30 units at 0.25, then update to 50 units at 0.30
add_item(inventory, "Eggs", 30, 0.25)
print("เพิ่มไข่:", inventory)

add_item(inventory, "Eggs", 50, 0.30)
print("อัปเดตไข่:", inventory)