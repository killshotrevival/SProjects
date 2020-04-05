from itertools import permutations

def next_bigger(n):
    s = str(n)
    l = [i for i in s]
    p = permutations(l)
    j=n+1
    for i in p:
    	print(i)
    while(str(j) not in p):
        print(j)
        j+=1
    return j

print(next_bigger(513))