def main():
    from queue import Queue
    from stack import Stack

    arr1 = Stack()

    arr1.add(1)
    arr1.add(2)
    arr1.add(3)
    arr1.add(4)

    arr1.get()

    arr1.remove()
    arr1.remove()

    arr1.get()

    arr2 = Queue()

    arr2.add(1)
    arr2.add(2)
    arr2.add(3)
    arr2.add(4)

    arr2.get()

    arr2.remove()
    arr2.remove()
    arr2.get()


if __name__ == "__main__":
    main()
