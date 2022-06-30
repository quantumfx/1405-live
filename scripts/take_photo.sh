#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live/photos
FILENAME=current.jpg
FILE=$DIR/$FILENAME

killall libcamera-still
libcamera-still --vflip --hflip --immediate -t 30000 --denoise cdn_hq -o $FILE --awb daylight --post-process-file $HOME/rpi_live/scripts/post-processing/nightmode.json
rsync -P $FILE sagan:~/rpi_live/photos/$FILENAME
