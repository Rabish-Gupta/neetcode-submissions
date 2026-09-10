class Solution:
    string = {}
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        i = len(strs)
        for s in strs:
            encoded += s+'~'
            i -= 1
        return encoded


    def decode(self, s: str) -> List[str]:
        lst = []
        for i in s:
            lst = s.split('~')
        return lst[:-1]


