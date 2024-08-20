import string
import json
import re


replacements = {'ä': 'a', 'ö': 'o', 'ü': 'u', 'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u', 'ừ': 'v', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ǎ': 'a', 'ǒ': 'o', 'ǔ': 'u', 'â': 'a', 'ê': 'e', '̀': ' ', 'ğ': 'g', 'ç': 'c', 'ş': 's', 'ậ': 'a', 'ệ': 'e', 'ộ': 'o', 'ố': 'o', 'ể': 'e', 'ạ': 'a', 'ṭ': 't'}


def replace_chars(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def replace_punctuation(text):
    for punct in string.punctuation:
        text = text.replace(punct, " ")
    return text


def fix_da_data():
    with open('dataset.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    correct_data = []
    for sentence in data:

        if isinstance(sentence, list) and len(sentence) > 1:
            language_name = sentence[0].lower()
            holy_sentence = sentence[1].lower()
            holy_sentence = replace_chars(sentence[1])
            holy_sentence = replace_punctuation(holy_sentence)
            if  re.match(r'^[a-z ]+$', holy_sentence) and holy_sentence and not holy_sentence.isspace():
                correct_data.append([language_name, holy_sentence])

    with open("correct_data.json", mode='w', encoding='utf-8') as f:
        f.write(json.dumps(correct_data, indent=4, ensure_ascii=False))

    return correct_data


fix_da_data()
