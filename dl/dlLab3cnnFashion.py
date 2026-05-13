# Convolutional Neural Network using Fashion MNIST Dataset
# Fashion Clothing Classification

# Step 1: Import Libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import fashion_mnist

# Step 2: Load Dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Step 3: Explore Dataset
print("Training Data Shape:", x_train.shape)
print("Testing Data Shape :", x_test.shape)

print("\nFirst Image Shape:", x_train[0].shape)

print("\nFirst Label:", y_train[0])

# Fashion category names
class_names = [
    'T-shirt/top',
    'Trouser',
    'Pullover',
    'Dress',
    'Coat',
    'Sandal',
    'Shirt',
    'Sneaker',
    'Bag',
    'Ankle boot'
]

print("\nFirst Clothing Category:")
print(class_names[y_train[0]])

# Step 4: Display First Image
plt.imshow(x_train[0], cmap='gray')
plt.title(class_names[y_train[0]])
plt.show()

# Step 5: Normalize Data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 6: Reshape for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

print("\nReshaped Training Data:", x_train.shape)

# Step 7: Build CNN Model
model = tf.keras.models.Sequential([

    # Convolution Layer
    tf.keras.layers.Conv2D(
        32,
        (3,3),
        activation='relu',
        input_shape=(28,28,1)
    ),

    # Pooling Layer
    tf.keras.layers.MaxPooling2D((2,2)),

    # Second Convolution Layer
    tf.keras.layers.Conv2D(
        64,
        (3,3),
        activation='relu'
    ),

    # Second Pooling Layer
    tf.keras.layers.MaxPooling2D((2,2)),

    # Convert 2D to 1D
    tf.keras.layers.Flatten(),

    # Dense Layer
    tf.keras.layers.Dense(64, activation='relu'),

    # Output Layer
    tf.keras.layers.Dense(10, activation='softmax')
])

# Step 8: Compile Model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Step 9: Model Summary
model.summary()

# Step 10: Train Model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_split=0.2,
    verbose=1
)

# Step 11: Evaluate Model
loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", accuracy)

# Step 12: Predictions
predictions = model.predict(x_test)

predicted_label = np.argmax(predictions[0])

print("\nPredicted Category:")
print(class_names[predicted_label])

print("\nActual Category:")
print(class_names[y_test[0]])

# Step 13: Plot Accuracy Graph
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend(["Training Accuracy", "Validation Accuracy"])

plt.show()
