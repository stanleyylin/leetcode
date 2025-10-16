class Solution:
    def expand(self, s: str) -> List[str]:
        self.res = []
        def builder(s, word): # s - remaining to process, word - what we have so far
            if not s:
                self.res.append(word)
                return
            if s[0] == "{":
                idx = s.find("}")
                for option in s[1:idx].split(","):
                    builder(s[idx+1:], word + option)
            else:
                builder(s[1:], word+s[0])
        builder(s, "")
        self.res.sort()
        return self.res


            
