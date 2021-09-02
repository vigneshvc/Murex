import time
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l
for i in range(1,15):
    start = time.time()
    ans = len(permutation([ j for j in range(1,i+1)]))
    print('Iteration -',i,'\n Total Count :',ans,'\n Time Taken -',round(time.time()-start,2),'seconds\n') 