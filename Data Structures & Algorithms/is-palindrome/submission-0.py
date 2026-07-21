class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        clean = "".join(char for char in s if char not in string.punctuation)
        clean_str = clean.replace(" ","").lower()
        return clean_str[::-1] == clean_str