class DictSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return False if the word don't have the same lenght
        if len(s) != len(t):
            return False
    
        # Create a dictionnary to store the characters that appear and how namy times they appear
        s_dict = {}
        t_dict = {}
        
        # Iterate over the characters in s and t
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        # Compare the dictionaries
        return s_dict == t_dict
    

solution = DictSolution()

#Input :
s1 = "qwerty"
t1 = "yrtewq"

s2 = "jar"
t2 = "jam"

if __name__ == '__main__':

    print(f"{s1} and {t1} are anagrams: {solution.isAnagram(s1, t1)}")
    print(f"{s2} and {t2} are anagrams: {solution.isAnagram(s2, t2)}")
    
    