inventory = [["Apple", 50, 0.75], ["Banana", 100, 0.50], ["Orange", 75, 0.80]]
# 1. ลดจำนวนเมื่อขาย
def update_inventory(inv, name, qty):
    for item in inv:
        if item[0] == name: item[1] -= qty
# 2. คำนวณราคารวม
def calculate_total_value(inv):
    return sum(q * p for _, q, p in inv)
# 3. หาของแพงสุด
def find_most_expensive(inv):
    return max(inv, key=lambda x: x[2])[0]
# 4. เพิ่มหรืออัปเดตสินค้า
def add_item(inv, name, qty, price):
    for item in inv:
        if item[0] == name:
            item[1], item[2] = qty, price
            return
    inv.append([name, qty, price])
# --- Actions ---
update_inventory(inventory, "Banana", 20)
print("Total Value:", calculate_total_value(inventory))
print("Most Expensive:", find_most_expensive(inventory))

add_item(inventory, "Eggs", 30, 0.25)
add_item(inventory, "Eggs", 50, 0.30)
print("Updated Inventory:", inventory)