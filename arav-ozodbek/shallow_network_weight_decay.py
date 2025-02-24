import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.regularizers import l2

# Generate synthetic dataset
np.random.seed(42)
n_samples = 100  # Larger dataset for better training
X = np.random.uniform(-1, 1, size=(n_samples, 1))
y = (np.sin(2 * np.pi * X).ravel() + 0.7 * np.random.normal(size=n_samples)) > 0  # Binary classification

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurations for the experiment
epoch_counts = [250, 500, 1000,1500, 2000, 2500,3000,3500,4000, 4500]  # Range of training epochs
weight_decay_values = [0.0, 0.01, 0.1, 0.5, 1.0]  # Different weight decay values
hidden_layer_size = 50  # Fixed model complexity

# Store results
results = {}

for weight_decay in weight_decay_values:
    train_losses, test_losses = [], []
    train_accuracies, test_accuracies = [], []

    for epochs in epoch_counts:
        # Build the model
        model = Sequential([
            Dense(hidden_layer_size, input_dim=1, activation='relu', kernel_regularizer=l2(weight_decay)),
            Dense(1, activation='sigmoid', kernel_regularizer=l2(weight_decay))
        ])

        # Compile the model
        model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

        # Train the model
        model.fit(X_train, y_train, epochs=epochs, verbose=0, batch_size=16)

        # Evaluate the model
        train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
        test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

        # Log the results
        train_losses.append(train_loss)
        test_losses.append(test_loss)
        train_accuracies.append(train_acc)
        test_accuracies.append(test_acc)

    # Store results for the current weight decay value
    results[weight_decay] = {
        'train_losses': train_losses,
        'test_losses': test_losses,
        'train_accuracies': train_accuracies,
        'test_accuracies': test_accuracies
    }

# Plot Loss
plt.figure(figsize=(10, 6))
for weight_decay in weight_decay_values:
    plt.plot(epoch_counts, results[weight_decay]['test_losses'], label=f"Test Loss (Weight Decay={weight_decay})", marker='o')
    plt.plot(epoch_counts, results[weight_decay]['train_losses'], linestyle='--', label=f"Train Loss (Weight Decay={weight_decay})")

plt.xlabel('Number of Epochs')
plt.ylabel('Loss (Binary Crossentropy)')
plt.title('Effect of Weight Decay Regularization on Loss')
plt.legend()
plt.grid()
plt.show()

# Plot Accuracy
plt.figure(figsize=(10, 6))
for weight_decay in weight_decay_values:
    plt.plot(epoch_counts, results[weight_decay]['test_accuracies'], label=f"Test Accuracy (Weight Decay={weight_decay})", marker='o')
    plt.plot(epoch_counts, results[weight_decay]['train_accuracies'], linestyle='--', label=f"Train Accuracy (Weight Decay={weight_decay})")

plt.xlabel('Number of Epochs')
plt.ylabel('Accuracy')
plt.title('Effect of Weight Decay Regularization on Accuracy')
plt.legend()
plt.grid()
plt.show()
