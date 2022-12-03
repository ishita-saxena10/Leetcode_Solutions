class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] =1
            else:
                freq[char] +=1
        char_sorted = sorted(freq, key=freq.get, reverse = True)
        
        res = ""
        for char in char_sorted:
            res = res + char*freq[char]
        return res