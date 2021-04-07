
class FileDict:
    def printMap(MAp):
        for key in list(MAp.keys()):
            print(key,"-",MAp[key])
    
    def funct(FileS):
        file = open(FileS, "rt")
        data = file.read()
        words = data.split()

        d = dict()

        for word in words:
            if word in d:
                d[word]=d[word]+1
            else:
                #print(words)
                d[word]=1
        FileDict.printMap(d)        
        

FileDict.funct("test.txt")

#print('Number of words in text file :', len(words))
