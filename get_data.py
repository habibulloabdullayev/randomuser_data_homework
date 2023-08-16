import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f = open(filename)
    x = f.read()
    return json.loads(x)
path = 'randomuser_data.json'
# print(get_data(path))