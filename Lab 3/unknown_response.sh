#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say "I didn't understand that. Can you repeat that?"

#record respondent's answer
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav repeat_response.wav
python3 my_vosk_engine.py repeat_response.wav