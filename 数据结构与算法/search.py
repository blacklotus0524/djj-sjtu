#%%
def binarysearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while last>=first and not found:
        mid=(first+last)//2
        if item==alist[mid]:
            found=True
        elif item>alist[mid]:
            first=mid+1
        else:
            last=mid-1
    return found

print(binarysearch([1,22,45,67,86,12213],22))
        



#%%
def binarysearch(alist,item):
    if len(alist)==0:
        return False
    else:
        if alist[len(alist)//2]==item:
            return True
        else:
            if item<alist[len(alist)//2]:
                return binarysearch(alist[:len(alist)//2],item)
            elif item>alist[len(alist)//2]:
                return binarysearch(alist[len(alist)//2+1:],item)
print(binarysearch([1,22,45,67,86,12213],22))
# %%
