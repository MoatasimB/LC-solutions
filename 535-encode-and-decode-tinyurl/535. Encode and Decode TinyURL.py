class Codec:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    mpp = {}
    def createKey(self):
        key = ""
        for i in range(6):
            key += self.chars[random.randint(0, 61)]
        return key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.createKey()
        while key in self.mpp:
            key = self.createKey()
        
        self.mpp[key] = longUrl

        return "http://tinyurl.com/" + key




        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        lst = shortUrl.split("http://tinyurl.com/")
        return self.mpp[lst[1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))