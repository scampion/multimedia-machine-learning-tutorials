#!/bin/sh 
mkdir -p data/query 
cd data/query 
wget http://media.la-bas.org/mp3/101216/101216.mp3
ffmpeg -i 101216.mp3 -ss 0:01:20 -t 10 speech.mp3
ffmpeg -i 101216.mp3 -ss 0:55:05 -t 10 music.mp3
ffmpeg -i 101216.mp3 -ss 1:01:05 -t 10 both.mp3