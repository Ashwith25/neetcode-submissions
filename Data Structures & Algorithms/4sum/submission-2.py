class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        L = len(nums)
        a=0
        res = []

        while a<L-3:
            if a>0 and nums[a]==nums[a-1]:
                a+=1
                continue
            b = a+1
            while b<L-2:
                if b>a+1 and nums[b]==nums[b-1]:
                    b+=1
                    continue
                t = target-(nums[a] + nums[b])
                c = b+1
                d = L-1
                while c<d:
                    summ = nums[c] + nums[d]
                    if summ==t:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c+=1
                        d-=1
                    elif summ<t:
                        c+=1
                    else:
                        d-=1
                b+=1
            a+=1

        return res