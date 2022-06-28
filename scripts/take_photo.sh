#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME

killall libcamera-still
libcamera-still --vflip --hflip --immediate -t 30000 -o $FILE --shutter 10000000
rsync -P $FILE sagan:~/rpi_live/photos/$FILENAME
