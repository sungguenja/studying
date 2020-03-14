def merge(m):
    if len(m)<=1:
        return m

    mid=len(m)//2
    left=m[:mid]
    right=m[mid:]

    left=merge(left)
    right=merge(right)

    return sorting(left,right)

def sorting(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0]>right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if len(left)>=1:
        result.extend(left)
    if len(right)>=1:
        result.extend(right)

    return result

A=[69,10,30,2,16,8,31,22]
B=merge(A)
print(A)
print(B)