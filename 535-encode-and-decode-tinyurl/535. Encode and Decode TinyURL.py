class Codec:

    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mpp = {}
    def getKey(self):
        key = []
        for i in range(6):
            key.append(self.s[random.randint(0, len(self.s) - 1)])
        
        return "".join(key)
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.getKey()
        while key in self.mpp:
            key = self.getKey()
        
        self.mpp[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        string = shortUrl.split("http://tinyurl.com/")
        return self.mpp[string[1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))