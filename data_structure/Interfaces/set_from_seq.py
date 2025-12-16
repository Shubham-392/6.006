def Set_from_Sequence(seq):
    class set_from_sequence:
        def __init__(self):
            self.S = seq()

        def __len__(self):
            return len(self.S)

        def __iter__(self):
            yield from self.S

        def build(self, A):
            self.S.build(A)

        def insert(self, x):
            for i in range(len(self.S)):
                if self.S.get_at(i, x) == x.key:
                    self.S.set_at(i, x)
                    return
            # If key is not found insert at the last of the sequence
            self.S.insert_last(x)

        def delete(self, key):
            for i in range(len(self.S)):
                if self.S.get_at(i).key == key:
                    return self.S.delete_at(i)

        def iter_ord(self):
            mini = self.find_min()
            while mini:
                yield mini
                mini = self.find_next(mini.key)

        def find(self, k):
            for x in self:
                if x.key == k:
                    return x
            return None

        def find_min(self):
            out = None
            for x in self:
                if (out is None) or (out.key > x.key):
                    out = x
            return out

        def find_max(self):
            out = None
            for x in self:
                if (out is None) or (out.key < x.key):
                    out = x
            return out

        def find_next(self, k):
            out = None
            for x in self:
                if x.key > k:
                    if (out is None) or (x.key < out.key):
                        out = x
            return out

        def find_prev(self, k):
            out = None
            for x in self:
                if x.key < k:
                    if (out is None) or (x.key > out.key):
                        out = x
            return out

    return set_from_sequence
