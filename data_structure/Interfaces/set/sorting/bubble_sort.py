############################
## Bubble Sort Example
############################
def bubble_sort(L, detail = False):
    did_swap = True
    while did_swap:
        did_swap = False
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                did_swap = True
                L[j],L[j-1] = L[j-1],L[j]
            if detail == True:
                print(L)
        print()

# print("--- BUBBLE SORT ---")
# L = [8, 4, 1, 6, 5, 11, 2, 0]
# print('L:       ', L)
# bubble_sort(L, True)
# print('Sorted L:', L)
