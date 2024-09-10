import random
for i in range(10):
    meow_str = ""
    meow_str += "М" if random.random() < 0.5 else "м"
    meow_str += "Я" if random.random() < 0.5 else "я"
    meow_str += "У" if random.random() < 0.5 else "у"
    print(meow_str)
print("🐱")