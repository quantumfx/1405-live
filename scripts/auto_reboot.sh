#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME
UNIXTIME_CURRENT=$(date +"%s")
UNIXTIME_FILE=$(date -r $FILE +"%s")
TDIFF=$(expr $UNIXTIME_CURRENT - $UNIXTIME_FILE)

if [ $TDIFF -gt 300 ];
then
#    echo "It\'s been $TDIFF s since last photo was taken, rebooting at $DATETIME ."
#    sudo /sbin/shutdown -r now
fi
