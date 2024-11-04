class MyArray:
    def __init__(self, total_size, used_size):
        self.total_size = total_size
        self.used_size = used_size
        self.array = [0] * total_size  # Initialize array with zeros

    def show(self):
        for i in range(self.used_size):
            print(self.array[i])

    def set_val(self):
        for i in range(self.used_size):
            n = int(input(f"Enter element {i}: "))
            self.array[i] = n

def main():
    marks = MyArray(10, 2)
    print("We are running set_val now")
    marks.set_val()

    print("We are running show now")
    marks.show()

if __name__ == "__main__":
    main()
