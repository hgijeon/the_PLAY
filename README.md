the_PLAY
========

POE Project, "the_PLAY"

What it needs
========

Python3, PyGame and Linux for using MIDI input<br />
Check with command 'python3'

How to install PyGame for Python3 in Ubuntu
========

refer to 
http://danielj.se/2012/06/16/how-to-install-pygame-to-python-3-on-ubuntu/

pre-install pygame:<br />
sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev checkinstall mercurial


download pygame source code:<br />
hg clone https://bitbucket.org/pygame/pygame

change directory to source code, build the source, and finally install pygame for python3:<br />
cd pygame<br />
python3 setup.py build<br />
sudo checkinstall python3 setup.py install
