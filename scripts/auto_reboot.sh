#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
PIHOME=/home/pi
DIR=$PIHOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME

UNIXTIME_CURRENT=$(date +"%s")
UNIXTIME_FILE=$(date -r $FILE +"%s")
TDIFF=$(expr $UNIXTIME_CURRENT - $UNIXTIME_FILE)


UPTIME=$(</proc/uptime)
UPTIME=${UPTIME%%.*}

if [[ $TDIFF -gt 300 ]] && [[ $UPTIME -gt 300 ]];
then
    echo "It\'s been $TDIFF s since last photo was taken (uptime: $UPTIME s), rebooting at $DATETIME ."
    sudo shutdown -r now
fi
