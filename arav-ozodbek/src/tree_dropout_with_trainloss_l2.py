import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Generate synthetic dataset
np.random.seed(42)
n_samples = 30
X = np.random.uniform(-1, 1, size=(n_samples, 1))
y = np.sin(2 * np.pi * X).ravel() + 0.3 * np.random.normal(size=n_samples)

# Regularization parameters
dropout_rates = [0.0, 0.1, 0.2, 0.3, 0.4]
l2_weights = [0.0, 0.1, 0.5, 1.0, 5.0]

# Initialize results
degrees = np.arange(1, 50)
results = {(dropout_rate, l2_weight): {'train_errors': [], 'test_errors': [], 'train_r2': [], 'test_r2': []} 
           for dropout_rate in dropout_rates for l2_weight in l2_weights}

# Function to simulate dropout (artificially setting weights to zero)
def apply_dropout(data, rate):
    mask = np.random.binomial(1, 1 - rate, size=data.shape)
    return data * mask

# Iterate over dropout rates and L2 regularization values
for dropout_rate in dropout_rates:
    for l2_weight in l2_weights:
        train_errors = []
        test_errors = []
        train_r2_scores = []
        test_r2_scores = []

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

        for degree in degrees:
            poly = PolynomialFeatures(degree=degree)
            X_train_poly = apply_dropout(poly.fit_transform(X_train), dropout_rate)
            X_test_poly = apply_dropout(poly.transform(X_test), dropout_rate)

            model = Ridge(alpha=l2_weight)  # Combine L2 and dropout
            model.fit(X_train_poly, y_train)

            y_train_pred = model.predict(X_train_poly)
            y_test_pred = model.predict(X_test_poly)

            train_errors.append(mean_squared_error(y_train, y_train_pred))
            test_errors.append(mean_squared_error(y_test, y_test_pred))
            train_r2_scores.append(r2_score(y_train, y_train_pred))
            test_r2_scores.append(r2_score(y_test, y_test_pred))

        results[(dropout_rate, l2_weight)]['train_errors'] = train_errors
        results[(dropout_rate, l2_weight)]['test_errors'] = test_errors
        results[(dropout_rate, l2_weight)]['train_r2'] = train_r2_scores
        results[(dropout_rate, l2_weight)]['test_r2'] = test_r2_scores

# Plot MSE results
fig, axs = plt.subplots(len(l2_weights), 1, figsize=(15, 4 * len(l2_weights)), sharex=True)
for i, l2_weight in enumerate(l2_weights):
    ax = axs[i]
    for dropout_rate in dropout_rates:
        train_errors = results[(dropout_rate, l2_weight)]['train_errors']
        test_errors = results[(dropout_rate, l2_weight)]['test_errors']
        
        ax.plot(degrees, test_errors, label=f"Test Loss (Dropout={dropout_rate})", marker='o')
        ax.plot(degrees, train_errors, linestyle='--', label=f"Train Loss (Dropout={dropout_rate})")
    
    ax.set_yscale("log")
    ax.set_title(f"L2 Regularization (Alpha={l2_weight})")
    ax.set_ylabel("MSE (Log Scale)")
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust the legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title="Legend")

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.suptitle("Effect of Combined Dropout and L2 Regularization on Double Descent (MSE)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Plot R2 results
fig, axs = plt.subplots(len(l2_weights), 1, figsize=(15, 4 * len(l2_weights)), sharex=True)
for i, l2_weight in enumerate(l2_weights):
    ax = axs[i]
    for dropout_rate in dropout_rates:
        train_r2 = results[(dropout_rate, l2_weight)]['train_r2']
        test_r2 = results[(dropout_rate, l2_weight)]['test_r2']
        
        ax.plot(degrees, test_r2, label=f"Test R² (Dropout={dropout_rate})", marker='o')
        ax.plot(degrees, train_r2, linestyle='--', label=f"Train R² (Dropout={dropout_rate})")
    
    ax.set_title(f"L2 Regularization (Alpha={l2_weight})")
    ax.set_ylabel("R² Score")
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adjust the legend
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, title="Legend")

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.suptitle("Effect of Combined Dropout and L2 Regularization on Double Descent (R²)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
