class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(ransomNote == magazine or ransomNote == ''):
            return True
        
        for i in ransomNote:
            if(ransomNote.count(i) > magazine.count(i)):
                return False
    
        return True
        