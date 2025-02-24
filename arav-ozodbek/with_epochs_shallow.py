import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
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
hidden_layer_size = 50  # Fixed model complexity
l2_weight = 0.00  # Moderate L2 regularization

# Store results
train_losses = []
test_losses = []

for epochs in epoch_counts:
    # Build the model
    model = Sequential([
        Dense(hidden_layer_size, input_dim=1, activation='relu', kernel_regularizer=l2(l2_weight)),
        Dense(1, activation='sigmoid', kernel_regularizer=l2(l2_weight))
    ])

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=epochs, verbose=0, batch_size=16)

    # Evaluate the model
    train_loss, _ = model.evaluate(X_train, y_train, verbose=0)
    test_loss, _ = model.evaluate(X_test, y_test, verbose=0)

    # Log the results
    train_losses.append(train_loss)
    test_losses.append(test_loss)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(epoch_counts, train_losses, label='Train Loss', marker='o')
plt.plot(epoch_counts, test_losses, label='Test Loss', marker='o')
plt.xlabel('Number of Epochs')
plt.ylabel('Loss (Binary Crossentropy)')
plt.title('Epoch-wise Double Descent Behavior')
plt.legend()
plt.grid()
plt.show()
