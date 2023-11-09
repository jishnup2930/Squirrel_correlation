import json

def load_data(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

data = load_data('journal.json')
print(data)
