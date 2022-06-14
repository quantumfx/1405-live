#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live
FILENAME=temp_humidity_current.csv
FILE=$DIR/$FILENAME

python $DIR/scripts/temp_hum.py
cat $FILE | ssh -T sagan "cat - >> /home/fx/rpi_live/temp_humidity.csv"
