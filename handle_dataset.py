import torch
import string
import json


def make_tensor_dataset(dataset_name: str):
    with open("datasets//" + dataset_name + "_data.json", 'r', encoding='utf-8') as file:
        data = json.load((file))
    languages = [item[0] for item in data]
    lines = [item[1] for item in data]
    unique_langs = sorted(list(set(languages)))
    unique_chars = sorted(list(string.ascii_lowercase + ' '))

    one_hot_samples_X = []
    one_hot_samples_Y = []

    for line in lines:
        examples = []
        language = languages[lines.index(line)]
        for i in range(0, len(line), 16):
            sample = line[i:i + 16]
            if len(sample) == 16:
               examples.append(sample)
            else:
                pass

            for sample in examples:

                one_hot_vector_X = torch.zeros(len(sample), len(unique_chars))
                one_hot_vector_Y = torch.zeros(len(unique_langs))

                for j, char in enumerate(sample):
                    char_index = unique_chars.index(char.lower())
                    lang_index = unique_langs.index(language)
                    one_hot_vector_X[j, char_index] = 1
                    one_hot_vector_Y[lang_index] = 1
                    one_hot_samples_X.append(one_hot_vector_X)
                    one_hot_samples_Y.append(one_hot_vector_Y)




    X_tensor = torch.stack(one_hot_samples_X)
    Y_tensor = torch.stack(one_hot_samples_Y)
    print(X_tensor.shape)
    print(Y_tensor.shape)

    return X_tensor, Y_tensor

print(make_tensor_dataset("test"))
