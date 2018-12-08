def findMin(l):
    min = -1
    for i in l:
        print (i)
        if i<min:
            min = i
    print("the lowest value is: ",min)
    
l=[12,0,15,-30,-24,40]
findMin(l)
