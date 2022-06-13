#!/bin/bash

DATETIME=`date +"%Y-%m-%dT%T"`
DIR=/home/pi/rpi_live/photos
FILENAME=${DATETIME}.jpg
FILE=${DIR}/${FILENAME}

killall libcamera-still
libcamera-still --vflip --hflip --immediate -t 60000 -o ${FILE}
scp ${FILE} sagan:~/rpi_live/photos/${FILENAME}
