import winsound
from time import sleep
import random

# major scale stored as frequencies
#        c    c#   d    d#   e    f    f#   g    a    b    c
NOTES = [261, 277, 294, 311, 329, 349, 370, 392, 440, 490, 523]

# folder containing wav files corresponding to the following note filenames
WAVS = ["A", "B", "Bb", "C", "Cs", "D", "E", "Eb", "F", "G"]
FILENAME = "1000.txt"
# how long each beep will last, in milliseconds
DURATION = 150
# digits of pi
def random_beeps(notes):
    for x in range(notes):
        wavfile = "Chords\{}.wav".format(random.randint(0,7))
        winsound.PlaySound(wavfile, winsound.SND_FILENAME|winsound.SND_ASYNC)


def pi_music():
    pi = open(FILENAME, "r")
    # current digit of pi
    curpi = pi.read(1)
    while curpi != "":
        if curpi == ".":
            curpi = pi.read(1)
            continue
        print(curpi, end="", flush=True)
        winsound.Beep(NOTES[int(curpi)], DURATION)
        sleep(DURATION/300)
        curpi = pi.read(1)
    # written.close()
    pi.close()
    
def pi_music_wav():
    pi = open(FILENAME, "r")
    # current digit of pi
    curpi = pi.read(1)
    while curpi != "":
        if curpi == ".":
            curpi = pi.read(1)
            continue
        print(curpi, end="", flush=True)
        wav = "Piano Notes\{}.wav".format(WAVS[int(curpi)])
        winsound.PlaySound(wav, winsound.SND_FILENAME)
        curpi = pi.read(1)
    pi.close()
    

pi_music()
