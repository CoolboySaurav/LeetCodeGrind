class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        if longUrl not in self.encodeMap:
            shortUrl  = self.base + str(1 + len(self.encodeMap))
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
            
        return self.encodeMap[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))