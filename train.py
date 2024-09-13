import matplotlib.pyplot as plt
import torch


def train_lil_dura(model, x_train, y_train, x_test, y_test, epochs, learning_rate):
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = torch.nn.CrossEntropyLoss()

    train_losses = []
    test_losses = []
    train_accuracies = []
    test_accuracies = []

    for epoch in range(epochs):
        model.train()
        outputs = model(x_train)
        train_loss = criterion(outputs, y_train)
        _, train_predicted_class_indices = torch.max(outputs, 1)
        _, train_actual_class_indices = torch.max(y_train, 1)
        train_accuracy = (train_predicted_class_indices == train_actual_class_indices).float().mean().item()

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        model.eval()

        with torch.no_grad():
            test_outputs = model(x_test)
            test_loss = criterion(test_outputs, y_test)
            _, test_predicted_class_indices = torch.max(test_outputs, 1)
            _, test_actual_class_indices = torch.max(y_test, 1)
            test_accuracy = (test_predicted_class_indices == test_actual_class_indices).float().mean().item()

        train_losses.append(train_loss.item())
        test_losses.append(test_loss.item())
        train_accuracies.append(train_accuracy)
        test_accuracies.append(test_accuracy)

        print(f"round {epoch + 1}/{epochs}, Train loss: {train_loss.item():.4f}, Test loss: {test_loss.item():.4f}", flush=True)

        if (epoch + 1) % 100 == 0:
            torch.save(model.state_dict(), f"langulator_brain_epoch_{epoch + 1}.pth")

            plt.clf()  # Clear the current figure

            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

            ax1.plot(train_losses, label="Train Loss")
            ax1.plot(test_losses, label="Test Loss")
            ax1.set_xlabel(f'round: {epoch + 1}')
            current_lr = optimizer.param_groups[0]['lr']
            ax1.set_ylabel(f'Loss at Learning Rate: {current_lr:.6f}')
            ax1.set_title("pain and suffering of Durachok")
            ax1.legend()

            ax2.plot(train_accuracies, label="Train Loss")
            ax2.plot(test_accuracies, label="Test Loss")
            ax2.set_xlabel(f'round: {epoch + 1}')
            current_lr = optimizer.param_groups[0]['lr']
            ax2.set_ylabel(f'accuracy at Learning Rate: {current_lr:.6f}')
            ax2.set_title("moments of glory(dw atleast you tried)")
            ax2.legend()

            plt.tight_layout()
            plt.show()

            torch.save(model.state_dict(), "langulator_brain.pth")

    # Final plot
    plt.clf()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

    ax1.plot(train_losses, label="Train Loss")
    ax1.plot(test_losses, label="Test Loss")
    ax1.xlabel(f'Epoch: {epochs}')
    current_lr = optimizer.param_groups[0]['lr']
    ax1.ylabel(f'Loss at Learning Rate: {current_lr:.6f}')
    ax1.title("The Epic Saga of Durachok's Pain and Suffering")
    ax1.legend()

    ax2.plot(train_accuracies, label="Train Accuracy")
    ax2.plot(test_accuracies, label="Test Accuracy")
    ax2.set_xlabel(f'Epoch: {epochs}')
    ax2.set_ylabel('Accuracy')
    ax2.set_title("Durachok's Moments of Glory (Now with actual glory!)")
    ax2.legend()

    plt.tight_layout()
    plt.show()
    torch.save(model.state_dict(), "langulator_brain.pth")
