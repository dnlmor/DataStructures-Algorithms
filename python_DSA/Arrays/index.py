import time
from DSA_Arrays import Array
from DSA_Bubble_Sort import bubble_sort
from DSA_Selection_Sort import selection_sort
from DSA_Insertion_Sort import insertion_sort
from DSA_Quick_Sort import quick_sort
from DSA_Counting_Sort import counting_sort
from DSA_Radix_Sort import radix_sort
from DSA_Merge_Sort import merge_sort
from DSA_Linear_Search import linear_search
from DSA_Binary_Search import binary_search

# Utility Functions
def get_input_array():
    """Helper function to get a list of integers from the user."""
    while True:
        try:
            return list(map(int, input("Enter numbers separated by spaces: ").split()))
        except ValueError:
            print("Invalid input. Please enter integers only.")

def time_execution(func, *args):
    """Measures the execution time of a function."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    return result

# Array Operations
def run_array_operations():
    arr = Array()
    print("\nInteractive Array Operations (insert, delete, search, traverse):")
    while True:
        operation = input("\nChoose operation - Insert (i), Delete (d), Search (s), Traverse (t), Quit (q): ").lower()
        if operation == 'i':
            value = int(input("Enter number to insert: "))
            arr.insert(value)
        elif operation == 'd':
            value = int(input("Enter number to delete: "))
            arr.delete(value)
        elif operation == 's':
            value = int(input("Enter number to search: "))
            index = arr.search(value)
            print(f"Element found at index: {index}" if index != -1 else "Element not found")
        elif operation == 't':
            print("Current array contents:")
            arr.traverse()
        elif operation == 'q':
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Sorting Algorithms
def run_sorting_algorithms():
    algorithms = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Selection Sort", selection_sort),
        "3": ("Insertion Sort", insertion_sort),
        "4": ("Quick Sort", quick_sort),
        "5": ("Counting Sort", counting_sort),
        "6": ("Radix Sort", radix_sort),
        "7": ("Merge Sort", merge_sort)
    }
    unsorted_arr = get_input_array()
    print(f"\nOriginal Array: {unsorted_arr}")

    print("\nChoose a Sorting Algorithm:")
    for key, (name, _) in algorithms.items():
        print(f"{key}: {name}")

    choice = input("Enter the number corresponding to your choice: ")
    if choice in algorithms:
        name, sort_function = algorithms[choice]
        arr_copy = unsorted_arr[:]
        print(f"\nRunning {name}...")
        sorted_arr = time_execution(sort_function, arr_copy)
        print(f"Sorted Array: {sorted_arr}")
    else:
        print("Invalid choice! Please select a valid option.")

# Search Algorithms
def run_search_algorithms():
    search_algorithms = {
        "1": ("Linear Search", linear_search),
        "2": ("Binary Search", binary_search)
    }
    sorted_arr = sorted(get_input_array())
    print(f"\nSorted Array for Searching: {sorted_arr}")

    target = int(input("Enter the number to search for: "))

    print("\nChoose a Search Algorithm:")
    for key, (name, _) in search_algorithms.items():
        print(f"{key}: {name}")

    choice = input("Enter the number corresponding to your choice: ")
    if choice in search_algorithms:
        name, search_function = search_algorithms[choice]
        print(f"\nRunning {name}...")
        index = time_execution(search_function, sorted_arr, target)
        print(f"Element found at index: {index}" if index != -1 else "Element not found")
    else:
        print("Invalid choice! Please select a valid option.")

# Main Interface
def main():
    print("\n==== Data Structures and Algorithms CLI ====")
    print("1: Array Operations")
    print("2: Sorting Algorithms")
    print("3: Search Algorithms")
    print("q: Quit")

    while True:
        choice = input("\nEnter 1, 2, 3, or q to quit: ").lower()
        
        if choice == '1':
            run_array_operations()
        elif choice == '2':
            run_sorting_algorithms()
        elif choice == '3':
            run_search_algorithms()
        elif choice == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
