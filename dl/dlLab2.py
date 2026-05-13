# Binary Classification using Deep Neural Network
# IMDB Movie Review Sentiment Analysis

# Step 1: Import Libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Step 2: Load Dataset
vocab_size = 10000

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

# Step 3: Explore Dataset
print("Training Data Shape:", x_train.shape)
print("Testing Data Shape :", x_test.shape)

print("\nFirst Review Label:", y_train[0])

# 0 = Negative
# 1 = Positive

# Step 4: Pad Sequences
max_length = 200

x_train = pad_sequences(x_train, maxlen=max_length)
x_test = pad_sequences(x_test, maxlen=max_length)

print("\nPadded Shape:", x_train.shape)

# Step 5: Build DNN Model
model = tf.keras.models.Sequential([

    tf.keras.layers.Embedding(vocab_size, 128,
                              input_length=max_length),

    tf.keras.layers.GlobalAveragePooling1D(),

    tf.keras.layers.Dense(64, activation='relu'),

    tf.keras.layers.Dense(32, activation='relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Step 6: Compile Model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Step 7: Model Summary
model.summary()

# Step 8: Train Model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=128,
    validation_split=0.2,
    verbose=1
)

# Step 9: Evaluate Model
loss, accuracy = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", accuracy)

# Step 10: Predictions
predictions = model.predict(x_test)

print("\nSample Predictions:")
print(predictions[:5])

# Step 11: Plot Accuracy Graph
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend(["Training Accuracy", "Validation Accuracy"])

plt.show()
