import get_data
import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    s = []
    results = data['results']
    for i in results:
        s.append(i['email'])
    return s
print(get_email(get_data.get_data('randomuser_data.json')))