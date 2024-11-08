import json

with open('ex_3.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
item1 = {'name': 'sword', 'price': 300.0, 'quantity': 1}
item2 = {'name': 'bread', 'price': 5.0, 'quantity': 10}
data['invoices'].append({'id': 3,
                         'total': sum(item['price'] * item['quantity'] for item in (item1, item2)),
                         'items': [item1, item2]})

with open('ex_3_new.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)