from Structure.Middle.pianoKey import pianoKey
import os

p = pianoKey(os.path.join("Music", "Twinkle Twinkle Little Star.mid"))

for i in range(128):
    print("\n%d: "%i,end="")
    for j in p.keyList[i]:
        try:
            print("(%g, %g), "%(j.startTime, j.endTime),end="")
        except:
            print("\n-----Exception startTime and endTime-----")
            print(j.startTime)
            print(j.endTime)
            raise
