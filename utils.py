import json
from class_Candidate import Candidate


def load_data(file_name):
    with open(file_name) as file:
        json.load(file)
    return file


def get_objects_list(added_list):
    list_objects = []
    for i in added_list:
        list_objects.append(
            Candidate(i['id'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills']))
    return list_objects
