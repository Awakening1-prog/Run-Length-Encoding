class Solution:
    def solve(self, s):
        i=1
        c=0
        res=''
        while i<len(s):
            if s[i-1]==s[i]:
                c+=1
                i+=1
            else:
                res+=str(c+1)+s[i-1]
                c=0
                i+=1
        res+=str(c+1)
        if i!=len(s)-1:
            res+=s[-1]
        print(res)
        return res
