# time to suffer
from model import Langulator
from handle_dataset import make_tensor_dataset
from train import train_lil_dura
from train import ask_user

choice, checkpoint_name = ask_user()
x_train, y_train = make_tensor_dataset('train')
x_test, y_test = make_tensor_dataset('test')
model = Langulator()
epochs = 500
learning_rate = 0.005

if __name__ == "__main__":
    if choice == '2':
        train_lil_dura(model, x_train, y_train, x_test, y_test, epochs, learning_rate)
    elif choice == '1':
        train_lil_dura(model, x_train, y_train, x_test, y_test, epochs, learning_rate, checkpoint_name)
    else:
        print("Oops! Looks like you're still half asleep. Try again with 1 or 2!")
    # train_lil_dura(model, x_train, y_train, x_test, y_test, 500, 0.005)
