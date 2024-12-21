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

# Dropout rates to analyze
dropout_rates = [0.0, 0.1, 0.2, 0.3, 0.4]

# Initialize results
degrees = np.arange(1, 50)
n_trials = 10
results = {rate: {'train_means': [], 'test_means': [], 'test_vars': []} for rate in dropout_rates}

# Function to simulate dropout (artificially setting weights to zero)
def apply_dropout(data, rate):
    mask = np.random.binomial(1, 1 - rate, size=data.shape)
    return data * mask

for dropout_rate in dropout_rates:
    train_errors_trials = []
    test_errors_trials = []

    for _ in range(n_trials):
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=np.random.randint(1000))

        train_errors = []
        test_errors = []

        for degree in degrees:
            poly = PolynomialFeatures(degree=degree)
            X_train_poly = apply_dropout(poly.fit_transform(X_train), dropout_rate)
            X_test_poly = apply_dropout(poly.transform(X_test), dropout_rate)

            model = Ridge(alpha=0.0)
            model.fit(X_train_poly, y_train)

            y_train_pred = model.predict(X_train_poly)
            y_test_pred = model.predict(X_test_poly)

            train_errors.append(mean_squared_error(y_train, y_train_pred))
            test_errors.append(mean_squared_error(y_test, y_test_pred))

        train_errors_trials.append(train_errors)
        test_errors_trials.append(test_errors)

    # Calculate means and variances
    results[dropout_rate]['train_means'] = np.mean(train_errors_trials, axis=0)
    results[dropout_rate]['test_means'] = np.mean(test_errors_trials, axis=0)
    results[dropout_rate]['test_vars'] = np.var(test_errors_trials, axis=0)

# Plot results
plt.figure(figsize=(12, 8))
for dropout_rate in dropout_rates:
    plt.plot(degrees, results[dropout_rate]['test_means'], label=f"Test Loss (Dropout={dropout_rate})", marker='o')
    plt.fill_between(degrees,
                     results[dropout_rate]['test_means'] - np.sqrt(results[dropout_rate]['test_vars']),
                     results[dropout_rate]['test_means'] + np.sqrt(results[dropout_rate]['test_vars']),
                     alpha=0.2)

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("Mean Squared Error (Log Scale)")
plt.yscale("log")
plt.title("Effect of Dropout Regularization on Double Descent")
plt.legend()
plt.grid()
plt.show()
