Insertion Sort in Python

This repository contains a simple implementation of the **Insertion Sort** algorithm in Python.

📖 Overview

Insertion Sort is a simple comparison-based sorting algorithm. It works by dividing the list into a sorted and an unsorted portion, 
then repeatedly inserting each element from the unsorted portion into its correct position in the sorted portion.

This implementation sorts the list in **ascending order**.

📝 Python Code

```python
def insertion_sort(seq):
    for slicend in range(1, len(seq)):
        pos = slicend

        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos], seq[pos-1]) = (seq[pos-1], seq[pos])
            pos = pos - 1

    print(seq)

seq = [67, 44, 82, 17, 20]
insertion_sort(seq)
```

▶️ Example

Input

```python
seq = [67, 44, 82, 17, 20]
```

Output

```text
[17, 20, 44, 67, 82]
```

⚙️ How It Works

1. Start from the second element of the list.
2. Compare it with the elements before it.
3. Shift larger elements one position to the right.
4. Insert the current element into its correct position.
5. Repeat until the entire list is sorted.

This project was created to practice:
- Python programming
- Sorting algorithms
- Algorithm analysis
- Git and GitHub

👨‍💻 Author

Created by "Hotnerdy"
