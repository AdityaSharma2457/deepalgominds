class Solution:
    def removeUtil (self, s):
		
		
		def recursion(s,i,last_rem,changed):
		    if len(s) <= 1:
                return s
		    if i>=len(s)-1:
		        if changed:
		            return recursion(s,0,None,False)
		        return s
		    if s[i]==s[i+1]:
		        last_rem = s[i]
		        while i + 1 < len(s) and s[i] == s[i + 1]:
                    s = s[:i] + s[i + 1:]

                s = s[:i] + s[i + 1:]
		        
		        
		        return recursion(s,i,last_rem,True)
		    if last_rem is not None and s[i]==last_rem:
		        s=s[:i]+s[i+1:]
		        
		        
		        return recursion(s,i,last_rem,True)
		    else:
		        last_rem=None
		        return recursion(s,i+1,last_rem,changed)
		return recursion(s,0,None,False)
