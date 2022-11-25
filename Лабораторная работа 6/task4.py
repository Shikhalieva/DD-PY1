import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    data = [data[_].split(",") for _ in range(len(data))]
    headers, objects = [data[0] for _ in range(len(data)-1)], []
    data.pop(0)
    for title in range(len(data)):
        dictionary = {}
        for value in range(len(data[title])):
            dictionary.update({headers[title][value]: data[title][value]})
        objects.append(dictionary)
    return objects


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
