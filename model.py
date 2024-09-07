# Let's build neural network :)
import torch.nn as nn
from handle_dataset import make_tensor_dataset


class Langulator(nn.Module):
    def __init__(self, total_characters = 27, embedding_size = 4, context_size = 16, neuron_num = 10, lang_num = 21):
        super().__init__()

        # character embeddings layer
        self.embedding = nn.Linear(total_characters, embedding_size)
        # middle layer
        self.middle = nn.Linear(context_size*embedding_size, neuron_num)
        #Last layer
        self.classifier = nn.Linear(neuron_num, lang_num)
        self.relu = nn.ReLU()
        #self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        x = self.relu(self.embedding(x))
        x = x.view(x.size(0), -1)
        x = self.relu(self.middle(x))
        x = self.classifier(x)

        return x





model = Langulator()
X, Y = make_tensor_dataset('test')#get yo data
output = model(X)