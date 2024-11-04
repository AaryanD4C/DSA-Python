def print_array(A):
    for element in A:
        print(element, end=" ")
    print()

def merge(A, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = A[left + i]

    for j in range(0, n2):
        R[j] = A[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def main():
    n = int(input("Enter number of elements: "))
    A = []

    print("Enter values of elements: ")
    for _ in range(n):
        A.append(int(input()))

    print("Before Merge sort:")
    print_array(A)

    merge_sort(A, 0, n - 1)

    print("After Merge sort:")
    print_array(A)

if __name__ == "__main__":
    main()
