from gi_sound import GiSound
import time


def play_note(sound, note, tone_length, delay):
    sound.set_volume(1, 1, 1)
    sound.set_tone(note, note, note)
    time.sleep(tone_length)
    sound.set_volume(0, 0, 0)
    time.sleep(delay)


def main():
    # Initialize sound object with pin definition.
    sound = GiSound(d0=8, d1=10, d2=12, d3=16, d4=18, d5=22, d6=24, d7=26, bc1=36, bdir=38, reset=40)

    # Set mixer; 1=0N, 0=OFF; (toneA, toneB, toneC, noiseA, noiseB, noiseC)
    sound.set_mixer(1, 1, 1, 0, 0, 0)
    # Set volume; 1=0N, 0=OFF; (volumeA, volumeB, volumeC)
    sound.set_volume(1, 1, 1)

    # C major key.
    note_a = int((2000000 / 16) / 440)
    note_b = int((2000000 / 16) / 493.88)
    note_b_minor = int((2000000 / 16) / 246.94)
    note_c = int((2000000 / 16) / 261.63)
    note_c5 = int((2000000 / 16) / 523.25)
    note_d = int((2000000 / 16) / 293.66)
    note_d_sharp = int((2000000 / 16) / 311.13)
    note_e = int((2000000 / 16) / 329.63)
    note_f = int((2000000 / 16) / 349.23)
    note_f_sharp = int((2000000 / 16) / 369.99)
    note_g = int((2000000 / 16) / 392)
    
    tone_length = 0.2
    delay = 0.07

    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_b_minor, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_b_minor, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)

    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_f_sharp, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_f_sharp, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c5, tone_length, delay)
    play_note(sound, note_c5, tone_length, delay)
    play_note(sound, note_c5, tone_length, delay)

    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_f_sharp, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_d_sharp, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_b_minor, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_b_minor, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
   
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_f, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_d, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_c, tone_length, delay)

    play_note(sound, note_c, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_e, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_b, tone_length, delay)
    play_note(sound, note_a, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_b_minor, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_g, tone_length, delay)
    play_note(sound, note_f_sharp, tone_length, delay)
    play_note(sound, note_g, 1, delay)
     
    # Turn off all sound output.
    sound.volume_off()

    return


if __name__ == "__main__":
    main()
