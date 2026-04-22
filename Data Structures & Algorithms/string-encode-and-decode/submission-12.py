class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        elif strs == [""]:
            return 'needs [""]'
        return "ADD".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == 'needs [""]':
            return [""]
        return s.split("ADD")
