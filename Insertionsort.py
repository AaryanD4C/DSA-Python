def print_array(A):
    for element in A:
        print(element, end=" ")
    print()

def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

def main():
    n = int(input("Enter number of Elements: "))
    A = []

    print("Enter Elements of the array: ")
    for i in range(n):
        A.append(int(input()))

    print("Original array:")
    print_array(A)

    insertion_sort(A)

    print("Sorted array:")
    print_array(A)

if __name__ == "__main__":
    main()
