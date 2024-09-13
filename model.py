# Let's build neural network :)
import torch.nn as nn
from handle_dataset import make_tensor_dataset


class Langulator(nn.Module):
    def __init__(self, total_characters=27, embedding_size=10, context_size=32, neuron_num=90, lang_num=21):
        super().__init__()

        # character embeddings layer
        self.embedding = nn.Linear(total_characters, embedding_size)
        # middle layer
        self.middle = nn.Linear(context_size * embedding_size, neuron_num)
        # Last layer
        self.classifier = nn.Linear(neuron_num, lang_num)
        self.relu = nn.ReLU()
        # self.bn = nn.BatchNorm1d
        # self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.embedding(x)
        # print(x.shape)
        x = x.view(x.size(0), -1)
        # print(x.shape)
        x = self.relu(self.middle(x))
        # print(x.shape)
        x = self.classifier(x)
        # print(x.shape)

        return x

# model = Langulator()
# X, Y = make_tensor_dataset('test')#get yo data
# output = model(X)
