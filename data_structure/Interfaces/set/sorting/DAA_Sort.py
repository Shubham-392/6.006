# Suppose all keys are unique non-negative integers in
# range {0, . . . , u − 1}, so n ≤ u
# Insert each item into a direct access array with size u in Θ(n)
# return items in order they appear in direct access array in Θ(u)
# running time is Θ(u), which is Θ(n) if u = Θ(n). Yay!


def direct_access_sort(Array):
    """
    Sort(Array) assuming items have distnict non-negative keys
    """
    u = 1 + max([x.key for x in Array])  # find maximum key
    DAA = [None] * u  # Direct Access Array with size O(u)
    for x in Array:  # O(n) insert items
        DAA[x.key] = x

    i = 0
    for key in range(u):
        if DAA[key] is not None:
            Array[i] = DAA[key]
            i += 1

    return Array
