#!/bin/bash

DATETIME=$(date +"%Y-%m-%dT%T")
DIR=$HOME/rpi_live/logs

rsync -P $DIR/* sagan:~/rpi_live/logs/
