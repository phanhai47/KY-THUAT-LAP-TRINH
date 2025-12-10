def bubbleSort(nlist):
    #thuat toan sap xep noi bot tren danh sach nlist
     n=len(nlist)
     #lap qua tat ca cac phan tu trong danh sach
     for passnum in range(n-1,0,-1):
         #lap qua cac phan tu chua duoc sap xep
        for i in range(passnum):
             #neu phan tu hien tai lon hon phan tu ke tiep
             if nlist[i]>nlist[i+1]:
                 #doi cho hai phan tu
                 temp=nlist[i]
                 nlist[i]=nlist[i+1]
                 nlist[i+1]=temp
                 swapped = True
        if not swapped:
            break
     return nlist