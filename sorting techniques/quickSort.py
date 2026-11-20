
def quickSort(ar):
    if len(ar)<=1:
        return ar
    pivot = len(ar)-1
    i = 0
    for j in range(len(ar)-1):
        if ar[j]<ar[pivot]:
            ar[i],ar[j]=ar[j],ar[i]
            i+=1
    ar[i],ar[pivot] = ar[pivot],ar[i]
    left = quickSort(ar[:i])
    right = quickSort(ar[i+1 :])
    return left+[ar[i]]+right


lst = [12,10,4,30,6,48,77,78,85,63,24]
print(quickSort(lst))
