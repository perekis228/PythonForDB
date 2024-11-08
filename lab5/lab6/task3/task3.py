from pprint import pprint
from lxml import etree
tree = etree.parse('ex_3.xml')
root = tree.getroot()

items = []
for item in root[1][1]:
    if item.tag == 'СведТов':
        items.append({'name': item.get('НаимТов'),
                      'quantity': int(item.get('КолТов')),
                      'price': float(item.get('ЦенаТов'))})

pprint(items)