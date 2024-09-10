import matplotlib.pyplot as plt
import torch


def train_lil_dura(model, x_train, y_train, x_test, y_test, epochs, learning_rate):
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = torch.nn.CrossEntropyLoss()

    train_losses = []
    test_losses = []

    for epoch in range(epochs):
        model.train()
        outputs = model(x_train)
        train_loss = criterion(outputs, y_train)
        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        model.eval()

        with torch.no_grad():
            test_outputs = model(x_test)
            test_loss = criterion(test_outputs, y_test)

        train_losses.append(train_loss)
        test_losses.append(test_loss)

        print(f"round {epoch+1}/{epochs}, Train loss: {train_loss.item():.4f}, Test loss: {test_loss.item():.4f}")

    torch.save(model.state_dict(), "langulator_brain.pth")

    plt.plot(train_losses, label="Train Loss")
    plt.plot(test_losses, label="Test Loss")
    plt.xlabel('round')
    plt.ylabel('Loss')
    plt.title("pain and suffering of Durachok")
    plt.legend()
    plt.show()




