import random

from Interfaces.set_from_seq import Set_from_Sequence
from sequence.linked_list import LinkedListSequence


class HashTableSet:
    def __init__(self, r=200):
        self.chain_set = Set_from_Sequence(LinkedListSequence)
        self.A = []
        self.size = 0
        self.p = 2**31 - 1
        self.r = r  # 100/self.r = fill ratio
        self.a = random.randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):  # O(N)
        for x in self.A:
            yield from x

    def build(self, X):  # O(N)
        for i in X:
            self.insert(i)

    def _hash(self, k, m):  # O(1)
        return ((self.a * k) % self.p) % m

    def _compute_bounds(self):  # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A) * 100 * 100 // (self.r * self.r)

    # this resizing of hash_table is a bit complex
    # I didn't understood but I wrote it here as it completes the implementation
    # when I will get the intuition for resizing then
    # I'LL REMOVE THESE LINES OF COMMENTS
    def _resize(self, n):  # O(N)
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:
                f += 1
            # f = ceil(r / 100)
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()

    def find(self, k):  # O(1)
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x):  # O(1)-amortized
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:
            self.size += 1
        return added

    def delete(self, k):  # O(1)-amortized
        assert len(self) > 0  # make sure hash_table not empty
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        return x

    def find_min(self):  # O(N)
        out = None
        for x in self:
            if (out is None) or (out.key > x.key):
                out = x
        return out

    def find_max(self):  # O(N)
        out = None
        for x in self:
            if (out is None) or (out.key < x.key):
                out = x
        return out

    def find_next(self, k):  # O(N)
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    def find_prev(self, k):  # O(N)
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_ord(self):  # O(N^2)
        mini = self.find_min()
        while mini:
            yield mini
            mini = self.find_next(mini.key)
