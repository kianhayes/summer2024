#!/bin/bash

python /home/haye6406@benedictine.edu/summer2024/scripts/quick_plot.py

ffmpeg -r 25 -i %1d.png ../output.mp4 