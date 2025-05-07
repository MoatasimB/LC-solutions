class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Create a hash value
        def get_hash(string: str):
            key = []
            for i in range(1, len(string)):
                #a b c

                curr = string[i] #b
                prev = string[i - 1] #a
                new = chr(((ord(curr) - ord(prev) )% 26) + ord('a'))
                key.append(new)


            # for a, b in zip(string, string[1:]):
            #     key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)
        
        # Create a hash value (hash_key) for each string and append the string
        # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        groups = collections.defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            print(hash_key)
            groups[hash_key].append(string)
        
        # Return a list of all of the grouped strings
        return list(groups.values())