#!/bin/bash

scrot /tmp/screen.png
convert /tmp/screen.png -blur 0x5 /tmp/screen_blur.png
i3lock -i /tmp/screen_blur.png -u
rm /tmp/screen.png /tmp/screen_blur.png
