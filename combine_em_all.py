import random
from get_yo_topics_here import get_random_topic
from get_yo_lines_here import get_lines
from transliterate_yo_lines_here import transliterate

lang_list = ["Bengali", "Russian", "English", "Mandarin", "Spanish", "Hindi", "Arabic", "Japanese", "Korean", "French", "German", "Italian", "Portuguese", "Dutch", "Greek", "Swedish", "Turkish", "Swahili", "Vietnamese", "Thai", "Indonesian"]


def things_I_do_to_get_dataset():
    topic = get_random_topic()
    language = random.choice(lang_list)
    yo_sentence = get_lines(topic, language)
    yo_data = transliterate(yo_sentence)
    return [language, yo_data]


def now_do_it_10_times():
    result = []
    for i in range(10):
        data = things_I_do_to_get_dataset()
        result.append(data)
    return result


print(now_do_it_10_times())
