def main():
    import queue
    from myqueue import MyQueue
    from mystack import MyStack

    # built function
    q = queue.Queue(maxsize=20)
    q.put(1)
    q.put(2)
    q.put(3)

    print(q.get())

    s = queue.LifoQueue(maxsize=10)
    s.put(1)
    s.put(2)
    s.put(3)

    print(s.get())

    # my own func
    arr1 = MyStack()

    arr1.add(1)
    arr1.add(2)
    arr1.add(3)
    arr1.add(4)

    arr1.get()

    arr1.remove()
    arr1.remove()

    arr1.get()

    arr2 = MyQueue()

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
