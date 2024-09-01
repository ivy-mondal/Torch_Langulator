#combine em all to get datasets
import random
import json
from topic_gen import get_random_topic
from sentence_gen import get_lines
from transliterator import transliterate

lang_list = ["Bengali", "Russian", "English", "Mandarin", "Spanish", "Hindi", "Arabic", "Japanese", "Korean", "French", "German", "Italian", "Portuguese", "Dutch", "Greek", "Swedish", "Turkish", "Swahili", "Vietnamese", "Thai", "Indonesian"]


def things_I_do_to_get_dataset():
    topic = get_random_topic()
    language = random.choice(lang_list)
    yo_sentence = get_lines(topic, language)
    yo_data = transliterate(yo_sentence)
    return [language, yo_data]


def now_do_it_1000_times():
    result = []
    for i in range(1000):
        data = things_I_do_to_get_dataset()
        print(data, i)
        result.append(data)
        with open("datasets/dataset.json", mode='w', encoding='utf-8') as f:
            f.write(json.dumps(result, indent=4,  ensure_ascii=False))
    return result

now_do_it_1000_times()

#print(now_do_it_10_times())
