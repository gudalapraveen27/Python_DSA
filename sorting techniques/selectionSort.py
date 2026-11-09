def selectionSort(ar):
    for i in range(len(ar)-1):
        min_index = i
        for j in range(i+1,len(ar)):
            if ar[j]<ar[min_index]:
                min_index = j
        min_val = ar.pop(min_index)
        ar.insert(i,min_val)
                


if __name__ == "__main__":
    ls = [20,32,14,65,7,12,40]
    selectionSort(ls)
    print(ls)