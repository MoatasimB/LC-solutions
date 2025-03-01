class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def getLine(i):

            ans = []
            currL = 0
            while i < len(words) and len(words[i]) + currL <= maxWidth:
                currL += len(words[i]) + 1
                ans.append(words[i])
                i += 1
            return ans
        
        def makeLine(line, i):
            totalCh = -1
            for word in line:
                totalCh += len(word) + 1
            
            s = maxWidth - totalCh


            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * s
            
            spaces = s // (len(line) - 1)
            extraSpaces = s % (len(line) - 1)
            
            for j in range(extraSpaces):
                line[j] += " "
            
            for j in range(len(line) - 1):
                line[j] += " " * spaces
            
            return " ".join(line)

        final = []

        i = 0
        while i <len(words):
            line = getLine(i)
            i += len(line)
            final.append(makeLine(line,i))
        
        return final
