# Drone FQ777-954

This code is an attempt to control and capture video from the cheap micro-drone fq777-954. Currently
it's able to send commands and capture video data, however the video data stalls after about 35 seconds.


## Requirements

Opencv + Python bindings
[PyAV](https://mikeboers.github.io/PyAV/installation.html)


## Usage

    python main.py


## Video playback

    mplayer -fps 13 fpv.mp4
