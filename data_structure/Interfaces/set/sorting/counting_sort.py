def counting_sort(Array):
    """Sort(Array) assuming items have non-negative keys"""
    u = 1 + max([x.key for x in Array])  # O(n) find maximum key
    DAA_with_Chain = [[] for i in range(u)]  # O(u) direct access array of chains
    for x in Array:  # O(n) insert into chain at x.key
        DAA_with_Chain[x.key].append(x)

    i = 0
    for chain in DAA_with_Chain:  # O(u) read out items in order
        for x in chain:
            Array[i] = x
            i += 1
