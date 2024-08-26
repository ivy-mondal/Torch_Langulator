import json


with open('correct_data.json', 'r', encoding= 'utf-8') as file:
    data = json.load(file)


def mapping_data():
    languages = [item[0] for item in data]
    lines = [item[1] for item in data]
    how_many_lang = list(set(languages))
    lang_to_num = {lang:i for i,  lang in enumerate(languages)}
    
