# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        def getHostName(url):
            hostName = url[7:].split("/")[0]
            hostName = "http://" + hostName
            return hostName

        ans = [startUrl]
        seen = set([startUrl])
        def dfs(node):
            myHostName = getHostName(node)
            for nei in htmlParser.getUrls(node):
                neiHostName = getHostName(nei)
                
                if nei not in seen and neiHostName == myHostName:
                    seen.add(nei)
                    ans.append(nei)
                    dfs(nei)
        
        dfs(startUrl)
        return ans
