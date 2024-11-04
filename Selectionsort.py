def print_array(A):
    for element in A:
        print(element, end=" ")
    print()

def selection_sort(A):
    for i in range(len(A) - 1):
        index_of_min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[index_of_min]:
                index_of_min = j
        A[i], A[index_of_min] = A[index_of_min], A[i]

def main():
    n = int(input("Enter number of elements: "))
    A = []

    print("Enter values of elements: ")
    for _ in range(n):
        A.append(int(input()))

    print("Before Selection sort:")
    print_array(A)

    selection_sort(A)

    print("After Selection sort:")
    print_array(A)

if __name__ == "__main__":
    main()
