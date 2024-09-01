#get yo topic here
import json
import random


with open('datasets/topics.json', 'r', encoding='utf-8') as file:
    data =json.load(file)

def get_random_topic():
    random_thingy = random.choice(data)
    return random_thingy['content']
#topic = get_random_topic()
#print(topic)









