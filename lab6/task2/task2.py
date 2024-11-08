import xmltodict
import pprint

with open('ex_2.xml', 'r', encoding='utf-8') as file:
    xml_string = file.read()

result_dict = xmltodict.parse(xml_string)
result_dict['PrintData']['Detail']['Item'].append({
    'ArtName': 'Алёнка',
    'Barcode': '2000000000221',
    'QNT': '110,5',
    'QNTPack': '110,5',
    'QNTRows': '13',
    'SN1': '00000007',
    'SN2': '06.11.2024',
    'Unit': 'шт'
})
summary = 0
rows = 0
for elem in result_dict['PrintData']['Detail']['Item']:
    qnt = elem['QNT'].replace(',', '.')
    summary += float(qnt)
    rows += int(elem['QNTRows'])
result_dict['PrintData']['Summary']['Summ'] = str(summary)
result_dict['PrintData']['Summary']['SummRows'] = str(rows)
pprint.pprint(result_dict)

with open('ex_2_new.xml', 'w', encoding='utf-8') as file:
    file.write(xmltodict.unparse(result_dict, pretty=True))