class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = {
            'a': 2,
            'b': 3,
            'c': 5,
            'd': 7,
            'e': 11,
            'f': 13,
            'g': 17,
            'h': 19,
            'g': 23,
            'h': 29,
            'i': 31,
            'j': 37,
            'k': 41,
            'l': 43,
            'm': 47,
            'n': 53,
            'o': 59,
            'p': 61,
            'q': 67,
            'r': 71,
            's': 73,
            't': 79,
            'u': 83,
            'v': 89,
            'w': 97,
            'x': 101,
            'y': 103,
            'z': 107
        }

        products = defaultdict(list)

        for s in strs:
            # compute prime product
            prod = 1
            for c in s:
                prod *= primes[c]
            
            products[prod].append(s)
        
        return list(products.values())




