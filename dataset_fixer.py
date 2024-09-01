#fix yo dataset here
import string
import json
import re

replacements = {'ä': 'a', 'ö': 'o', 'ü': 'u', 'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'à': 'a', 'è': 'e', 'ì':'i', 'ò': 'o', 'ù': 'u', 'ừ': 'v', 'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ǎ': 'a', 'ǒ': 'o', 'ǔ': 'u', 'â': 'a', 'ê': 'e', '̀': ' ', 'ğ': 'g', 'ç': 'c', 'ş': 's', 'ậ': 'a', 'ệ': 'e', 'ộ': 'o', 'ố': 'o', 'ể': 'e', 'ạ': 'a', 'ṭ': 't', '—':' ', 'ṣ':'s', 'ḥ':'h', 'ɛ':' ', 'ě':'e', 'ë':'e', 'ã':'a', 'š':'s', 'å':'a', 'ñ':'n', 'ı':'i', 'о':'o', 'ï':'i', 'õ':'o', 'ß':'b', 'ý':'y', 'ś':'s', 'ṇ':'n', 'ẏ':'y', 'ṛ':'r', 'ṁ':'m', 'ô':'o', 'и':'i', 'α':'a', 'τ':'e', 'û':'u', 'î':'i', 'ḍ':'d', 'ẓ':'z', 'ṅ':'n', 'ḳ':'k', 'ŋ':'n', 'а':'a', 'т':'t', 'ь':'b', 'č':'k', 'ž':'z', 'ɪ':'i', 'ʊ':'o', 'ɡ':'g', 'ʌ':'l', 'ʃ':'s', 'θ':'t', 'ư':'u',  'е':'e', '̄':'', '“':'', '”':'', 'ˈ':'', 'ǐ':'l', '–':''}

num_replacements = { '0':'o', '1':'i', '2':'ii', '3':'iii','4':'iv', '5':'v', '6':'vi', '7':'vii', '8':'viii', '9':'ix'}

def replace_chars(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def replace_nums(text):
    for old, new in num_replacements.items():
        text = text.replace(old, new)
    return text


def replace_punctuation(text):
    for punct in string.punctuation:
        text = text.replace(punct, "")
    return text


def fix_da_data():
    with open('datasets/dataset.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    correct_data = []
    pesky_lil_piece_of_shi = []
    for sentence in data:

        if isinstance(sentence, list) and len(sentence) > 1:
            language_name = sentence[0].lower()
            holy_sentence = sentence[1].lower()
            holy_sentence = replace_chars(holy_sentence)
            holy_sentence = replace_nums(holy_sentence)
            holy_sentence = replace_punctuation(holy_sentence)
            holy_sentence = holy_sentence.replace("\n", "")
            holy_sentence = " ".join(holy_sentence.split())
            if re.match(r'^[a-z ]+$', holy_sentence) and holy_sentence and not holy_sentence.isspace():
                correct_data.append([language_name, holy_sentence])
            else:
                for char in holy_sentence:
                    if not re.match(r'^[a-z ]+$', char):
                        pesky_lil_piece_of_shi += (char)


    with open("datasets/correct_data.json", mode='w', encoding='utf-8') as f:
        f.write(json.dumps(correct_data, indent=4, ensure_ascii=False))

    print(pesky_lil_piece_of_shi)
    return correct_data



fix_da_data()
