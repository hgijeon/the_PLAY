import os


class HighScore:
    def __init__(self):
        self.songs = []
        
    def loadFile(self, filename = "highscore.dat"):
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

    def getTarget(self, name, score):
        try:
            index = self.songs.index(name)
            song = self.songs[index]
        except ValueError:
            song = Song()
            song.name = name
            self.songs.append(song)

        rank = 0
        for e in song.slotList:
            if e.score > score:
                rank += 1
            else:
                break
        
        song.slotList.insert(rank, slot().set("",score))
        return (song, rank)
            
        


class Song:
    def __eq__(self, value):
        return value == self.name
    
    def __init__(self):
        self.name = "no name"
        self.slotList = dummySlotList()


        
    def parseDat(self, dataList):
        self.name = dataList[0]

        n = int(len(dataList)/2)

        for i in range(n):
            tmp=slot()
            tmp.set(dataList[i*2+1], int(dataList[i*2+2]))
            self.slotList.append(tmp)

        self.slotList.sort()
        self.slotList.reverse()

    def __str__(self):
        ret = self.name+"\n"
        for e in self.slotList:
            ret += str(e)+"\n"
        return ret

class dummySlotList(list):
    def __getitem__(self, index):
        try:
            ret = super().__getitem__(index)
        except:
            ret = slot()
            ret.set("Hyeon-Gi Henry Jeon", "hgijeon@gmail.com")
        return ret
        

class slot:
    def __init__(self):
        self.set("blank", 0)

    def __lt__(self, right):
        return self.score < right.score
    def __le__(self, right):
        return self.score <= right.score
    def __gt__(self, right):
        return self.score > right.score
    def __ge__(self, right):
        return self.score >= right.score

    def set(self, name, score):
        self.name = name
        self.score = score

        return self

    def __str__(self):
        return self.name+": "+str(self.score)


if __name__ == "__main__":
    tmp = HighScore().loadFile()
    print(tmp)
    tmp.saveFile()
