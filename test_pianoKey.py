from Structure.Middle.pianoKey import pianoKey
import os

<<<<<<< HEAD
p = pianoKey(".\MIDI\Music\minuet1track.mid")
=======
p = pianoKey(os.path.join("Music", "Twinkle Twinkle Little Star.mid"))
>>>>>>> feaf66f342f14e6f40130fdff3e32c3a1abf0fb4

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
print(p.endTime)
