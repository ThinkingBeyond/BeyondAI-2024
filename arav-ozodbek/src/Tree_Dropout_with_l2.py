import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
np.random.seed(42)
n_samples = 30
X = np.random.uniform(-1, 1, size=(n_samples, 1))
y = np.sin(2 * np.pi * X).ravel() + 0.3 * np.random.normal(size=n_samples)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Parameters to explore
degrees = np.arange(1, 50)
dropout_rates = [0.0, 0.1, 0.2, 0.3, 0.4]
alphas = [0.0, 0.1, 0.5, 1.0]  # L2 regularization levels

# Initialize data storage for results
results = {}

# Compute results for each combination of dropout and L2 regularization
for alpha in alphas:
    results[alpha] = {}
    for dropout_rate in dropout_rates:
        train_errors = []
        test_errors = []
        for degree in degrees:
            # Polynomial features
            poly = PolynomialFeatures(degree=degree)
            X_train_poly = poly.fit_transform(X_train)
            X_test_poly = poly.transform(X_test)

            # Apply dropout by randomly zeroing out features
            if dropout_rate > 0:
                mask = np.random.binomial(1, 1 - dropout_rate, X_train_poly.shape)
                X_train_poly = X_train_poly * mask

            # Ridge regression model
            model = Ridge(alpha=alpha)
            model.fit(X_train_poly, y_train)

            # Calculate errors
            y_train_pred = model.predict(X_train_poly)
            y_test_pred = model.predict(X_test_poly)
            train_errors.append(mean_squared_error(y_train, y_train_pred))
            test_errors.append(mean_squared_error(y_test, y_test_pred))

        # Store errors for current combination
        results[alpha][dropout_rate] = {
            "train_errors": train_errors,
            "test_errors": test_errors,
        }

# Plot results
fig, axes = plt.subplots(len(alphas), 1, figsize=(10, 10), sharex=True)
for i, alpha in enumerate(alphas):
    ax = axes[i]
    for dropout_rate in dropout_rates:
        test_errors = results[alpha][dropout_rate]["test_errors"]
        ax.plot(
            degrees,
            test_errors,
            label=f"Dropout={dropout_rate}",
            marker="o",
            linestyle="-",
        )
    ax.set_yscale("log")
    ax.set_title(f"L2 Regularization (Alpha={alpha})")
    ax.set_xlabel("Model Complexity (Polynomial Degree)")
    ax.set_ylabel("MSE (Log Scale)")
    ax.legend()
    ax.grid()

plt.tight_layout()
plt.show()
