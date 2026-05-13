# Viva Questions and Answers – IMDB Movie Review Classification

1. **What is the objective of this practical?**  
   To classify IMDB movie reviews into:  
   - positive reviews  
   - negative reviews  
   using Deep Neural Network.

2. **What type of problem is this?**  
   Binary Classification problem.  
   Because there are only two classes:  
   - Positive  
   - Negative

3. **Which dataset did you use?**  
   IMDB Movie Review Dataset.  
   It contains movie reviews and sentiment labels.

4. **What are the shapes of training and testing data?**  
   **Training Data Shape:** `(25000,)`  
   **Testing Data Shape:** `(25000,)`  
   **Meaning:**  
   - 25,000 training reviews  
   - 25,000 testing reviews  
   Each review is stored as a sequence of word indices.

5. **What does the first review label mean?**  
   `1`  
   **Meaning:**  
   - first review is positive  
   **Labels:**  
     - 0 → Negative  
     - 1 → Positive

6. **Why did you use num_words=10000?**  
   To keep only the top 10,000 most frequent words in the dataset.  
   This reduces complexity and memory usage.

7. **Why is padding required?**  
   Reviews have different lengths.  
   Padding makes all reviews equal length.

8. **What is the padded shape?**  
   `(25000, 200)`  
   **Meaning:**  
   - 25,000 reviews  
   - each review contains 200 words/tokens after padding

9. **What does Embedding layer do?**  
   Embedding layer converts words into dense numerical vectors.  
   It helps the model understand semantic relationships between words.

10. **What is GlobalAveragePooling1D?**  
    It reduces sequence data into a single vector by taking average values.  
    It simplifies the model and reduces parameters.

11. **Why use Dense layers?**  
    Dense layers learn hidden patterns from review data.

12. **Why use ReLU activation?**  
    ReLU introduces non-linearity.  
    **Formula:** `f(x) = max(0, x)`

13. **Why use sigmoid in output layer?**  
    Sigmoid gives output between 0 and 1.  
    Used for binary classification.  
    **Formula:** `σ(x) = 1 / (1 + e^-x)`

14. **Why output layer has only 1 neuron?**  
    Because model predicts one probability:  
    - positive or negative sentiment

15. **Which optimizer did you use?**  
    Adam optimizer.  
    It provides fast and efficient learning.

16. **Which loss function did you use?**  
    `binary_crossentropy`  
    Used for binary classification problems.

17. **What is an epoch?**  
    One complete training cycle through the dataset.  
    You trained for 5 epochs.

18. **What is batch size?**  
    `128`  
    **Meaning:**  
    - model processes 128 reviews at one time.

19. **What is validation_split=0.2?**  
    20% of training data is used for validation.  
    80% used for training.

20. **Why does accuracy increase during training?**  
    Because model learns sentiment patterns better over epochs.  
    **Example:**  
    - Epoch 1 accuracy: 73%  
    - Final epoch accuracy: 94%

21. **What is Test Accuracy?**  
    `0.8675`  
    Convert into percentage: `0.8675 × 100 ≈ 86.75%`  
    **Meaning:**  
    - model correctly predicts approximately 86.75% of reviews.

22. **Explain sample predictions.**  
    - `0.077` → Very close to 0 → Negative review  
    - `0.998` → Very close to 1 → Positive review  
    **Rule:**  
    - 0.5 → Positive  
    - < 0.5 → Negative

23. **Why does model summary show 0 parameters initially?**  
    0 (unbuilt)  
    This is normal in newer TensorFlow versions.  
    Model becomes fully built during training.

24. **Why plot accuracy graph?**  
    To visualize:  
    - training accuracy  
    - validation accuracy  
    - model learning performance

25. **Difference between regression and classification?**  

    | Regression              | Classification             |
    |-------------------------|----------------------------|
    | Predict numerical value | Predict category/class     |
    | Example: House price    | Example: Positive/Negative |

---

## Output Explanation

- **Training Accuracy:**  
  Started around 73% → Ended around 94%  
  Meaning: model improved learning over epochs.

- **Validation Accuracy:**  
  Final validation accuracy: 88%  
  Shows good performance on unseen validation data.

- **Test Accuracy:**  
  Final testing accuracy: 86.75%  
  Meaning: model generalizes well on new reviews.

---

## Important Teacher-Trap Questions

- **Why use Embedding instead of one-hot encoding?**  
  Embedding is:  
  - memory efficient  
  - captures semantic meaning  
  - better for NLP tasks

- **Why use sigmoid instead of softmax?**  
  Because this is binary classification.  
  Softmax is mainly used for multi-class classification.

- **What happens if padding is not used?**  
  Input review lengths become inconsistent and model cannot process batches properly.
