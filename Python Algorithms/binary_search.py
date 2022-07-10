# Binary Search - time complexity: O(log(n))

def binary_search(l, value):
    LOW = 0
    TOP = len(l)-1
    while LOW <= TOP:
        MID = (LOW + TOP) // 2
        if l[MID] > value:
            TOP = MID-1
        elif l[MID] < value:
            LOW = MID+1
        else:
            return MID
    return -1

# Recursive method


def binary_search(l, value, LOW=0, TOP=-1):
    if not l:
        return -1
    if TOP == -1:
        TOP = len(l)-1
    if LOW >= TOP:
        if l[LOW] == value:
            return LOW
        else:
            return -1
    MID = (LOW + TOP) // 2
    if l[MID] > value:
        return binary_search(l, value, LOW, MID-1)
    elif l[MID] < value:
        return binary_search(l, value, MID+1, TOP)
    else:
        return MID
