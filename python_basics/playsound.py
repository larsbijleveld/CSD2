#import modules
import simpleaudio as sa
import time
from random import randint

#array with rhythm possibilities
rhythm = [0.125, 0.25, 0.5, 1, 2, 4]

#random bpm count between 60 and 180
bpm = randint(20, 40)

#empty list
sequence = []
x = 0

#input from user
numPlaybackTimes = input("Gimme some RHYTHM! ")
numPlaybackTimes = int(numPlaybackTimes)

#create list with random rhythm values
for i in range(0, numPlaybackTimes):
    sequence.append(rhythm[randint(0, 5)])
print(sequence)
print(bpm)

#forloop with scrolling "sequence" trough "bpm" with playing sound file.
while (x < bpm):
    time.sleep(sequence[0])
    bpm = bpm - sequence[0]
    sequence.append(sequence[0])
    del(sequence[0])
    wave_obj = sa.WaveObject.from_wave_file("noise1.wav")
    play_obj = wave_obj.play()
    print(bpm)
#if statement to reintiate loop with new bpm value
    if bpm <= 0:
        bpm = randint(20, 40)
        sequence.append(rhythm[randint(0, 5)])
        print(sequence)
        print(bpm)
