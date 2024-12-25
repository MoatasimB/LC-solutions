class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getWords(i):

            line = []
            curr_length = 0

            while i<len(words) and curr_length + len(words[i])<=maxWidth:
                line.append(words[i])
                curr_length += len(words[i]) + 1
                i+=1
            
            return line
        

        def create(line, i):
            totalCh = -1
            for w in line:
                totalCh+=len(w) + 1
            
            spaces = maxWidth - totalCh
            if len(line)==1 or i==len(words):
                return " ".join(line) + " " * spaces

            betweenWords = spaces // (len(line) - 1)
            extraSpaces = spaces % (len(line) - 1)

            
       
            for j in range(extraSpaces):
                line[j] += " "
            
                        
       
            for j in range(len(line) - 1):
                line[j] += " "*betweenWords
            
            return " ".join(line)
        
        ans = []
        i=0
        while i<len(words):
            line = getWords(i)
            i+= len(line)
            ans.append(create(line, i))
        
        return ans
