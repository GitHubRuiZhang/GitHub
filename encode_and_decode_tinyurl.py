# python3
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


# My solution
class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_short:
            return
        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))
        while code in self.short_long:
            code = ''
            for i in range(6):
                code += str(random.randint(0, 9))

        self.long_short[longUrl] = code
        self.short_long[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        idx = shortUrl.split('/')[-1]
        return self.short_long[idx]



        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))