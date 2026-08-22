class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        new_message = []

        for word in strs:
            n = len(word)
            new_message.append(str(n) + "#" + word)
        return "".join(new_message)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        print(s)
        i = 0
        while i < len(s):
            j = i
            curr_word_len = 0
            while j < len(s) and s[j] != "#":
                curr_word_len = curr_word_len * 10 + int(s[j])
                j += 1

            j += 1
            ans.append(s[j: j + curr_word_len])
            i = j + curr_word_len
        return ans
        


            




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))