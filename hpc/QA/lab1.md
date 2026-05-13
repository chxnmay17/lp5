# Viva Questions and Answers

## 1. What is the objective of this program?

To implement:

* Parallel Breadth First Search (BFS)
* Parallel Depth First Search (DFS)

using OpenMP in C++.

---

## 2. What is BFS?

BFS (Breadth First Search) traverses tree level by level.

Traversal order for this tree:

```text
1 2 3 4 5 6 7
```

---

## 3. What is DFS?

DFS (Depth First Search) traverses depth-wise.

Possible DFS order:

```text
1 2 4 5 3 6 7
```

In parallel DFS, order may vary because threads execute simultaneously.

---

## 4. What data structure is used in BFS?

Queue.

Because BFS follows FIFO (First In First Out).

---

## 5. What data structure is used in DFS?

Recursion / Stack.

Recursive calls internally use stack memory.

---

## 6. What is OpenMP?

OpenMP is an API used for parallel programming in C/C++.

It creates multiple threads for concurrent execution.

---

## 7. Why use parallel programming?

To:

* improve performance
* reduce execution time
* utilize multiple CPU cores

---

## 8. Which OpenMP directive is used in BFS?

```cpp
#pragma omp parallel for
```

Used to process nodes of the same level in parallel.

---

## 9. Why use `#pragma omp critical`?

Critical section prevents multiple threads from accessing shared resources simultaneously.

Used for:

* printing
* queue insertion

to avoid race conditions.

---

## 10. What is race condition?

When multiple threads access and modify shared data simultaneously causing incorrect output.

---

## 11. What is `#pragma omp parallel sections`?

Used in DFS to execute different recursive sections in parallel.

Example:

* left subtree
* right subtree

run simultaneously.

---

## 12. What is the advantage of parallel BFS?

Multiple nodes at same tree level can be processed simultaneously.

---

## 13. What is the advantage of parallel DFS?

Left and right subtrees can be explored concurrently.

---

## 14. What is `chrono` library used for?

To measure execution time.

---

## 15. What does this line do?

```cpp
auto start1 = high_resolution_clock::now();
```

Stores starting time of execution.

---

## 16. Why use `duration_cast<microseconds>`?

To convert execution time into microseconds.

---

## 17. What is a microsecond?

```text
1 microsecond = 10^-6 seconds
```

---

## 18. What is the tree structure used?

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

Binary tree with 7 nodes.

---

## 19. What is a binary tree?

A tree where each node has at most:

* one left child
* one right child

---

## 20. Why is traversal order in parallel DFS not fixed?

Because threads execute independently and concurrently.

---

## 21. What is recursion?

A function calling itself repeatedly.

Used in DFS traversal.

---

## 22. What happens if critical section is removed?

Possible problems:

* mixed output
* corrupted queue
* race conditions

---

## 23. Difference between BFS and DFS?

| BFS                  | DFS                       |
| -------------------- | ------------------------- |
| Level-wise traversal | Depth-wise traversal      |
| Uses Queue           | Uses Stack/Recursion      |
| Finds shortest path  | Less memory in some cases |

---

## 24. Why parallelism is easier in BFS levels?

Nodes at same level are independent and can be processed simultaneously.

---

## 25. What compiler flag is needed for OpenMP?

```bash
-fopenmp
```

Example:

```bash
g++ file.cpp -fopenmp
```

# Output Explanation

## Parallel BFS Traversal

```text
1 2 3 4 5 6 7
```

Tree visited level by level.

---

## Parallel DFS Traversal

Order may vary because:

* left and right recursive calls execute in parallel.

---

## Execution Time

```text
BFS Execution Time: xxx microseconds
DFS Execution Time: xxx microseconds
```

Shows performance measurement using chrono library.

# Important Teacher-Trap Questions

## Why use queue in BFS?

Because BFS processes nodes in insertion order (FIFO).

---

## Why recursion is suitable for DFS?

DFS naturally explores deeper nodes recursively.

---

## Is parallel version always faster?

Not always.

For small trees:

* thread creation overhead may reduce performance benefit.

---

## Why use critical section around queue push?

Queue is shared among threads.

Without synchronization:

* data corruption may occur.

# One-Line Practical Summary

> Implemented parallel BFS and DFS tree traversal using OpenMP in C++ and measured execution time using the chrono library.
