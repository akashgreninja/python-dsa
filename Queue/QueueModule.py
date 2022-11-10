# from collections import deque

# customq=deque(maxlen=3)
# customq.append(1)
# customq.append(1)
# customq.append(1)
# print(customq.popleft())
# print(customq.clear())

import queue as q

customq=q.Queue(maxsize=3)
customq.put(1)
customq.put(1)
customq.put(1)
print(customq.full())
print(customq.get())
print(customq.qsize())