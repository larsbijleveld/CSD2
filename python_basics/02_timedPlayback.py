import simpleaudio as sa
import time

"""
An example project in which three wav files are played after eachother with a
minor break in between.

------ HANDS-ON TIPS ------
- Alter the code:
  Write a function that plays the samples a given number of times.
  Use this function.


- Alter the code:
  Change the time in between samples into a random value.
  E.g. wait 0.25, 0.5, or 1 second.
  hint:  there is a standard random package available with a random function
         https://docs.python.org/2/library/random.html
         A standard package does not need to be installed with pip, but it does
         need to be imported.
"""
#user input
n = input("How much bro? ")
n = int(n)

# load 3 audioFiles into a list
samples = [ sa.WaveObject.from_wave_file("audioFiles/robo1.wav"),
            sa.WaveObject.from_wave_file("audioFiles/vinyl1.wav"),
            sa.WaveObject.from_wave_file("audioFiles/noise1.wav")]

#function plays amount of times from input
def multiPlay(n):
    for n in range(0, n):
        # play samples, wait 1 second in between
        for sample in samples:
            # display the sample object
            print(sample)
            # play sample
            sample.play()
            # wait 1 second
            time.sleep(1)
    n += 1

#calls function
multiPlay(n)
