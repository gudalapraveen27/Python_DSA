def bubbleSort(ar):

    for i in range(len(ar)-1):
        swapped = False

        for j in range(len(ar)-1-i):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1] = ar[j+1],ar[j]
                swapped = True

        if not swapped:
            break

    return ar

ls = bubbleSort([20,32,14,65,7,12,40])
print(ls)