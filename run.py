# time to suffer
from model import Langulator
from handle_dataset import make_tensor_dataset
from train import train_lil_dura

x_train, y_train = make_tensor_dataset('train')
x_test, y_test = make_tensor_dataset('test')
model = Langulator()

if __name__ == "__main__":
    train_lil_dura(model, x_train, y_train, x_test, y_test, 100, 0.001)
