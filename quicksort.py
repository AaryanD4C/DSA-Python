def print_array(A):
    for element in A:
        print(element, end=" ")
    print()

def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high

    while True:
        while i <= high and A[i] <= pivot:
            i += 1
        while j >= low and A[j] > pivot:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[low], A[j] = A[j], A[low]
    return j

def quicksort(A, low, high):
    if low < high:
        partition_index = partition(A, low, high)
        quicksort(A, low, partition_index - 1)
        quicksort(A, partition_index + 1, high)

def main():
    n = int(input("Enter number of elements: "))
    A = []

    print("Enter values of elements: ")
    for _ in range(n):
        A.append(int(input()))

    print("Before Quick sort:")
    print_array(A)

    quicksort(A, 0, n - 1)

    print("After Quick sort:")
    print_array(A)

if __name__ == "__main__":
    main()
