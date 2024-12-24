import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
np.random.seed(42)
n_samples = 30  # Dataset size
X = np.random.uniform(-1, 1, size=(n_samples, 1))
y = np.sin(2 * np.pi * X).ravel() + 0.3 * np.random.normal(size=n_samples)

# Weight decay values to analyze (L2 regularization strength)
weight_decay_values = [0.0, 0.1, 0.5, 1.0, 5.0]

# Initialize results
degrees = np.arange(1, 50)  # Model complexity: Polynomial degrees
results = {wd: {'train_errors': [], 'test_errors': [], 'train_r2': [], 'test_r2': []} 
           for wd in weight_decay_values}

# Iterate over weight decay values
for weight_decay in weight_decay_values:
    train_errors = []
    test_errors = []
    train_r2_scores = []
    test_r2_scores = []

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    for degree in degrees:
        poly = PolynomialFeatures(degree=degree)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)

        # Fit polynomial regression model with weight decay (Ridge regression)
        model = Ridge(alpha=weight_decay)  # Alpha controls the weight decay strength
        model.fit(X_train_poly, y_train)

        # Calculate train and test errors
        y_train_pred = model.predict(X_train_poly)
        y_test_pred = model.predict(X_test_poly)

        train_errors.append(mean_squared_error(y_train, y_train_pred))
        test_errors.append(mean_squared_error(y_test, y_test_pred))
        train_r2_scores.append(r2_score(y_train, y_train_pred))
        test_r2_scores.append(r2_score(y_test, y_test_pred))

    results[weight_decay]['train_errors'] = train_errors
    results[weight_decay]['test_errors'] = test_errors
    results[weight_decay]['train_r2'] = train_r2_scores
    results[weight_decay]['test_r2'] = test_r2_scores

# Plot MSE results
plt.figure(figsize=(12, 8))
for weight_decay in weight_decay_values:
    plt.plot(degrees, results[weight_decay]['test_errors'], label=f"Test Loss (Weight Decay={weight_decay})", marker='o')
    plt.plot(degrees, results[weight_decay]['train_errors'], linestyle='--', label=f"Train Loss (Weight Decay={weight_decay})")

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("Mean Squared Error (Log Scale)")
plt.yscale("log")
plt.title("Effect of Weight Decay Regularization on Double Descent (MSE)")
plt.legend()
plt.grid()
plt.show()

# Plot R2 results
plt.figure(figsize=(12, 8))
for weight_decay in weight_decay_values:
    plt.plot(degrees, results[weight_decay]['test_r2'], label=f"Test R² (Weight Decay={weight_decay})", marker='o')
    plt.plot(degrees, results[weight_decay]['train_r2'], linestyle='--', label=f"Train R² (Weight Decay={weight_decay})")

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("R² Score")
plt.title("Effect of Weight Decay Regularization on Double Descent (R²)")
plt.legend()
plt.grid()
plt.show()
