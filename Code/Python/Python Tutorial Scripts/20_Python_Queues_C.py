import queue

q = queue.PriorityQueue()

q.put((2, "Hello Drug Discovery World!"))
q.put((11, 99))
q.put((5, 7.5))
q.put((1, True))

while not q.empty():
    print(q.get())