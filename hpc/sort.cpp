#include <iostream>
#include <omp.h>
#include <chrono>

using namespace std;
using namespace chrono;

// Bubble Sort
void bubbleSort(int arr[], int n) {

    for (int i = 0; i < n - 1; i++) {

        #pragma omp parallel for
        for (int j = 0; j < n - i - 1; j++) {

            if (arr[j] > arr[j + 1]) {

                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Merge Function
void merge(int arr[], int low, int mid, int high) {

    int i = low;
    int j = mid + 1;
    int k = 0;

    int temp[100];

    while (i <= mid && j <= high) {

        if (arr[i] < arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while (i <= mid)
        temp[k++] = arr[i++];

    while (j <= high)
        temp[k++] = arr[j++];

    for (i = low, k = 0; i <= high; i++, k++)
        arr[i] = temp[k];
}

// Parallel Merge Sort
void mergeSort(int arr[], int low, int high) {

    if (low < high) {

        int mid = (low + high) / 2;

        #pragma omp parallel sections
        {

            #pragma omp section
            mergeSort(arr, low, mid);

            #pragma omp section
            mergeSort(arr, mid + 1, high);
        }

        merge(arr, low, mid, high);
    }
}

// Print Array
void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";

    cout << endl;
}

int main() {

    int arr1[] = {9, 4, 7, 6, 3, 1, 5};
    int arr2[] = {9, 4, 7, 6, 3, 1, 5};

    int n = 7;

    // Bubble Sort Timing
    auto start1 = high_resolution_clock::now();

    bubbleSort(arr1, n);

    auto end1 = high_resolution_clock::now();

    auto duration1 =
    duration_cast<microseconds>(end1 - start1);

    cout << "Bubble Sort Result: ";
    printArray(arr1, n);

    cout << "Bubble Sort Time: "
         << duration1.count()
         << " microseconds\n\n";

    // Merge Sort Timing
    auto start2 = high_resolution_clock::now();

    mergeSort(arr2, 0, n - 1);

    auto end2 = high_resolution_clock::now();

    auto duration2 =
    duration_cast<microseconds>(end2 - start2);

    cout << "Merge Sort Result: ";
    printArray(arr2, n);

    cout << "Merge Sort Time: "
         << duration2.count()
         << " microseconds\n";

    return 0;
}
