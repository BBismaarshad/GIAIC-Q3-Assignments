import json

# Python to JSON
data = {'name': 'Ali', 'age': 30, 'city': 'Karachi'}
json_str = json.dumps(data)
print(json_str)  # '{"name": "Ali", "age": 30, "city": "karachi"}'

# JSON to Python
json_data = '{"name": "Ali", "age": 30, "city": "Karachi"}'
python_obj = json.loads(json_data)
print(python_obj['name'])  # 'John'