## Selection Sort Example
############################
def selection_sort(L, detail = False):
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
            if detail:
                print(L)
        print()

# print("--- SELECTION SORT ---")
# L = [8, 4, 1, 6, 5, 11, 2, 0]
# print('L:       ', L)
# selection_sort(L, True)
# print('Sorted L:', L)
