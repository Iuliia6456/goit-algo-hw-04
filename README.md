Based on the provided output we can conclude that Insertion Sort has the slowest performance, especially for large datasets. This is due to the nature of Insertion Sort, as its time complexity is O(n^2). 
Thus it leads to slower execution time compared to the Merge Sort and Timsort.

Merge Sort is consistently faster than Insertion Sort. It has a time complexity of O(n log n), which makes it more efficient for larger datasets. Merge Sort is a divide-and-conquer algorithm and in general
performs better than Insertion Sort but worse than Timsort.

Timsort is significantly faster than both Insertion Sort and Merge Sort, as it is a hybrid sorting algorithm derived from merge sort and insertion sort. It has the extremely short execution time even with large
datasets, making it the best choice for sorting.

Conclusion: for small datasets Insertion Sort might be competitive, but as the dataset size grows, Merge Sort and Timsort become more favorable. To achieve the highest performance it is advisable to use
the built-in algorithm (Timsort) 
