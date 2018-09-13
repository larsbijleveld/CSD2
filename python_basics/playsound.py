import simpleaudio as sa
i = 0

insert = input("Please tell me how many times you would like to hear the vinyl ripple. ")
insert = int(insert)
while( i < insert):
  wave_obj = sa.WaveObject.from_wave_file("vinyl1.wav")
  play_obj = wave_obj.play()
  play_obj.wait_done()
  i += 1
