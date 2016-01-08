* [adafruit beaglebone io](https://github.com/adafruit/adafruit-beaglebone-io-python)
`sudo pip install Adafruit_BBIO`

* [gopro python library](http://goprohero.readthedocs.org/en/latest/)
`sudo pip install goprohero`

* ALSA
`sudo apt-get install alsa-base`
**then**
From [here](http://superuser.com/questions/626606/how-to-make-alsa-pick-a-preferred-sound-device-automatically)

Find your card with

cat /proc/asound/cards
and then create /etc/asound.conf with following:

pcm.!default {
    type hw
    card 1
}

ctl.!default {
    type hw           
    card 1
}

but [this](http://www.alsa-project.org/main/index.php/Asoundrc) also seems to be important?

`sudo vim /etc/modprobe.d/alsa-base.conf` **change line 33** `options snd-usb-audio index=-2` **to** `options snd-usb-audio index=-1` **and delete lines** *42 and 43* (`#Keep snd-usb-audio from beeing loaded as first soundcard`
`options snd-usb-audio index=-2`)
**then reboot!**
**It may then be neccessary to open `alsamixer` and adjust the volume.

* [pyaudio](https://github.com/jleb/pyaudio)
`sudo apt-get install python-pyaudio`