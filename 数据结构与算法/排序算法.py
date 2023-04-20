#%%
def bubblesort(alist):
    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            if alist[i]>alist[j]:
                alist[i],alist[j]=alist[j],alist[i]
    return alist
print(bubblesort([9,2,1,5,1,5,7,88]))


#%%
def insetsort(alist):
    for i in range(1,len(alist)):
        currentvalue=alist[i]
        poisition=i
        while poisition>0 and alist[poisition-1]>currentvalue:
            alist[poisition]=alist[poisition-1]
            poisition-=1
        alist[poisition]=currentvalue
    return alist
insetsort([7,2,1,5,3,5])

#%%
def shellsort(alist):
    