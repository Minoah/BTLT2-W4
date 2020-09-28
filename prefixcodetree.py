
class TrieNode:
    def __init__(self, code = [],symbol=''):
        self.code = code
        self.symbol=symbol
        self.children = dict()
        self.is_leaf = False

class PrefixCodeTree:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, codeword, symbol):
        current=self.root
        sym=''
        for i, num in enumerate(codeword):
           # sym+=chr(num+48)
            if num not in current.children:
                prefix = [n for y,n in enumerate(codeword) if(y<i+1)]
                current.children[num] = TrieNode(prefix,'')
            current = current.children[num]
        current.is_leaf = True
        current.symbol = symbol
    def decode(self,encodedData, datalen):
        l=len(encodedData)
        s=''
        for i in range(l):
            sam=bin(encodedData[i])[2:]
            while len(sam) < 8:
                sam = '0' + sam
            s+=sam
        s=s[0:datalen]
        decodedData = ''
        index = 0;
        while index < datalen:
            current = self.root;
            while(not current.is_leaf):
                j=ord(s[index])-48
                current=current.children[j]
                index+=1;
            decodedData += current.symbol
        return decodedData

        
# codebook = {
# 'x1': [0],
# 'x2': [1,0,0],
# 'x3': [1,0,1],
# 'x4': [1,1]
# }

# codeTree = PrefixCodeTree()
# for symbol in codebook:
#   codeTree.insert(codebook[symbol], symbol)
# message = codeTree.decode(b'\xd2\x9f\x20', 21)
# print(message)
