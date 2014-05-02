import os


class HighScore:
    def __init__(self):
        self.songs = []
        
    def readFile(self, filename = "highscore.dat"):
        with open(filename, 'r') as f:
            self.filename = filename
            r = f.read().strip()
            eachSong = r.split("\n\n")
            
            for songData in eachSong:
                tmp = Song()
                tmp.parseDat(songData.split("\n"))

                self.songs.append(tmp)

        return self

    def saveFile(self, filename = None):
        if filename == None:
            filename = self.filename

        with open(filename, 'w') as f:
            lines = []
            for s in self.songs:
                lines.append(s.name+"\n")
                for l in s.slotList:
                    lines.append(l.name+"\n"+str(l.score)+"\n")
                lines.append("\n")
            f.writelines(lines)
        return self
            

    def __str__(self):
        ret = "--\n"
        for e in self.songs:
            ret += str(e)
            ret += "--\n"
        return ret
        


class Song:
    def __init__(self):
        self.name = "no name"
        self.slotList = []


        
    def parseDat(self, dataList):
        self.name = dataList[0]

        n = int(len(dataList)/2)

        for i in range(n):
            tmp=slot()
            tmp.set(dataList[i*2+1], int(dataList[i*2+2]))
            self.slotList.append(tmp)

    def place(self, num):
        try:
            ret = self.slotList[num]
        except:
            ret = slot()
            ret.set("Hyeon-Gi Henry Jeon", "hgijeon@gmail.com")
        return ret

    def __str__(self):
        ret = self.name+"\n"
        for e in self.slotList:
            ret += str(e)+"\n"
        return ret
            

class slot:
    def __init__(self):
        self.set("blank", 0)

    def set(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name+": "+str(self.score)


if __name__ == "__main__":
    tmp = HighScore().readFile()
    print(tmp)
    tmp.saveFile()