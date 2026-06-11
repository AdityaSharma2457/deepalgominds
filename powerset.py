class Solution:
	def powerSet(self, s):
        ans=[]
		for i in range(2**len(s)):
		    temp=""
		    j=0
		    while(i):
		        if(i&1):
		            temp+=s[j]
		        j+=1
		        i=i>>1
		    ans.append(temp)
		ans.sort()
		return ans
