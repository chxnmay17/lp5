# Viva Questions and Answers for CUDA Programs

# Part 1: Addition of Two Large Vectors

## 1. What is CUDA?

CUDA (Compute Unified Device Architecture) is a parallel computing platform developed by NVIDIA for GPU programming.

---

## 2. Why use CUDA?

CUDA uses GPU parallelism to:

* increase speed
* perform large computations efficiently

---

## 3. What is vector addition?

Adding corresponding elements of two vectors.

Example:

C[i]=A[i]+B[i]

---

## 4. Why is vector addition suitable for CUDA?

Each element addition is independent and can run in parallel.

---

## 5. What is a GPU?

GPU (Graphics Processing Unit) is a processor optimized for parallel execution of many tasks.

---

## 6. Difference between CPU and GPU?

| CPU                   | GPU                        |
| --------------------- | -------------------------- |
| Few powerful cores    | Thousands of smaller cores |
| Sequential processing | Parallel processing        |

---

## 7. What is a CUDA kernel?

A function executed on GPU.

Declared using:

```cpp id="3l1fb8"
__global__
```

---

## 8. What does `__global__` mean?

Function runs on GPU and is called from CPU.

---

## 9. What is a thread in CUDA?

Small execution unit performing one task.

In vector addition:

* one thread handles one vector element.

---

## 10. What is block in CUDA?

Group of threads.

---

## 11. What is grid in CUDA?

Collection of blocks.

---

## 12. How is thread index calculated?

Formula:

index=blockIdx.x\times blockDim.x+threadIdx.x

---

## 13. What is `blockIdx.x`?

Block number in grid.

---

## 14. What is `threadIdx.x`?

Thread number inside a block.

---

## 15. What is `blockDim.x`?

Number of threads per block.

---

## 16. What is memory allocation function in CUDA?

```cpp id="5h76u7"
cudaMalloc()
```

Allocates memory on GPU.

---

## 17. What is `cudaMemcpy()`?

Copies data between CPU and GPU memory.

---

## 18. What is `cudaFree()`?

Frees GPU memory.

---

## 19. Why use large vectors?

To utilize GPU parallel processing effectively.

---

## 20. What is synchronization in CUDA?

Ensures all GPU threads complete execution before proceeding.

Function:

```cpp id="ebmjlwm"
cudaDeviceSynchronize()
```

---

# Part 2: Matrix Multiplication using CUDA

## 21. What is matrix multiplication?

Multiplying rows of first matrix with columns of second matrix.

Formula:

C[i][j]=\sum A[i][k]\times B[k][j]

---

## 22. Why use CUDA for matrix multiplication?

Matrix multiplication involves many independent computations suitable for parallel execution.

---

## 23. How are threads assigned in matrix multiplication?

Usually:

* one thread computes one output matrix element.

---

## 24. What is 2D indexing in CUDA?

Used for matrix operations.

Example:

```cpp id="jlwmr2"
row = blockIdx.y * blockDim.y + threadIdx.y
col = blockIdx.x * blockDim.x + threadIdx.x
```

---

## 25. Why matrix multiplication is computationally expensive?

Because each output element requires multiple multiplications and additions.

---

## 26. What is the time complexity of matrix multiplication?

For two N×N matrices:

O(n^3)

---

## 27. What is parallelism in matrix multiplication?

Multiple matrix elements are computed simultaneously by different threads.

---

## 28. What are advantages of CUDA matrix multiplication?

* Faster execution
* Efficient parallel computation
* Better performance for large matrices

---

## 29. What is device memory?

Memory present on GPU.

---

## 30. What is host memory?

Memory present on CPU.

---

# Important CUDA Keywords

| Keyword      | Meaning             |
| ------------ | ------------------- |
| `__global__` | GPU kernel function |
| `cudaMalloc` | Allocate GPU memory |
| `cudaMemcpy` | Copy memory         |
| `cudaFree`   | Free GPU memory     |
| `threadIdx`  | Thread ID           |
| `blockIdx`   | Block ID            |
| `blockDim`   | Threads per block   |

# Important Teacher-Trap Questions

## Why GPU is faster for parallel tasks?

Because GPU contains thousands of cores executing tasks simultaneously.

---

## Can CUDA run without NVIDIA GPU?

No.

CUDA is specific to NVIDIA GPUs.

---

## Why CPU still needed with CUDA?

CPU:

* controls program flow
* launches kernels
* handles memory operations

GPU:

* performs parallel computation

---

## What happens if thread index exceeds array size?

Need boundary check:

```cpp id="jlwm5g"
if(index < n)
```

Otherwise memory access errors may occur.

---

## Why matrix multiplication benefits more from GPU than vector addition?

Because matrix multiplication has much higher computational workload.

# One-Line Practical Summary

> Implemented vector addition and matrix multiplication using CUDA C by utilizing GPU parallelism to improve computational performance.
