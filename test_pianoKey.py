from Structure.Middle.pianoKey import pianoKey

p = pianoKey("Music/minuet1track.mid")

for i in range(128):
    print("\n%d: "%i,end="")
    for j in p.keyList[i]:
        print("(%g, %g), "%(j.startTime, j.endTime),end="")
