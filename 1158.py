class Circular:
    def __init__(self, c):
        self.max = c
        self.data = [None] * c
        self.length = 0
        self.front = -1
        self.rear = -1
        self.out = [None] * c

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def isFull(self):
        return self.length == self.max

    def enqueue(self, x):
        if self.isFull():
            raise IndexError

        self.rear = (self.rear + 1) % self.max
        self.data[self.rear] = x
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError

        self.front = (self.front + 1) % self.max
        while (self.out[self.front] != None):
            self.front = (self.front + 1) % self.max
        x = self.data[self.front]
        self.out[self.front] = 1
        self.length -= 1
        return x


    def peek(self):
        if self.isEmpty():
            raise IndexError
        self.front = (self.front + 1) % self.max
        while (self.out[self.front] != None):
            self.front = (self.front + 1) % self.max
        return self.data[self.front]



a, b = map(int, input().split())
s = Circular(a)
for i in range(1, a + 1):
    s.enqueue(i)
c = 0
while(True):
    try:
        for i in range(b - 1):
            c = s.peek()
        print(s.dequeue())
    except:
        break