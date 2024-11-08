import json
import jsonschema

def is_valid(json_file, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)

    with open(json_file) as f:
        data = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)
        print("Данные валидны")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Ошибка валидации: {err.message}")

is_valid('ex_1.json', 'schema.json')
is_valid('ex_1_err.json', 'schema.json')