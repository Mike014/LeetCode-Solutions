# Exercises
# Give the run time for each of these scenarios in terms of Big O.

# Common Big O Run Times
# Here are the most common run times, from fastest to slowest:

# O(log n) (logarithmic time): Example, binary search.
# O(n) (linear time): Example, simple search.
# O(n * log n) (linearithmic time): Example, fast sorting algorithms like quicksort.
# O(n^2) (quadratic time): Example, slow sorting algorithms like selection sort.
# O(n!): Example, complex problems like the traveling salesman problem.
# O(2^n): Example, the Tower of Hanoi problem.
# O(n^n): Example, another complex problem.

# 1.3

# You have a name, and you want to find the person’s phone number in the phone book.
name = "John"
person_phone_book = {
    "John": 1234567890,
    "Jane": 2345678901,
    "Doe": 3456789012,
    "Smith": 4567890123,
    "Johnson": 5678901234,
    "Williams": 6789012345,
    "Brown": 7890123456,
    "Jones": 8901234567,
}

# 1.4

# You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

# 1.5

# You want to read the numbers of every person in the phone book.

def process_phone_numbers(phone_book, window_size):
    """
    Combines Sliding Window and Quicksort to read and sort phone numbers in blocks.
    
    :param phone_book: Dictionary with names and phone numbers
    :param window_size: Window size (number of elements per block)
    :return: List of sorted phone numbers
    """
    # Extract phone numbers
    phone_numbers = list(phone_book.values())
    sorted_numbers = []

    # Sliding Window: process numbers in blocks
    for i in range(0, len(phone_numbers), window_size):
        window = phone_numbers[i:i + window_size]  # Extract the block
        sorted_window = quicksort(window)  # Sort the block with Quicksort
        sorted_numbers.extend(sorted_window)  # Add sorted numbers

    # Final merge for global sorting
    sorted_numbers = quicksort(sorted_numbers)
    return sorted_numbers

def quicksort(array):
    """
    Quicksort algorithm to sort a list.
    
    :param array: List of numbers
    :return: Sorted list
    """
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]  # Choose the pivot
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

phone_book = {
    "John": 1234567890,
    "Jane": 2345678901,
    "Doe": 3456789012,
    "Smith": 4567890123,
    "Johnson": 5678901234,
    "Williams": 6789012345,
    "Brown": 7890123456,
    "Jones": 8901234567,
}

window_size = 3
result = process_phone_numbers(phone_book, window_size)
print(result)

# The total number of elements (n):
# The number of phone numbers in the dictionary.

# The window size (k):
# The number of elements processed per block.

# Sorting efficiency:
# The time required by Quicksort to sort the blocks and subsequently the global sorting.

# With n=1,000,000 numbers and a window of k=10,000, the algorithm takes about 35 seconds on a system that handles 1 million operations per second.
# Actual times will vary based on system capacity and memory management.

# 1.6

# You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)