def print_array(A):
    for element in A:
        print(element, end=" ")
    print()

def counting_sort(A, exp):
    n = len(A)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = A[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = A[i] // exp
        output[count[index % 10] - 1] = A[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        A[i] = output[i]

def radix_sort(A):
    max1 = max(A)
    exp = 1
    while max1 // exp > 0:
        counting_sort(A, exp)
        exp *= 10

def main():
    n = int(input("Enter number of elements: "))
    A = []

    print("Enter values of elements: ")
    for _ in range(n):
        A.append(int(input()))

    print("Before Radix sort:")
    print_array(A)

    radix_sort(A)

    print("After Radix sort:")
    print_array(A)

if __name__ == "__main__":
    main()
