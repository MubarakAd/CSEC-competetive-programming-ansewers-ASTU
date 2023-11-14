class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i=0
        sum=0
        j=len(skill)-1
        skill.sort()
        while i<j:
            
            if len(skill)==2:
                sum+=(skill[i]*skill[j])
                break
            
            elif skill[i]+skill[j]==skill[i+1]+skill[j-1]:
                sum+=(skill[i]*skill[j])
                i+=1
                j-=1
            else:
                sum=-1
                break
            if (j)-(i)==1:
                sum+=(skill[i]*skill[j])
                break
        return sum
