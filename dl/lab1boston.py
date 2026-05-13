# Linear Regression using Deep Neural Network
# Boston Housing Price Prediction

# Step 1: Import Libraries
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import boston_housing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Step 2: Load Dataset
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# Step 3: Explore Dataset
print("Training Data Shape:", x_train.shape)
print("Testing Data Shape :", x_test.shape)

print("\nNumber of Features:", x_train.shape[1])

print("\nFirst Training Record:")
print(x_train[0])

print("\nFirst Target Value:")
print(y_train[0])

# Step 4: Feature Scaling
scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Step 5: Build Deep Neural Network Model
model = tf.keras.models.Sequential([

    tf.keras.layers.Dense(64, activation='relu',
                          input_shape=(x_train.shape[1],)),

    tf.keras.layers.Dense(32, activation='relu'),

    tf.keras.layers.Dense(1)

])

# Step 6: Compile Model
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Step 7: Train Model
history = model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

# Step 8: Evaluate Model
loss, mae = model.evaluate(x_test, y_test)

print("\nTest Loss:", loss)
print("Test MAE :", mae)

# Step 9: Predict Output
y_pred = model.predict(x_test)

# Step 10: Calculate Error
mse = mean_squared_error(y_test, y_pred)

print("\nMean Squared Error:", mse)

# Step 11: Compare Actual and Predicted Values
results = pd.DataFrame({
    "Actual Price": y_test,
    "Predicted Price": y_pred.flatten()
})

print("\nActual vs Predicted Values")
print(results.head(10))

# Step 12: Plot Loss Graph
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend(["Training Loss", "Validation Loss"])

plt.show()
