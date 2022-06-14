#!/bin/bash

DATETIME=`date +"%Y-%m-%dT%T"`
DIR=$HOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME

cp $FILE $DIR/$DATETIME.jpg
