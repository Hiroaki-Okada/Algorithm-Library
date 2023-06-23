class UnionFind:
    def __init__(self, n):
        '''
        n : int
            要素数
        parents : list
            各要素の親要素の番号を格納するリスト
            ただし根の要素には -(そのグループの要素数) が格納されている
        '''
        self.n = n
        self.parents = [-1] * n

    # 要素 x が属するグループの根を返す
    def find(self, x):
        # -1 以下なら根なので返す
        if self.parents[x] < 0:
            return x
        
        # 再帰ステップ
        # 根に辿り着くまで再帰的に木を辿る
        # 親番号を根番号に更新して経路圧縮することで計算量を削減
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    # 要素 x が属するグループと要素 y が属するグループを併合
    def union(self, x, y):
        # x, y は要素 x と要素 y が属するグループの根
        x = self.find(x)
        y = self.find(y)

        # 根が同じなら既に同じグループに属しているので return して良い
        if x == y:
            return

        # そうでなければ併合する
        # x, y は根なので、parents[x] と parents[y] には -(そのグループの要素数) が格納されている
        # ここで、計算量改善の観点では併合する際にサイズが小さい方を大きい方に繋げると良い
        # そこで、y をサイズの小さいグループの根、x をサイズの大きいグループの根とすることを考える
        # parentsにはサイズの負の値が格納されていることを利用すれば、以下のように書ける
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        # y を x に繋ぎ、x の要素数に y の要素数を足す
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素 x, y が同じグループに属するかどうかを boolean で返す
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素 x が属するグループのサイズ(要素数)を返す
    # x の根を調べ、その根の parents の値を調べる
    def size(self, x):
        return -self.parents[self.find(x)]
    
    # 要素 x が属するグループに属する要素をリストで返す
    # まず x の根を調べ、次に n 個の要素全てに対して根を調べていき、両者が同じであればリストに追加する
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    # 全ての根の要素をリストで返す
    # parents の値を調べ、-1 以下の根である要素をリストに加える
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    # グループの数を返す
    def group_count(self):
        return len(self.roots())
    
    # {ルート要素:[そのグループに含まれる要素のリスト]}を文字列で返す
    def all_group_members(self):
        from collections import defaultdict
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    

n = 100
uf=UnionFind(n) # n 個の頂点を 0～n-1 で管理する