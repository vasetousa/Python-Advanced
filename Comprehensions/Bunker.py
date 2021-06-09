categories = input().split(", ")
lines = int(input())
bunker = {category: [] for category in categories}

for line in range(lines):
    category, item_name, quantity_quality = input().split(' - ')
    quantity, quality = quantity_quality.split(";")
    quantity, quality = quantity.split(":")[1], quality.split(":")[1]
    quantity = int(quantity)
    quality = int(quality)
    bunker[category].append({'name': item_name, 'quantity': quantity, 'quality': quality})

total_items = sum([item['quantity'] for items in bunker.values() for item in items])
avg_quality = sum([item['quality'] for items in bunker.values() for item in items])
avg_quality /= len(categories)
print(f"Count of items: {total_items}")
print(f"Average quality: {avg_quality:.2f}")

print('\n'.join(
    f'{category} -> {", ".join(item["name"] for item in bunker[category])}'
    for category in categories
))