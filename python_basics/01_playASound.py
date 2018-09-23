# simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

"""
An example project in which three wav files are played after eachother.
------ HANDS-ON TIPS ------
- Answer the following question before running the code:
  Do you expect to hear the samples played simultaniously or after eachother?
  Why?

  After eachother because in the code you can find: sampleMidPlay.wait_done() wich means
  when a sample is played the next sample will wait till the previous is done playing.

- Alter the code:
  Play the sounds simultaniously.

  Check

- Alter the code:
  Ask the user to choice which one of the three samples should be played and
  only play the chosen sample.
"""

#user input
selection = input("Wich sample would you like to hear? Press 1 for robo, 2 for noise and 3 for vinyl! ")
selection = int(selection)

# load 3 audioFiles
sampleHigh = sa.WaveObject.from_wave_file("audioFiles/robo1.wav")
sampleMid = sa.WaveObject.from_wave_file("audioFiles/noise1.wav")
sampleLow = sa.WaveObject.from_wave_file("audioFiles/vinyl1.wav")

# play high sample
if selection == 1:
    sampleHighPlay = sampleHigh.play()
# wait till sample is done playing
    print("All duck its a MECH!")
    sampleHighPlay.wait_done()

if selection == 2:
# play mid sample
    sampleMidPlay = sampleMid.play()
# wait till sample is done playing
    print("Noise is the best!")
    sampleMidPlay.wait_done()

if selection == 3:
# play low sample
    sampleLowPlay = sampleLow.play()
# wait till sample is done playing
    print("The warmth of vinyl, YES!")
    sampleLowPlay.wait_done()
