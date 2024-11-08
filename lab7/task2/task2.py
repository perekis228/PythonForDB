import json

def format(json_read, json_write):
    with open(json_read, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(json_write, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data['users']:
        print(f'{item["name"]:<25}{item["phoneNumber"]}')

format('ex_2.json', 'ex_2_formatted.json')
read_json('ex_2_formatted.json')