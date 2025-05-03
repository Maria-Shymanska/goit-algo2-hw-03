import csv
import timeit
import BTrees
import pandas as pd  

def load_data(filename):
    items = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            }
            items.append(item)
    return pd.DataFrame(items)  # Return as DataFrame

# Initialize the OOBTree
oob_tree = BTrees.family64.OO.BTree()
dict_store = {}

# Function to add an item to OOBTree
def add_item_to_tree(item):
    oob_tree[item['ID']] = item

# Function to add an item to dict
def add_item_to_dict(item):
    dict_store[item['ID']] = item

# Function for range query in OOBTree
def range_query_tree(min_price, max_price):
    return [
        v for v in oob_tree.items(min_price, max_price)
        if min_price <= v[1]['Price'] <= max_price
    ]

# Function for range query in dict
def range_query_dict(min_price, max_price):
    return [
        v for v in dict_store.values()
        if min_price <= v['Price'] <= max_price
    ]

# Load data into DataFrame
df = load_data('generated_items_data.csv')

# Add items to both data structures
for _, item in df.iterrows():
    add_item_to_tree(item)
    add_item_to_dict(item)

# Measure time for OOBTree range queries
oob_time = timeit.timeit('range_query_tree(10, 100)', globals=globals(), number=100)

# Measure time for dict range queries
dict_time = timeit.timeit('range_query_dict(10, 100)', globals=globals(), number=100)

print(f"🔹 Total range_query time for OOBTree: {oob_time:.6f} seconds")
print(f"🔸 Total range_query time for Dict: {dict_time:.6f} seconds")






