# Viva Questions and Answers

## 1. What is the objective of this program?

To implement parallel:

* Minimum operation
* Maximum operation
* Sum operation
* Average operation

using OpenMP reduction in C++.

---

## 2. What is OpenMP?

OpenMP is an API used for parallel programming in C/C++.

It creates multiple threads for concurrent execution.

---

## 3. What is reduction in OpenMP?

Reduction combines results from multiple threads into a single final result.

---

## 4. Which OpenMP directive is used?

```cpp id="2krbd8"
#pragma omp parallel for reduction(...)
```

Used to parallelize loop operations safely.

---

## 5. Why reduction is required?

Because multiple threads update shared variables like:

* sum
* min
* max

Reduction avoids race conditions.

---

## 6. What is race condition?

When multiple threads access and modify shared data simultaneously causing incorrect results.

---

## 7. What does this line mean?

```cpp id="ttjlwm"
reduction(+ : sum)
```

Each thread computes partial sum and OpenMP combines them at the end.

---

## 8. What does `reduction(min : minValue)` do?

Finds minimum value safely using parallel threads.

---

## 9. What does `reduction(max : maxValue)` do?

Finds maximum value safely using parallel threads.

---

## 10. What array is used in the program?

```text id="jlwmr5"
[4, 6, 3, 2, 6, 7, 9, 2, 1, 6, 5]
```

---

## 11. How is array length calculated?

```cpp id="vjlwm9"
sizeof(nums) / sizeof(int)
```

It calculates total number of elements.

---

## 12. What is the minimum value?

```text id="fjlwm6"
1
```

---

## 13. What is the maximum value?

```text id="6jlwm1"
9
```

---

## 14. What is the sum of array elements?

Calculation:

4+6+3+2+6+7+9+2+1+6+5=51

So:

```text id="tjlwm2"
Sum = 51
```

---

## 15. What is the average value?

Formula:

Average=\frac{Sum}{Number\ of\ Elements}

Calculation:

\frac{51}{11}\approx4.63

---

## 16. Why use parallel programming here?

To improve performance using multiple CPU cores.

---

## 17. What is the purpose of `chrono` library?

To measure execution time.

---

## 18. What does `high_resolution_clock` do?

Measures time with high precision.

---

## 19. Why use microseconds?

To measure very small execution times accurately.

---

## 20. What is a thread?

A lightweight execution unit inside a process.

---

## 21. What is the difference between sequential and parallel execution?

| Sequential         | Parallel                      |
| ------------------ | ----------------------------- |
| One task at a time | Multiple tasks simultaneously |
| Slower             | Faster                        |

---

## 22. Why initialize minValue and maxValue with nums[0]?

Because:

* first element provides valid initial comparison value.

---

## 23. Why is average function using float?

Because average may contain decimal values.

---

## 24. What happens if reduction is removed?

Possible incorrect results due to race conditions.

---

## 25. What compiler flag is required for OpenMP?

```bash id="mjlwm9"
-fopenmp
```

Example:

```bash id="2jlwm4"
g++ file.cpp -fopenmp
```

# Output Explanation

## Display Array

Prints all array elements.

---

## Min Operation

Finds smallest value:

```text id="8jlwm2"
1
```

---

## Max Operation

Finds largest value:

```text id="zjlwm1"
9
```

---

## Sum Operation

Total of all elements:

```text id="hjlwm4"
51
```

---

## Average Operation

Average value:

```text id="1jlwm3"
4.63
```

---

## Execution Time

```text id="wjlwm7"
Execution time: xxx microseconds
```

Shows total program execution time.

# Important Teacher-Trap Questions

## Why is reduction better than critical section here?

Reduction is:

* faster
* optimized
* avoids unnecessary locking

---

## Can min and max operations also use reduction?

Yes.

OpenMP supports:

* min
* max
* *
* *

and other operations.

---

## Is parallel execution always faster?

Not always.

For very small arrays:

* thread overhead may reduce benefits.

# One-Line Practical Summary

> Implemented parallel minimum, maximum, sum, and average operations using OpenMP reduction directives and measured execution time using the chrono library.
