#verbally ask for zip code input
#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "What is the zip code for your home town?"

#record respondent's answer
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
python3 my_vosk_engine.py recorded_mono.wav

