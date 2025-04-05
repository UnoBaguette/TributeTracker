def calculate_total_value(items):
    total_value = sum(item['value'] for item in items)
    return total_value

def calculate_category_totals(items):
    category_totals = {}
    for item in items:
        category = item['category']
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += item['value']
    return category_totals