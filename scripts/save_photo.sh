#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME

UNIXTIME_CURRENT=$(date +"%s")
UNIXTIME_FILE=$(date -r $FILE +"%s")
TDIFF=$(expr $UNIXTIME_CURRENT - $UNIXTIME_FILE)

if [[ $TDIFF -lt 100 ]]
then
    cp $FILE $DIR/$DATETIME.jpg
fi
