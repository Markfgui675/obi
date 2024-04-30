class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
qs = []
for _ in range(queries):
    stream_name, n = input().split()
    qs.append([stream_name, int(n)])
for p in qs:
    if p[0] == "even":
        print_from_stream(p[1])
    else:
        print_from_stream(p[1], OddStream())
