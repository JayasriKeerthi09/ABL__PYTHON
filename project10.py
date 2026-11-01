REORDER_LEVEL = 10
products = [
    ("P101", 250.0, 40),
    ("P102", 99.5, 5),
    ("P103", -50.0, 20),
    ("P104", 120.0, -3),
    ("", 75.0, 15),
    ("P106", 500.0, 8),
    ("P107", "abc", 12),
    ("P108", 35.0, 0),
    ("P109", 800.0, 25),
    ("P110", 60.0),
]
def is_valid(record):
    if len(record) != 3:
        return False
    product_id, price, stock = record
    if not isinstance(product_id, str) or product_id.strip() == "":
        return False
    if not isinstance(price, (int, float)) or price <= 0:
        return False
    if not isinstance(stock, int) or stock < 0:
        return False
    return True
valid_products = []
invalid_products = []
for record in products:
    if is_valid(record):
        valid_products.append(record)
    else:
        invalid_products.append(record)
total_inventory_value = 0
print("=== INVENTORY VALUE PER PRODUCT ===")
print(f"{'ID':<8}{'Price':>10}{'Stock':>8}{'Value':>12}")
for product_id, price, stock in valid_products:
    value = price * stock
    total_inventory_value += value
    print(f"{product_id:<8}{price:>10.2f}{stock:>8}{value:>12.2f}")
print(f"\nTotal Inventory Value: {total_inventory_value:.2f}")
print("\n=== ITEMS NEEDING REPLENISHMENT ===")
needs_restock = []
for product_id, price, stock in valid_products:
    if stock < REORDER_LEVEL:
        needs_restock.append((product_id, stock))
if needs_restock:
    for product_id, stock in needs_restock:
        status = "OUT OF STOCK" if stock == 0 else "LOW STOCK"
        print(f"{product_id}: {stock} units left -> {status}")
else:
    print("All products have enough stock.")
print("\n=== INVALID RECORDS ===")
for record in invalid_products:
    print(record)
print("\n=== AUDIT SUMMARY ===")
print(f"Total records checked : {len(products)}")
print(f"Valid records         : {len(valid_products)}")
print(f"Invalid records       : {len(invalid_products)}")
print(f"Items to replenish    : {len(needs_restock)}")