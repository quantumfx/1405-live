#!/bin/bash

DATETIME=`date +"%Y-%m-%dT%T"`
DIR=/home/pi/rpi_live/photos
FILENAME=${DATETIME}.jpg
FILE=${DIR}/${FILENAME}

libcamera-still --vflip -o ${FILE}
scp ${FILE} sagan:~/rpi_live/photos/${FILENAME}
