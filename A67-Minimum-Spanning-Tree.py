class UnionFind:
    def __init__(self, n: int) -> None:
        # n:頂点数
        self.n = n
        # par[x]:頂点xの親の番号 根の場合は-1
        self.par = [-1] * (n + 1)
        # size[x]:頂点xを根とするグループのサイズ
        self.size = [1] * (n + 1)

    def root(self, x: int) -> int:
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, x: int, y: int) -> None:
        # union by size
        rootX = self.root(x)
        rootY = self.root(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.par[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.par[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


n, m = map(int, input().split())
# 頂点q[0]と頂点q[1]を長さq[2]の辺でつなぐ
edges = [list(map(int, input().split())) for i in range(m)]
# 辺を長さでソート
edges.sort(key=lambda x: x[2])


u = UnionFind(n)
cost = 0
for a, b, c in edges:
    # 全て一直線で繋がったら（根が同じなら）、新しい辺は追加されない
    if not u.same(a, b):
        u.unite(a, b)
        cost += c
print(cost)
