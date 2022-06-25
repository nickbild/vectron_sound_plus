# Vectron Sound Plus

Vectron Sound Plus uses the General Instrument AY-3-8910 sound generator to produce 8-bit retro audio.

![](https://raw.githubusercontent.com/nickbild/vectron_sound_plus/main/media/vectron_audio_angle_sm.jpg)

## How It Works

The simple design exposes the AY-3-8910's data bus and control pins so that an external system can control it.  The required crystal oscillator and audio output circuitry are also included so that any speaker can be connected via a TRS cable through the onboard jack.

This is the circuit design:
![](https://raw.githubusercontent.com/nickbild/vectron_sound_plus/main/media/schematic.svg)

## Media

![](https://raw.githubusercontent.com/nickbild/vectron_sound_plus/main/media/vectron_audio_top_sm.jpg)

Here, the Vectron Sound Plus is being controlled by the [Vectron 65 Plus computer](https://github.com/nickbild/vectron_65_plus):

![](https://raw.githubusercontent.com/nickbild/vectron_sound_plus/main/media/v65_w_audio_angle_sm.jpg)
![](https://raw.githubusercontent.com/nickbild/vectron_sound_plus/main/media/v65_w_audio_top_sm.jpg)

You can download an [MP3 here](https://github.com/nickbild/vectron_sound_plus/blob/main/media/vectron_65_audio.mp3?raw=true) of a tune I made with it.

## Bill of Materials

- 1 x General Instrument AY-3-8910 sound generator
- 1 x 2 MHz crystal oscillator
- 1 x 220 uF electrolytic capacitor
- 1 x 47 uF electrolytic capacitor
- 1 x 1K resistor
- 2 x 0.1 uF ceramic capacitors
- 1 x TRS jack connector
- 1 x PCB ([Kicad design files](https://github.com/nickbild/vectron_sound_plus/tree/main/vectron_sound_kicad))

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
