# Important Viva Questions and Answers – CNN (Fashion MNIST)

1. **What is CNN?**  
   CNN (Convolutional Neural Network) is a deep learning algorithm mainly used for image processing and image classification.

2. **Which dataset did you use?**  
   Fashion MNIST dataset.  
   It contains grayscale images of fashion clothing items.

3. **How many classes are present in the dataset?**  
   10 classes:  
   - T-shirt/top  
   - Trouser  
   - Pullover  
   - Dress  
   - Coat  
   - Sandal  
   - Shirt  
   - Sneaker  
   - Bag  
   - Ankle boot

4. **What is the shape of training data?**  
   `(60000, 28, 28)`  
   **Meaning:**  
   - 60,000 training images  
   - each image size is 28×28 pixels

5. **What is the shape after reshaping?**  
   `(60000, 28, 28, 1)`  
   **Meaning:**  
   - 1 represents grayscale channel  
   CNN requires: `(height, width, channels)`

6. **Why normalize the data?**  
   Original pixel values: 0 to 255  
   After normalization: 0 to 1  
   **Reason:** Improves training speed and model performance.

7. **What does Conv2D layer do?**  
   Conv2D extracts important image features like:  
   - edges  
   - shapes  
   - textures  
   - patterns

8. **Why use MaxPooling2D?**  
   MaxPooling reduces image size and computation.  
   It also helps reduce overfitting.

9. **What does Flatten layer do?**  
   Flatten converts 2D feature maps into a 1D vector before passing to Dense layers.  
   **Example:** `(5,5,64) → 1600`  
   Because: `5 × 5 × 64 = 1600`

10. **Why use ReLU activation?**  
    ReLU introduces non-linearity and helps the network learn complex patterns.  
    **Formula:** `f(x) = max(0, x)`

11. **Why use Softmax in output layer?**  
    Softmax is used for multi-class classification.  
    It converts outputs into probabilities.

12. **Why output layer has 10 neurons?**  
    Because dataset contains 10 clothing categories.

13. **What loss function is used?**  
    `sparse_categorical_crossentropy`  
    Used for multi-class classification with integer labels.

14. **Which optimizer did you use?**  
    Adam optimizer.  
    It gives fast and efficient training.

15. **What accuracy did you get?**  
    `0.9021`  
    Convert to percentage: `0.9021 × 100 ≈ 90.21%`  
    **Meaning:** test accuracy is approximately 90.21%.

16. **Explain the prediction output.**  
    - Predicted Category: Ankle boot  
    - Actual Category: Ankle boot  
    **Meaning:** model predicted correctly

17. **What is an epoch?**  
    One complete training cycle through the entire dataset.  
    You trained for 5 epochs.

18. **What is validation_split=0.2?**  
    20% of training data is used for validation.  
    80% used for training.

19. **Why CNN is better for images?**  
    CNN automatically extracts image features and preserves spatial relationships between pixels.

20. **Difference between ANN and CNN?**  

    | ANN                     | CNN                       |
    |--------------------------|---------------------------|
    | General neural network   | Specialized for images    |
    | Fully connected          | Uses convolution filters  |
    | More parameters          | Fewer parameters          |
    | Slower for images        | Efficient for images      |

---

## Output Explanation

- **Dataset Download:**  
  TensorFlow automatically downloaded Fashion MNIST dataset.

- **First Label = 9** → corresponds to Ankle boot

- **Model Summary Explanation:**  
  - **Conv2D Output:** `(None, 26, 26, 32)`  
    Meaning: 32 feature maps generated; image reduced from 28×28 to 26×26 due to 3×3 filter  
  - **MaxPooling Output:** `(None, 13, 13, 32)`  
    Pooling reduces dimensions by half  
  - **Flatten Output:** `(None, 1600)`  
    Converted into 1D vector

- **Why accuracy increases and loss decreases?**  
  Because model learns patterns better during training.
