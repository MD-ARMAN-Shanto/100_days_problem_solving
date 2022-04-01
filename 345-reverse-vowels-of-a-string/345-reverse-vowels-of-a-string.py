class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        l, h =0, len(s) - 1
        
        v = set(list("aeiouAEIOU"))
        
        while l < h:
            if s[l] not in v:
                l += 1
            elif s[h] not in v:
                h -= 1
            else:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
                
        return ''.join(s)
                
        
            
            
            
        
        
                
            
                