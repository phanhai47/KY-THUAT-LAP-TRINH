def Binary_Search(dlist, value):
    first = 0
    last = len(dlist) - 1
    found = False
    #vi tri ban dau la -1 (khong tim thay)
    position = -1
    while first <= last and not found:
        #tinh chi so giua
        midpoint = (first + last) // 2
        if dlist[midpoint] == value:
            found = True
            position = midpoint
        elif value < dlist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    if found:
        return True, position
    else:
        return False, -1