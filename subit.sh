#!/bin/bash

youtube-dl -f best https://www.youtube.com/watch?v=bdTN-z90eM4 -o pso2_ep1.mp4
./main.py \
    'https://docs.google.com/spreadsheets/d/1d4jA47BvdUpiCfmhBhiY65anvnCCZgRoGjARjj3G63I/export?format=csv&id=1d4jA47BvdUpiCfmhBhiY65anvnCCZgRoGjARjj3G63I&gid=0' \
    'pso2_ep1.mp4'