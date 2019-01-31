import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
while not q.empty():
    print(q.get())

stack = queue.LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
while not stack.empty():
    print(stack.get())
