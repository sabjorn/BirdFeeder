##Jan 8/15
* *PyAudio* plays sound but then crashes python script. An alternative may need to be found.
** `aplay` works and although not ideal, will be used for now
* Having the Ultrasonic object run on separate thread would be ideal (non-blocking)
* System works successfully!

##Jan 6/15
* beaglebone connects to goPro over wifi (automatically at startup).
* need hysterisis on theshold
* python script should be setup as 'command line' so variables like *wifi pass*, *theshold value*, *length of record*