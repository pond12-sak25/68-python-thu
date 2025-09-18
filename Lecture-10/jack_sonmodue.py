import json
data = {"name": "John", "age": 30}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(parsed_data["name"])
print(parsed_data["age"])