 
def Merge(nums,low,mid,high):
        left=low
        right=mid+1
        temp=[]
        while(left<=mid and right<=high):
            if(nums[left]<=nums[right]):
                temp.append(nums[left])
                left=left+1
            else : 
                temp.append(nums[right])
                right=right+1
            
        while(left<=mid):
            temp.append(nums[left])
            left=left+1
        while(right<=high):
            temp.append(nums[right])
            right=right+1
        for i in range(low,high+1):
            nums[i]=temp[i-low]

def MergeSort(nums,low,high):
        if (low>=high):
            return
        mid=(low+high)//2
        MergeSort(nums,low,mid)#left
        MergeSort(nums,mid+1,high)#right
        Merge(nums,low,mid,high)
        return

   

nums=[0,3,4,1,1,0,4]
n=len(nums)
MergeSort(nums,0,n-1)
print(nums)

# 0 0 1 1 3 4 4

