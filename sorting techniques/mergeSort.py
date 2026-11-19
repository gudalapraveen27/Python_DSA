def merge(ar,br):
    cr = []
    i=0
    j=0
    while i<len(ar) and j<len(br):
        if ar[i]<br[j]:
            cr.append(ar[i])
            i+=1
        else:
            cr.append(br[j])
            j+=1
    cr.extend(ar[i:])
    cr.extend(br[j:])
    return cr

def merge_sort(ar,width):
    result = []
    for i in range(0,len(ar),width*2):
        left = ar[i:i+width]
        right = ar[i+width:i+width*2]
        result.extend(merge(left,right))
    return result

k = [9,8,5,4,7,3,10,5]
width = 1
while width < len(k):
    k = merge_sort(k,width)
    print(k)
    width*=2
print(k)



# x = [34,54,67,87,99,105,300,367]
# y = [10,22,56,98,101]
# print(merge(x,y))