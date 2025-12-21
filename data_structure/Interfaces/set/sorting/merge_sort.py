############################
## Merge Sort Example
############################
def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # one list is empty
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, detail = False):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        # divide
        left = merge_sort(L[:middle], detail)
        right = merge_sort(L[middle:], detail)
        if detail == True:
            print("Merging", left, "and", right)
        # conquer
        return merge(left, right)

# print("--- MERGE SORT ---")
# L = [8, 4, 1, 6, 5, 11, 2, 0]
# print('L:       ', L)
# print(merge_sort(L, True))
