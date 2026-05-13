# Viva Questions and Answers

## 1. What is the objective of this program?

To implement:

* Parallel Bubble Sort
* Parallel Merge Sort

using OpenMP in C++ and compare execution times.

---

## 2. What is sorting?

Sorting means arranging data in:

* ascending order
* descending order

---

## 3. Which sorting algorithms are used?

* Bubble Sort
* Merge Sort

---

## 4. What is Bubble Sort?

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in wrong order.

Largest element moves to the end after each pass.

---

## 5. What is Merge Sort?

Merge Sort uses:

* Divide and Conquer technique

It:

1. divides array into smaller parts
2. sorts them
3. merges them back

---

## 6. What is Divide and Conquer?

A technique where:

* problem is divided into smaller subproblems
* solved recursively
* combined to get final result

---

## 7. Which OpenMP directive is used in Bubble Sort?

```cpp id="f2gqv8"
#pragma omp parallel for
```

Used to parallelize comparison loop.

---

## 8. Which OpenMP directive is used in Merge Sort?

```cpp id="6e8x1r"
#pragma omp parallel sections
```

Used to execute left and right recursive calls simultaneously.

---

## 9. What is the advantage of parallel Merge Sort?

Left and right halves are sorted concurrently, improving performance.

---

## 10. What is recursion?

A function calling itself repeatedly.

Used in Merge Sort.

---

## 11. What is the purpose of merge() function?

To combine two sorted subarrays into one sorted array.

---

## 12. What is temporary array used for?

```cpp id="11jfxe"
int temp[100];
```

Stores merged sorted elements temporarily.

---

## 13. What is time complexity of Bubble Sort?

Worst case:

O(n^2)

---

## 14. What is time complexity of Merge Sort?

Worst case:

O(n\log n)

---

## 15. Which sorting algorithm is faster?

Merge Sort is generally faster for large datasets.

---

## 16. Why is Merge Sort more efficient?

Because:

* it divides problem recursively
* reduces comparisons

---

## 17. What is the purpose of `chrono` library?

To measure execution time.

---

## 18. Why use `high_resolution_clock`?

To measure time with high precision.

---

## 19. What does `duration_cast<microseconds>` do?

Converts execution time into microseconds.

---

## 20. What is a microsecond?

```text id="g1m7m4"
1 microsecond = 10^-6 seconds
```

---

## 21. What is the input array?

```text id="mjlwm6"
9 4 7 6 3 1 5
```

---

## 22. What is the sorted output?

```text id="jlwm7t"
1 3 4 5 6 7 9
```

---

## 23. Why use parallel programming in sorting?

To:

* improve speed
* reduce execution time
* use multiple CPU cores

---

## 24. What is the role of `swap()`?

Exchanges two elements during Bubble Sort.

---

## 25. Why Merge Sort is suitable for parallelism?

Because left and right halves are independent and can run simultaneously.

# Output Explanation

## Bubble Sort Result

```text id="6jlwm5"
1 3 4 5 6 7 9
```

Array sorted in ascending order using Bubble Sort.

---

## Merge Sort Result

```text id="jlwm1x"
1 3 4 5 6 7 9
```

Array sorted using Merge Sort.

---

## Execution Time

```text id="8jlwm4"
Bubble Sort Time: xxx microseconds
Merge Sort Time: xxx microseconds
```

Shows time taken by each algorithm.

Usually:

* Merge Sort is faster for large data.

# Important Teacher-Trap Questions

## Is Bubble Sort truly efficient for parallelism?

Not very efficient because:

* iterations are dependent on previous swaps.

---

## Why does Merge Sort parallelize better?

Subarrays are independent.

---

## Can parallel overhead reduce performance?

Yes.

For small arrays:

* thread creation overhead may reduce speed gain.

---

## Why use recursive Merge Sort?

Recursion naturally fits divide-and-conquer problems.

# Difference Between Bubble Sort and Merge Sort

| Bubble Sort      | Merge Sort         |
| ---------------- | ------------------ |
| Simple algorithm | Divide and conquer |
| O(n²)            | O(n log n)         |
| Slower           | Faster             |
| In-place sorting | Uses extra memory  |

# One-Line Practical Summary

> Implemented Parallel Bubble Sort and Parallel Merge Sort using OpenMP in C++ and compared their execution times using the chrono library.
