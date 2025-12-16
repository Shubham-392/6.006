from data_structure.Interfaces.sequence.array_seq import ArraySequence


class SortedArraySet:
    def __init__(self):
        self.A = ArraySequence()  # O(1)

    def __len__(self):
        return len(self.A)  # O(1)

    def __iter__(self):
        yield from self.A  # O(n)

    def iter_ord(self):  # O(n)
        """return the stored item one-by-one in key order."""
        yield from self

    def build(self, X):  # O(?)
        """
        given an iterable X, build set from items in X.
        """
        self.A.build(X)  # O(n)
        self._sort()  # O(?)

    def _sort():  # O(?)
        pass

    def _binary_search(self, target_key, lower_limit, upper_limit):  # O(log(n))
        if lower_limit >= upper_limit:
            return lower_limit

        mid = (lower_limit + upper_limit) // 2
        mid_item = self.A.get_at(mid)

        if mid_item.key > target_key:
            return self._binary_search(target_key, lower_limit, upper_limit=mid - 1)

        if mid_item.key < target_key:
            return self._binary_search(
                target_key, lower_limit=mid + 1, upper_limit=upper_limit
            )

        return mid

    def find_min(self):  # O(1)
        """
        return the stored item with smallest key.
        """
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self):  # O(1)
        """
        return the stored item with largest key.
        """
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def find(self, key):  # O(logn)
        if len(self) == 0:
            return None
        index = self._binary_search(key, 0, len(self) - 1)
        item = self.A.get_at(index)
        if item.key == key:
            return item
        else:
            return None

    def find_next(self, key):  # O(logn)
        if len(self) == 0:
            return None
        index = self._binary_search(key, 0, len(self) - 1)
        item = self.A.get_at(index)
        if item.key > key:
            return item
        if index + 1 < len(self):
            return self.A.get_at(index + 1)
        else:
            return None

    def insert(self, x):
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self) - 1)
            k = self.A.get_at(i).key
            if x.key == k:
                self.A.set_at(i, x)
                return False
            if k > x.key:
                self.A.insert_at(i, x)
            else:
                self.A.insert_at(i + 1, x)
        return True

    def delete(self, k):
        i = self._binary_search(k, 0, len(self) - 1)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)
