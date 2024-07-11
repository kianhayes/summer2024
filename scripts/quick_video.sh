#!/bin/bash

### Outputs a video of all data files in the directory data/run/data/plots/ if the current working directory is where the data is located

python /home/khayes/summer2024/scripts/plot_all.py

ffmpeg -r 25 -i %1d.png ../output.mp4 