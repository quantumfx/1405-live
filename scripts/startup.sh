#!/bin/bash

source $HOME/miniconda3/etc/profile.d/conda.sh
$HOME/miniconda3/bin/conda activate 1405-live
python $HOME/rpi_live/webserver.py
