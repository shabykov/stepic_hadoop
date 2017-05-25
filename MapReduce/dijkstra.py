import sys


class W:
    weights = {}
    pathway = {}

    def get_w(self, x, y):
        return self.weights.get((x, y), -1)

    def set_w(self, x, y, v):
        self.weights[x, y] = v
        if self.pathway.get(x) is None:
            self.pathway[x] = []
        self.pathway[x].append(y)

    def get_v(self, v, *args):
        return self.pathway.get(v, *args)


def dijkstra(V, s, w):
    d = {}
    for v in V:
        d[v] = float('inf')

    d[s] = 0
    Q = d.copy()
    while len(Q):
        u = min(Q, key=Q.get)
        Q.pop(u)
        for v in w.get_v(u, []):
            if d[v] > d[u] + w.get_w(u, v):
                d[v] = d[u] + w.get_w(u, v)
                Q[v] = d[v]
    return d

w = W()
V = []
from_v = '1'
to_v = '4'

for i, line in enumerate(sys.stdin):
    data = line.strip().split()

    if len(data) == 2:
        if i:
            from_v = data[0]
            to_v = data[-1]
        else:
            V = [str(i) for i in range(1, int(data[0]) + 1)]

    elif len(data) == 3:
        from_V = data[0]
        to_V = data[1]
        w.set_w(from_V, to_V, int(data[2]))

dd = dijkstra(V, from_v, w)

if dd.get(to_v) is None or dd.get(to_v) == float('inf'):
    print(-1)
else:
    print(dd.get(to_v))


