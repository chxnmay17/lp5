# Viva Questions and Answers

1. **What is the objective of this practical?**  
   To predict Boston house prices using Linear Regression implemented with a Deep Neural Network.

2. **Which dataset did you use?**  
   Boston Housing Dataset.  
   It contains house-related features and corresponding house prices.

3. **What type of problem is this?**  
   Regression problem.  
   Because output is a continuous numerical value (house price).

4. **What are the shapes of training and testing data?**  
   **Training data:** `(404, 13)`  
   **Testing data:** `(102, 13)`  
   **Meaning:**  
   - 404 training records  
   - 102 testing records  
   - 13 features in each record

5. **How did you know the dataset has 13 features?**  
   Using: `x_train.shape[1]`  
   **Output:** `13`

6. **What is the first training record?**  
   `[1.23247 0. 8.14 ...]`  
   These are numerical feature values of one house.

7. **What is the target value?**  
   `15.2`  
   **Meaning:**  
   - actual house price for first record

8. **Why did you use StandardScaler?**  
   To normalize feature values.  
   Feature scaling improves:  
   - training speed  
   - convergence  
   - model performance

9. **Why use Dense layers?**  
   Dense layers help learn relationships between features and house prices.

10. **Why use ReLU activation?**  
    ReLU introduces non-linearity.  
    **Formula:** `f(x) = max(0, x)`

11. **Why output layer has only 1 neuron?**  
    Because only one continuous value is predicted:  
    - house price

12. **Why no activation function in output layer?**  
    Regression problems require unrestricted numerical output.

13. **Which optimizer did you use?**  
    Adam optimizer.  
    It is fast and efficient.

14. **What loss function did you use?**  
    `mse` (Mean Squared Error).  
    **Formula:** `MSE = (1/n) * Σ(y - ŷ)^2`

15. **What is MAE?**  
    Mean Absolute Error.  
    It measures average absolute difference between actual and predicted values.

16. **What is an epoch?**  
    One complete training cycle through the entire dataset.  
    You trained for 100 epochs.

17. **What is batch size?**  
    `16`  
    **Meaning:**  
    - model processes 16 samples at a time.

18. **What is validation_split=0.2?**  
    20% of training data used for validation.  
    80% used for training.

19. **Why does loss decrease during training?**  
    Because model learns better patterns over epochs.  
    - **Initial loss:** 543  
    - **Final loss:** 6  
    This shows learning improvement.

20. **What is Test Loss?**  
    `23.048`  
    It measures prediction error on unseen testing data.

21. **What is Test MAE?**  
    `2.89`  
    **Meaning:**  
    - average prediction error is approximately 2.89 price units.

22. **Explain Actual vs Predicted Output.**  
    **Example:**  

    | Actual | Predicted |
    |--------|-----------|
    | 7.2    | 7.97      |
    | 18.8   | 18.20     |

    Predicted prices are close to actual prices, so model performs well.

23. **Why is this called Linear Regression using DNN?**  
    Because:  
    - output is continuous  
    - final layer predicts numerical value  
    - neural network performs regression task

24. **Difference between classification and regression?**  

    | Classification | Regression        |
    |----------------|-----------------|
    | Predict categories | Predict numerical values |
    | Example: Positive/Negative | Example: House price |

25. **Why plot loss graph?**  
    To visualize:  
    - training performance  
    - validation performance  
    - learning progress

**Output Explanation**  
- **Initial Large Loss:** 543  
  At beginning: model predictions are poor  

- **Gradual Loss Reduction:** 543 → 6  
  Meaning: model learned house price patterns successfully

- **Final Prediction Example:**  
  Actual Price: 27.0  
  Predicted Price: 29.44  
  Prediction is close to actual value

---

## Important Teacher-Trap Questions

- **Why use scaling in regression?**  
  Because feature ranges are different.  
  **Example:**  
  - TAX may be hundreds  
  - RM may be single digits  
  Scaling prevents dominance of large-value features.

- **Why use DNN instead of simple linear regression?**  
  DNN can learn complex non-linear relationships between features and prices.

- **Why does validation loss fluctuate later?**  
  Possible slight overfitting after many epochs.
