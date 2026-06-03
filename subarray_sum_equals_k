class Solution:
    def commonElements(self, a, b, c):
        i = j = k = 0
        ans = []

        while i < len(a) and j < len(b) and k < len(c):

            if a[i] == b[j] == c[k]:

                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])

                i += 1
                j += 1
                k += 1

            else:
                mn = min(a[i], b[j], c[k])

                if a[i] == mn:
                    i += 1
                if b[j] == mn:
                    j += 1
                if c[k] == mn:
                    k += 1

        return ans
