# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        l=0
        r=0
        ma=0
        for i in range(len(fruits)):
            if fruits[i] in d:
                d[fruits[i]]+=1
            else:
                d[fruits[i]]=1
            while len(d)>2:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            ma=max(ma,r-l+1)
            r+=1
        return ma
