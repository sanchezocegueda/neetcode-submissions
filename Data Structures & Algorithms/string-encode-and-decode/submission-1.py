class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)

        small_delimiter = "_"
        delimiter = ":"

        lengths = [str(len(s)) for s in strs]

        encoding = str(n) + ":" + "_".join(lengths) + ":" + "_".join(strs)
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        # Unpack the header
        decoding = []
        i = 0
        while s[i] != ":":
            i += 1
        
        # Get number of elements
        n = int(s[0:i])
        print(n)

        # l = length_index, w = word_index
        l = i + 1
        w = l
        while s[w] != ":":
            w += 1
        w += 1

        for i in range(n):
            print(i)
            
            # Get word length
            r = l
            while s[r] != '_' and s[r] != ':':
                r += 1

            word_length = int(s[l:r])

            l = r + 1

            # if word_length == 0:
            #     decoding.append("0")

            # Get word
            word = s[w:w+word_length]
            decoding.append(word)

            # Increase word index
            w += word_length + 1


        # Get starting point of words


        return decoding
