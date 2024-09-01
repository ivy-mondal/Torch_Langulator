import json
import torch
import torch.nn.functional as F


with open('datasets/correct_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


languages = [item[0] for item in data]
unique_langs = list(set(languages))
unique_langs = sorted(unique_langs)
#lines = [item[1] for item in datasets]
numerical_labels = [unique_langs.index(lang) for lang in languages]
tensor_labels = torch.tensor(numerical_labels)
tensor_Y = F.one_hot(tensor_labels, num_classes=len(unique_langs))
tensor_Y = tensor_Y.float()
print(unique_langs)
#print(unique_langs)
#print(numerical_labels)
#print(tensor_labels)
#print(tensor_Y)
    
