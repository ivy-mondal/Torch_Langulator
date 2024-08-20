import json
import re


def fix_da_data():
    with open('dataset.json' , 'r' , encoding='utf-8') as file:
        data = json.load(file)

    correct_data =[]
    for sentence in data:
        if isinstance(sentence, list) and len(sentence) > 1:
            language_name = sentence[0]
            holy_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence[1])
            holy_sentence = ' '.join(holy_sentence.split())

            if holy_sentence and not holy_sentence.isspace():
                correct_data.append([language_name, holy_sentence])


    with open("correct_data.json", mode='w', encoding='utf-8') as f:
                f.write(json.dumps(correct_data, indent=4, ensure_ascii=False))

    return correct_data
fix_da_data()