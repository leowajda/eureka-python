from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        start, end = len(p), len(s)
        original, window = Counter(p), Counter(s[:start])

        anagrams = []
        for i in range(start, end):
            if original == window:
                anagrams.append(i - start)

            window[s[i - start]] -= 1
            window[s[i]] += 1

        return anagrams + [end - start] if original == window else anagrams
