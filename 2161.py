import queue

a = queue.Queue()
n = int(input())

for i in range(1,n+1):
    a.put(i)


while(a.qsize() > 1):
    c = a.get()
    print(c)
    c = a.get()
    a.put(c)

print(a.get())