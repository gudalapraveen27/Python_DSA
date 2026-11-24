def toh(n,s,d,a):
    if n == 1:
        print(f"{n} moves from {s} to {d}")
        return
    toh(n-1,s,a,d)
    print(f"{n} moves from {s} to {d}")
    toh(n-1,a,d,s)

toh(4,"A","B","C")